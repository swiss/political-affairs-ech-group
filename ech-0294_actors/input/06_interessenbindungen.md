\newpage

# Interessenbindungen (Interest Links)

Das InterestLink-Schema erfasst Interessenbindungen, Interessenkonflikte und Verflechtungen von Personen mit Organisationen. Es orientiert sich an den Transparenzanforderungen für Parlamentsmitglieder gemäss [Bundesversammlung – Interessenbindungen](https://www.parlament.ch/centers/documents/de/interessen-nr.pdf).

- **Abgrenzung zu Mitgliedschaften (`Membership`):** `InterestLink` bildet Bindungen zu Organisationen *ausserhalb* des Akteur-Schemas ab (Interessenkonflikte, Politikfinanzierung) – im Unterschied zur formalen Zugehörigkeit *innerhalb* des Schemas, die über `Membership` erfasst wird.
- **Obligatorische Klassifikation (`interest_type`):** Jede Bindung wird zwingend nach Art eingeordnet (berufliche Tätigkeit, politische Ämter, Verein), angelehnt an die Offenlegungskategorien der Bundesversammlung.
- **Organisation über UID referenzierbar (`organization_uid`):** Ist die Organisation im UID-Register erfasst, wird sie über ihre UID (eCH-0098, `CHE-XXX.XXX.XXX`) referenziert – das ermöglicht Auswertungen, z. B. mit NOGA-Codes. Für Organisationen ohne UID stehen `organization_name`/`organization_address` bereit; die Rechtsform folgt einem kontrollierten Vokabular (`LegalFormEnum`).
- **Umfang und Entschädigung (`is_paid`, `committee`, `function_role`):** Neben Gremium und Funktion innerhalb der Organisation wird explizit festgehalten, ob die Position bezahlt ist – ein zentraler Transparenzaspekt.



{{include:ech-0294_actors/output/docs/InterestLink.md}}

{{include:ech-0294_actors/output/docs/InterestTypeEnum.md}}

{{include:ech-0294_actors/output/docs/LegalFormEnum.md}}