\newpage

# Liens d'intérêts (Interest Links)

Le schéma InterestLink consigne les liens d'intérêts, les conflits d'intérêts et les imbrications des personnes avec des organisations. Il s'appuie sur les exigences de transparence applicables aux membres du parlement selon [Assemblée fédérale – Liens d'intérêts](https://www.parlament.ch/centers/documents/de/interessen-nr.pdf).

- **Délimitation par rapport aux affiliations (`Membership`) :** `InterestLink` représente les liens avec des organisations *extérieures* au schéma des acteurs (conflits d'intérêts, financement de la politique) – par opposition à l'appartenance formelle *au sein* du schéma, qui est consignée au moyen de `Membership`.
- **Classification obligatoire (`interest_type`) :** chaque lien est obligatoirement classé selon son type (activité professionnelle, mandats politiques, association), en s'appuyant sur les catégories de divulgation de l'Assemblée fédérale.
- **Organisation référençable par IDE (`organization_uid`) :** si l'organisation est enregistrée dans le registre IDE, elle est référencée au moyen de son IDE (eCH-0097, `CHE-XXX.XXX.XXX`) – ce qui permet des analyses, p. ex. à l'aide de codes NOGA. Pour les organisations sans IDE, `organization_name`/`organization_address` sont disponibles ; la forme juridique suit un vocabulaire contrôlé (`LegalFormEnum`).
- **Étendue et rémunération (`is_paid`, `committee`, `function_role`) :** outre l'organe et la fonction au sein de l'organisation, il est explicitement consigné si la position est rémunérée – un aspect central de la transparence.



{{include:ech-0294_actors/output/docs/InterestLink.md}}

{{include:ech-0294_actors/output/docs/InterestTypeEnum.md}}

{{include:ech-0294_actors/output/docs/LegalFormEnum.md}}