#!/usr/bin/env bash
#
# docx_to_pdf.sh <in.docx> <out.pdf>
#
# Render a DOCX to PDF via LibreOffice headless, updating the Word table-of-
# contents field(s) first so the PDF's TOC is populated with page numbers.
# A plain `soffice --convert-to pdf` does NOT update fields, so the TOC would
# otherwise stay empty; this uses a one-shot Basic macro that refreshes all
# indexes and text fields and then exports the PDF.
#
# Requires: libreoffice / soffice on PATH (override with SOFFICE=...).

set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "usage: docx_to_pdf.sh <in.docx> <out.pdf>" >&2
  exit 2
fi

DOCX="$1"
PDF="$2"
SOFFICE_BIN="${SOFFICE:-soffice}"
command -v "$SOFFICE_BIN" >/dev/null 2>&1 || { echo "docx_to_pdf.sh: '$SOFFICE_BIN' not on PATH (set SOFFICE=...)" >&2; exit 3; }

ABS_DOCX="$(cd "$(dirname "$DOCX")" && pwd)/$(basename "$DOCX")"
ABS_PDF="$(cd "$(dirname "$PDF")" && pwd)/$(basename "$PDF")"
DOCX_URL="file://$ABS_DOCX"
PDF_URL="file://$ABS_PDF"

# Disposable profile carrying a one-shot macro (never touches the real profile).
PROFILE="$(mktemp -d)"
trap 'rm -rf "$PROFILE"' EXIT
STD="$PROFILE/user/basic/Standard"
mkdir -p "$STD" "$PROFILE/user/basic"

cat > "$STD/Module1.xba" <<'XBA'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE script:module PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "module.dtd">
<script:module xmlns:script="http://openoffice.org/2000/script" script:name="Module1" script:language="StarBasic">
Sub UpdateAndPdf(sUrl As String, sPdf As String)
    Dim oDoc As Object, a(0) As New com.sun.star.beans.PropertyValue
    a(0).Name = "Hidden" : a(0).Value = True
    oDoc = StarDesktop.loadComponentFromURL(sUrl, "_blank", 0, a())
    On Error Resume Next
    oDoc.getTextFields().refresh()
    Dim oIdx As Object : oIdx = oDoc.getDocumentIndexes()
    Dim i As Integer
    For i = 0 To oIdx.getCount() - 1
        oIdx.getByIndex(i).update()
    Next i
    oDoc.refresh()
    Dim p(0) As New com.sun.star.beans.PropertyValue
    p(0).Name = "FilterName" : p(0).Value = "writer_pdf_Export"
    oDoc.storeToURL(sPdf, p())
    oDoc.close(False)
End Sub
</script:module>
XBA

cat > "$STD/script.xlb" <<'XLB'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE library:library PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "library.dtd">
<library:library xmlns:library="http://openoffice.org/2000/library" library:name="Standard" library:readonly="false" library:passwordprotected="false">
 <library:element library:name="Module1"/>
</library:library>
XLB

cat > "$PROFILE/user/basic/script.xlb" <<'XLB'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE library:libraries PUBLIC "-//OpenOffice.org//DTD OfficeDocument 1.0//EN" "libraries.dtd">
<library:libraries xmlns:library="http://openoffice.org/2000/library" xmlns:xlink="http://www.w3.org/1999/xlink">
 <library:library library:name="Standard" xlink:href="$(USER)/basic/Standard/script.xlb" xlink:type="simple" library:link="false"/>
</library:libraries>
XLB

rm -f "$ABS_PDF"
# A brand-new profile can skip macro registration on its very first boot, so retry.
for attempt in 1 2 3; do
  "$SOFFICE_BIN" --headless --norestore --invisible \
    -env:UserInstallation="file://$PROFILE" \
    "macro:///Standard.Module1.UpdateAndPdf($DOCX_URL,$PDF_URL)" >/dev/null 2>&1 || true
  [ -s "$ABS_PDF" ] && break
done

[ -s "$ABS_PDF" ] || { echo "docx_to_pdf.sh: ERROR — PDF not created for $DOCX" >&2; exit 1; }
echo "docx_to_pdf.sh: wrote $PDF (TOC updated)"
