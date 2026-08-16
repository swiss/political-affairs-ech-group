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

## Änderungen und Zeitverläufe

Ein Erlass ändert andere und wird selbst geändert. Akoma Ntoso hält das im Analyseblock fest, und zwar auf der Ebene der Textstelle: Eine Änderung nennt die Stelle, die sie bewirkt (`akn:source`), die Stelle, die sie trifft (`akn:destination`), und bei einer Textänderung den bisherigen und den neuen Wortlaut (`akn:old`, `akn:new`). Der Typ sagt, was geschieht — eingefügt, ersetzt, aufgehoben, neu nummeriert, geteilt, zusammengeführt — oder, bei einer Änderung der Rechtskraft, ob etwas in Kraft tritt, ausser Kraft fällt oder aufgeschoben wird.

Wann eine Änderung gilt, steht nicht bei ihr, sondern hinter einem Verweis: `@period` zeigt auf eine Zeitgruppe, deren Intervall wiederum auf Datumselemente im Text zeigt. Diese Umleitung ist Absicht — dasselbe Datum trägt oft mehrere Änderungen, und im Text steht es ohnehin.

Der Bund nutzt diesen Block nicht: Fedlex liefert konsolidierte Fassungen mit Datumsangaben, ohne die einzelnen Änderungsschritte auszuweisen. Der Kanton Zürich tut es, und daran zeigt sich, worüber bei der Zuordnung zu ELI zu entscheiden ist: ELI kennt Beziehungen zwischen *Erlassen* (`eli:amends`, `eli:repeals`, `eli:consolidates`), Akoma Ntoso beschreibt Änderungen zwischen *Textstellen*. Aus „diese Passage wurde am 1. Juni 2007 ersetzt" wird nicht von selbst „Erlass A ändert Erlass B"; diese Hochrechnung ist eine fachliche Entscheidung und steht noch aus.

{{include:ech-0296_laws/output/docs/Analysis.md}}

{{include:ech-0296_laws/output/docs/ActiveModifications.md}}

{{include:ech-0296_laws/output/docs/PassiveModifications.md}}

{{include:ech-0296_laws/output/docs/Modification.md}}

{{include:ech-0296_laws/output/docs/TextualMod.md}}

{{include:ech-0296_laws/output/docs/ForceMod.md}}

{{include:ech-0296_laws/output/docs/ModTypeEnum.md}}

{{include:ech-0296_laws/output/docs/ModSource.md}}

{{include:ech-0296_laws/output/docs/ModDestination.md}}

{{include:ech-0296_laws/output/docs/ModOld.md}}

{{include:ech-0296_laws/output/docs/ModNew.md}}

{{include:ech-0296_laws/output/docs/TemporalData.md}}

{{include:ech-0296_laws/output/docs/TemporalGroup.md}}

{{include:ech-0296_laws/output/docs/TimeInterval.md}}
