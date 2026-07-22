#!/usr/bin/env bash
# Direct DOCX -> PDF conversion via LibreOffice headless.
#
#   docx_to_pdf.sh <input.docx> <output.pdf>
#
# Renders the actual Word document (reference-doc styling, footer, tables) and
# — via the bundled Basic macro (scripts/lo-macro) — updates the fields and the
# table of contents first, so the TOC is populated in the PDF (a plain
# `soffice --convert-to pdf` leaves the TOC field placeholder).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

IN_ABS="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
OUT_DIR="$(cd "$(dirname "$2")" && pwd)"
OUT_ABS="$OUT_DIR/$(basename "$2")"

SOFFICE="$(command -v soffice || command -v libreoffice)"

# Isolated LibreOffice profile carrying our conversion macro.
PROFILE="${LO_PROFILE:-$(mktemp -d)/lo_profile}"
mkdir -p "$PROFILE/user/basic"
# Warm up first so LibreOffice creates a valid profile; only then seed the Basic
# library (a Basic macro is not recognised in a not-yet-initialised profile).
timeout 120 "$SOFFICE" --headless --terminate_after_init \
  -env:UserInstallation="file://$PROFILE" || true
cp -R "$SCRIPT_DIR/lo-macro/." "$PROFILE/user/basic/"

rm -f "$OUT_ABS"
export LO_IN="$IN_ABS" LO_OUT="$OUT_ABS"
# Guard against a hang if the macro errors before terminating LibreOffice.
timeout 180 "$SOFFICE" --headless --norestore --invisible --nofirststartwizard \
  -env:UserInstallation="file://$PROFILE" \
  "macro:///Standard.Module1.Run"

if [ ! -f "$OUT_ABS" ]; then
  echo "docx_to_pdf.sh: PDF was not created: $OUT_ABS" >&2
  exit 1
fi
echo "docx_to_pdf.sh: wrote $OUT_ABS"
