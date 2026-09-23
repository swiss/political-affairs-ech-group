\newpage

# Safety considerations

<!-- DRAFT — to be reviewed by the specialist group, technically and legally.
     Translation of the German chapter 08_sicherheitsueberlegungen.md. -->

This standard describes data about natural persons. Such data are personal data within the meaning of Art. 5 lit. a of the Swiss Federal Act on Data Protection (FADP, in force since 1 September 2023). Information on party affiliation, mandates and interest links allows political opinions to be inferred and therefore constitutes sensitive personal data (Art. 5 lit. c FADP).

The standard does not create a legal basis for publication. It structures data whose publication follows from the principle of transparency, from disclosure obligations of parliaments, or from consent. Whether a data element may be published is decided by the publishing body, not by the schema.

The following points require particular attention:

- **Legal basis per element.** Not every element of the schema is publishable in every context. The publishing body verifies, for each populated element, that a legal basis or consent exists.
- **Data minimisation.** Optional elements — in particular date of birth, address and contact details — are populated only where they are necessary for the purpose of the publication.
- **Private residential addresses.** Their publication is the subject of parliamentary initiatives (see Annex A). Where an address is required, a business or correspondence address is to be used where possible.
- **Aggregation.** Combining several sources can produce personality profiles that go beyond the purpose of any individual publication. Whoever combines data according to this standard re-examines the purpose limitation.
- **Historical values in references.** `PersonReference` and `GroupReference` retain local attributes as of the time of linking. They must not be interpreted as the current state.
- **Transmission and access.** Where data according to this standard are exchanged before they are public, the usual precautions apply: encrypted transport, access restricted to authorised persons, protection against modification during transmission.
- **Processing data from third parties.** Before further processing an incoming delivery, schema validation is performed. Content transmitted in free-text fields is escaped before display.
