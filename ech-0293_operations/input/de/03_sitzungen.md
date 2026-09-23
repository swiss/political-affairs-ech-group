\newpage

<!-- ToDo: Christian -->

# Zeitliche Organisation des Ratsbetriebs

Der Ratsbetrieb ist zeitlich in vier Klassen gegliedert:

```
Legislature (Legislaturperiode)
  └─ Session (z.B. Frühjahrssession)
      └─ Meeting (einzelne Sitzung)
          └─ AgendaItem (Traktandum)
```

Die Legislaturperiode bildet den langfristigen Rahmen, die Session strukturiert die Arbeit innerhalb einer Legislaturperiode, das Meeting ist die konkrete Sitzung, in der Geschäfte beraten werden, und das Traktandum gliedert die einzelne Sitzung. Die Ebenen greifen auf zwei Arten ineinander: Nach unten sind sie eingebettet — die Session nimmt ihre Sitzungen auf (`meetings`), Sitzung und Session ihre Traktanden (`agenda_items`); nach oben zeigen Referenzen — die Session verweist auf ihre Legislaturperiode (`parent_legislature`), die Sitzung auf ihre Session (`parent_session`) oder, wo es keine Session gibt, direkt auf die Legislaturperiode (`parent_legislature`). Innerhalb der Traktandenliste bildet `parent_agenda_item` die Gliederung in Untertraktanden ab.

Die ersten drei Klassen sind nachfolgend beschrieben, das Traktandum im nächsten Kapitel.

## Gemeinsame Elemente

Die drei Klassen sind bewusst gleich gebaut. Die folgenden Felder haben auf allen Ebenen dieselbe Bedeutung.

**Identifikation.** `global_uri` ist der Identifikator und obligatorisch. `local_id` nimmt die Id des liefernden Systems auf, `wikidata_uri` verweist auf den Wikidata-Eintrag, sofern es einen gibt.

**Beginn und Ende.** Die Zeitangaben werden doppelt geführt: `date_begin_planned` und `date_end_planned` halten fest, was angesetzt war, `date_begin_actual` und `date_end_actual`, was tatsächlich geschah. Wo die Uhrzeit relevant ist, stehen die Varianten `datetime_*` zur Verfügung.

**Raum und Organ.** `spatial` verweist auf die Raumeinheit gemäss LINDAS — Land, Kanton, Bezirk oder Gemeinde, also `https://ld.admin.ch/canton/2` statt „BE". Es ist dasselbe Feld, mit dem eCH-0294 seine Gruppen verortet, sodass ein Ratsbetrieb und die Akteure, die ihn tragen, auf dieselbe Ressource zeigen. Wer innerhalb dieser Raumeinheit tagt, sagt `actor_id` als Kurzreferenz auf das Organ gemäss eCH-0294.

**Verlinkte Dokumente.** `documents` verknüpft Dokumente als FRBR-Works gemäss eCH-0292 — bei der Legislaturperiode etwa Mitglieder- und Geschäftsverzeichnisse, bei der Session das Sessionsprogramm, beim Meeting Tagblatt und Beilagen (das Protokoll hingegen über `has_protocol`).

## Legislature (Legislaturperiode)

Eine Legislaturperiode bezeichnet den Zeitraum, für den ein Parlament gewählt wird und in seiner aktuellen Zusammensetzung tätig ist.

{{include:ech-0293_operations/output/docs/Legislature.md}}

## Session (Sitzungsperiode)

Eine Session ist eine zusammenhängende Sitzungsperiode, in der mehrere Meetings stattfinden.

{{include:ech-0293_operations/output/docs/Session.md}}

## Meeting (Einzelne Sitzung)

Ein Meeting ist die einzelne Sitzung eines Organs — die Ebene, auf der Traktanden beraten, Beschlüsse gefasst und Wortmeldungen festgehalten werden.

{{include:ech-0293_operations/output/docs/Meeting.md}}

{{include:ech-0293_operations/output/docs/StateEnum.md}}
