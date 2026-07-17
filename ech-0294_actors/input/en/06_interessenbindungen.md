\newpage

# Interest Links

The InterestLink schema records interest links, conflicts of interest and entanglements of persons with organisations. It is based on the transparency requirements for members of parliament according to [Federal Assembly – Interest Links](https://www.parlament.ch/centers/documents/de/interessen-nr.pdf).

- **Distinction from memberships (`Membership`):** `InterestLink` represents links to organisations *outside* the actor schema (conflicts of interest, political financing) – in contrast to the formal affiliation *within* the schema, which is recorded via `Membership`.
- **Mandatory classification (`interest_type`):** Every link is mandatorily categorised by type (professional activity, political offices, association), based on the disclosure categories of the Federal Assembly.
- **Organisation referenceable via UID (`organization_uid`):** If the organisation is recorded in the UID register, it is referenced via its UID (eCH-0097, `CHE-XXX.XXX.XXX`) – this enables analyses, e.g. with NOGA codes. For organisations without a UID, `organization_name`/`organization_address` are available; the legal form follows a controlled vocabulary (`LegalFormEnum`).
- **Scope and remuneration (`is_paid`, `committee`, `function_role`):** In addition to the committee and function within the organisation, it is explicitly recorded whether the position is paid – a central transparency aspect.



{{include:ech-0294_actors/output/docs/InterestLink.md}}

{{include:ech-0294_actors/output/docs/InterestTypeEnum.md}}

{{include:ech-0294_actors/output/docs/LegalFormEnum.md}}
