\newpage

# Metadaten

Der Metadatenblock `akn:meta` versammelt alles, was ein Dokument beschreibt, ohne Teil seines Textes zu sein: die FRBR-Identifikation (siehe Kapitel Identifikation) und die Referenzen auf die beteiligten Stellen und Rollen.

{{include:ech-0296_laws/output/docs/ActMeta.md}}

## Referenzen auf Akteure und Rollen

Personen, Organisationen und Rollen werden nicht im Text selbst beschrieben, sondern einmal im Abschnitt `akn:references` deklariert; die Elemente des Dokuments verweisen anschliessend über einen dokumentinternen Anker darauf (`href="#ch.bk"`). So bleibt die Angabe an einer Stelle, auch wenn sie im Dokument mehrfach vorkommt.

{{include:ech-0296_laws/output/docs/References.md}}

{{include:ech-0296_laws/output/docs/TLCOrganization.md}}

{{include:ech-0296_laws/output/docs/TLCRole.md}}

{{include:ech-0296_laws/output/docs/TLCReference.md}}

{{include:ech-0296_laws/output/docs/FedlexRoleEnum.md}}

## Werte, Sprache und Format

Mehrere AKN-Elemente tragen ihren Inhalt nicht als Text, sondern in einem Attribut — `value`, `href`, `language` oder `format`. Dafür stehen eigene kleine Klassen, damit die Attributform im Modell sichtbar bleibt.

{{include:ech-0296_laws/output/docs/ValueType.md}}

{{include:ech-0296_laws/output/docs/UriValueType.md}}

{{include:ech-0296_laws/output/docs/LanguageType.md}}

{{include:ech-0296_laws/output/docs/FormatType.md}}

{{include:ech-0296_laws/output/docs/DocumentLanguageEnum.md}}

## Anmerkungen und weitere Verweise

Anmerkungen stehen nicht im Text, sondern im Metadatenblock; der Text verweist mit `akn:noteRef` darauf. Dazu kommen Verweise, die den Erlass in seinem Umfeld verorten: auf die ursprüngliche Fassung, auf die Erlasse, die er ändert, und auf Begriffe wie den zeitlichen Status.

{{include:ech-0296_laws/output/docs/Notes.md}}

{{include:ech-0296_laws/output/docs/Note.md}}

{{include:ech-0296_laws/output/docs/OriginalRef.md}}

{{include:ech-0296_laws/output/docs/ActiveRef.md}}

{{include:ech-0296_laws/output/docs/TLCConcept.md}}
