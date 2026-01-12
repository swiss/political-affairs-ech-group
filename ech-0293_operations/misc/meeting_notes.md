## 12.06.2025 ##

**Meeting Items**

- [Sessionenprogramm SR (Parlament.ch)](https://www.parlament.ch/de/ratsbetrieb/sessionen/sessionsprogramme-sr?CouncilId=2&SessionId=2025+II)  
- [Ordine del giorno GC (TI)](https://www4.ti.ch/poteri/gc/attivita/ordine-del-giorno)  
- [Traktanden BE](https://www.gr.be.ch/de/start/grosser-rat/open-data-angebot-gr/datensaetze-und-dokumentation.html)  
- [E-Traktandenliste Grosser Rat (AG)](https://www.ag.ch/grossrat/grweb/de/186/E-Traktandenliste?SitzungId=23805)
- [VS](https://parlement.vs.ch/app/fr/search/parl_session/264452?date=2025-06-10)
- [BS](https://grosserrat.bs.ch/ratsbetrieb/tagesordnung)
- [TG](https://parlament.tg.ch/public/upload/assets/176389/01%20Tagesordnung%20der%20Grossratssitzung%20vom%2018.%20Juni%202025.pdf?fp=1)

OPAR: https://oparl.org/spezifikation/online-ansicht/#entity-agendaitem

Besprochen:

- Traktanden haben können ein oder mehrere federührende Departments haben, die häufig als Gruppierungselemente (BE, TI, AG) in der Darstellung genutzt werden.
- Recapp extrahiert Traktadum und Details
- BE hat Titel (Geschätstitel) und Untertitel
  - Details und Subitel können über Description abgebildet werden.
- Problematik: Traktanden können während der Beratung gemeinsam behandelt werden.
  -  BE: Beschluss wird beim ersten Traktdum ergänzt, Hinweis beim 2,3.. das dies gemeinsam Behandelt wurde
 
- Wir bilden diese Thematik damit mit einer neuen Klasse JointDebate ab, welche die gemeinsam behandelten Traktanden aufführt und damit zusammenfasst.

## 19.06.2025 ##
- Arbeit direkt im Schema


## 2026 ##

Todo Alt

- Abstimmungstypen - Wahl und Abstimmung unterschiedlich?
- Handling Präsidium
- Absolutes / Relatives Mehr
- Rolle bei Abstimmung
- Verknüpfung

Todo Neu
- Bestimmung Roles Actor für Legislatur, meeting, Agenda_item Siehe GroupReference und ActorReference: https://github.com/swiss/political-affairs-ech-group/blob/main/ech-0294_actors/input/schema.yaml

