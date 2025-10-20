## Meeting Notes 20 October 2025

– FRBR
- [Liste Vokabular](https://docs.google.com/spreadsheets/d/1taUeu5BWyzboI01Hmde-G_TbGklVjgDgaKvjBqixMjs/edit?gid=0#gid=0)
- ...

## Meeting Notes 22 September 2025

- dependencies (cf. https://github.com/swiss/political-affairs-ech-group/blob/main/docs/resolved_dependencies_2025-09-01.md)
     - Versionisierung (bei Fehlern): später
     - Timeline -> (Timestamps, Activities): Michael und Benedikt machen Vorschlag
- see: https://github.com/swiss/political-affairs-ech-group/blob/main/ech-0292_meta/input/schema_workin.yml
     - to do: Michael und Benedikt: linkml
     - to do: Florin: [Liste Vokabular](https://docs.google.com/spreadsheets/d/1taUeu5BWyzboI01Hmde-G_TbGklVjgDgaKvjBqixMjs/edit?gid=0#gid=0) von Fabian Ligibel ☑️
- regelmässige Meetings: monatlich? 11:00 - 12:00 Montag -> Florin lädt ein ☑️

## Meeting Notes 16. Juli 2025
 
 -  Activity i.e. event (vs. business object/state) based model
     - vgl. [paf.link](https://paf.link) / Prov-O
     - Aktivität (mit Zeitraum) + Agent (Person/en, Gruppierung) + Entität (+ Identifikator)
     - Vorteil: Flexibilität, Modularität (Prozesse Stück für Stück abbilden) etc. siehe [paf.link](https://paf.link/#event-based-approach)
     - Nachteil: anfangs komplexer, braucht "Übersetzung" in einfachen aktuellen Status
     - Perspektive Legislative (vs. Exekutive) > paf.link würde Kompatibiltät ermöglichen 
- Priorisierung
- recurring meetings 


- 1. Vision / Scope / Life-Cycle
- 2. Chronologie / Prozesse
- 3. Verknüpfungen (von Events)
- 4. Dokumente (Chronologisch verordnet)
- 5. Publikationsvorgehen Vorschlagen
  - wo möglich unabhängige Publikation und Vorteile davon auflisten.- 
- 6. Guidelines Zugriff (Files, API)
- 7. Permanente URL/URI/DOI (gegen Linkrot) (ggf. via Hilfsmittel), an ELI orientieren (?)
- 8. Ablaufdaten für Links, Links zur Archivierung (vgl. [Kanton Uri](https://staur-digitalplattform.ch/tonaufnahmen/))


 ## Meeting Notes 10. Juni 2025

 - Review Mini Gap Analysis (siehe oben)
 - Prozess: Anforderungen zwischen Meta-Gruppe aus Subgruppen sammeln bzw. Kommunikations-/Entscheidungsfluss
   - via GitHub Issues / -> Template: Gruppe / Problemtyp / Wished Due Date / Prio
 - "Transition"/Verbindung von einem Geschäft zum nächsten/related (insb. Exekutive - Legislative)
   - Vernehmlassung - Geschäft im Rat
   - (in)direkter Gegenvorschlag
   - Beispiele:
     - Link Volksinitative - Parlamentarisches Geschäft: https://www.bk.admin.ch/ch/d/pore/vi/vis515.html
   - Link Auswertung Bundesgesetzesänderung: https://www.bsv.admin.ch/bsv/de/home/sozialversicherungen/ueberblick/reformen-revisionen/modernisierung_aufsicht.html
   - SH Parlament: https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Parlament/Der-Kantonsrat/Portal-Kantonsrat---Ratsbetrieb-15931135-DE.html -> 
https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Parlament/Der-Kantonsrat/Portal-Kantonsrat---Ratsbetrieb/Vorlagen-Parlament-17071346-DE.html (ADS 25-23)
SH Regierung:
https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Parlament/Der-Kantonsrat/Portal-Kantonsrat---Ratsbetrieb/Vorlagen-Regierung-15910026-DE.html (ADS 24-146)

## Meeting Notes 22. April 2025

Mögliche Namen der Subgruppe:

1. “Generische Politische Geschäfte im Prozess”
2. “Abstrakte Aktivitäten der politischen Geschäfte”
3. “Generische Chronologie der politischen Geschäfte”
4. “Metainformation und Links zu politischen Geschäften”
5. **“Metaprozesse zu politischen Geschäften”** --> gewählt




## Zielgruppen und Prioritäten:

1. Andere eCH PoGe Subgruppen (Schema basis)
2. Städte / Bund / Kantone (Publikation)
3. Journalisten / OpenData Swiss / DCAT-AP-CH (Auffindbar machen)
4. Politmonitor/OparlData (Konsum, Monitoring, Veredlung)
5. Öffentliche Verwaltung (Statistikämter, Konsum, Monitoring)
6. Forschung: Politikwissenschaft / Historiker (Forschung)

## Mini Gap Analysis (inkl. Eränzungen 10.06.):

- Dokumente (Chronologisch verordnet)
  - Versionen / Publikationsdatum
  - Kommissionsberichte und Postulatsberichte
  - Referenden und Volksinitiativen (Ablaufen und Inkrafttreten)
  - [FRBR Model]([url](https://www.loc.gov/catdir/cpso/frbreng.pdf)): Work (z.b. Geschäft) - Expression (e.g. DE/FR/EN) - Manifestation (e.g. PDF) (- Item)

- Chronologie / Prozesse
  - Räte sehr unterschiedlich (teils einfacher)
  - Übergeben und Abschliessen (unterschiedliche Semantik in Kantonen)
  - Vergleichbarkeit über Kantone und föderale Stufen hinweg (Scope: Parlamente)
  - Logik: abbilden, was passiert (vs. wie der Prozess abläuft (stärker kausal))

- Verknüpfungen (von Events)
  - Vernehmlassung (und Anhörungen) und Ratsgeschäft
  - Ratsgeschäft zu Gesetzteserlass
  - Ratsgeschäft und Medienmitteilung
  - Exekutivbeschlüsse mit Geschäften (z.B. Inkrafttreten)
  - Identifikation "mitnehmen" von einem zum "related" Geschäft

- Guidelines Zugriff (Files, API)
- Permanente URL/URI/DOI (gegen Linkrot) (ggf. via Hilfsmittel), an ELI orientieren (?)
- Ablaufdaten für Links, Links zur Archivierung (vgl. [Kanton Uri](https://staur-digitalplattform.ch/tonaufnahmen/))


