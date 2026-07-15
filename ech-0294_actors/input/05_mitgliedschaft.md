\newpage

# Mitgliedschaften (Memberships)

Das Membership-Schema bildet die Beziehung zwischen Personen und Gruppen ab und ist das zentrale Bindeglied im Akteur-Schema.

- **Abgrenzung zu Interessenbindungen (`InterestLink`):** `Membership` erfasst die *formale Zugehörigkeit* einer Person zu einer Gruppe innerhalb des Akteur-Schemas (z. B. Partei-, Kommissions- oder Parlamentsmitgliedschaft). Interessenbindungen und Interessenkonflikte zu Organisationen *ausserhalb* des Schemas sind bewusst davon getrennt und werden über `InterestLink` abgebildet (siehe folgendes Kapitel).
- **Referenzen mit Snapshot statt Einbettung (`person_reference`/`group_reference`):** Eine Mitgliedschaft verweist über leichtgewichtige Referenzen auf Person und Gruppe und hält dabei deren wichtigste Identifikationsmerkmale zum Zeitpunkt der Verknüpfung fest. So bleibt der Eintrag historisch korrekt, auch wenn sich Person oder Gruppe später ändern.
- **Aktivität explizit oder abgeleitet (`is_active`):** Ob eine Mitgliedschaft aktiv ist, kann explizit über `is_active` gesetzt oder aus der zeitlichen Gültigkeit abgeleitet werden. Ist `is_active` nicht gesetzt, ergibt sich die Aktivität aus `valid_from`/`valid_through`.
- **Mitgliedschaft ≠ Stimmrecht (`authorized_to_vote`):** Das Stimmrecht wird getrennt von der Mitgliedschaft geführt – typischerweise `false` bei Ersatzmitgliedern (ausser im Einsatz), Beobachtenden, dem Sekretariat und Gästen.
- **Rolle als kontrolliertes Vokabular mit Freitext-Option (`role_type`):** Die Rolle in der Gruppe (z. B. Mitglied, Präsidium, Stellvertretung) wird über ein kontrolliertes Vokabular (`RoleEnum`) angegeben; für nicht abgedeckte Rollen dient der Wert `other` mit einer freien Bezeichnung.

{{include:ech-0294_actors/output/docs/Membership.md}}
