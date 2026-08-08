\newpage

# Gruppen und Organe (Groups)

Das Group-Schema bildet politische Gruppen, Organisationen und Körperschaften ab.

- **Ein generisches Modell statt vieler Spezialklassen:** Parlamente, Parteien, Fraktionen, Kommissionen, Departemente, Gerichte und zivilgesellschaftliche Organisationen werden alle als *eine* Klasse `Group` abgebildet und über `group_type` unterschieden. Das hält das Modell einfach und ohne Schemaänderung erweiterbar – Legislative, Exekutive, Judikative und Zivilgesellschaft sind damit gleichermassen abbildbar.
- **Gruppen und Sub-Gruppen über `parent_groups`:** Untergeordnete Gruppen verweisen auf ihre übergeordnete Gruppe – z. B. eine Kommission des Ständerats, eine Subkommission innerhalb einer Kommission, eine Kantonalpartei unter ihrer Mutterpartei oder eine Behörde innerhalb einer Direktion. Die Hierarchie entsteht so aus diesen Verweisen statt aus einer festen Ebenenstruktur. Sie bleibt meist innerhalb desselben `group_type`; typenübergreifende Verweise sind aber möglich (z. B. eine Fraktion, die auf ihr Parlament verweist). Massgebend ist dabei allein die Über-/Unterordnung: Die Parteien, welche eine Fraktion tragen, sind ihr nicht übergeordnet. Ihr Verhältnis zur Fraktion bleibt im Standard bewusst unabgebildet – es ist keine Hierarchie, und eine tragfähige allgemeine Form dafür gibt es nicht, weil Fraktionen je nach Rat unterschiedlich eng an Parteien gebunden sind. Wo die Zugehörigkeit sichtbar sein muss, tut sie es über die Mitgliedschaften der einzelnen Personen. Der Verweis erfolgt als `GroupReference` – dieselbe Form, mit der eine Mitgliedschaft ihre Gruppe benennt. Dass es sich um eine Über-/Unterordnung handelt, sagt dabei der Slot `parent_groups` selbst; die Referenz trägt nur die Adressierung. Diese kann über die `local_id` erfolgen, wenn die übergeordnete Gruppe Teil derselben Lieferung ist, oder über die `global_uri`, wenn sie ausserhalb liegt – eine Kantonalpartei kann so auf ihre Bundespartei verweisen, ohne dass diese mitgeliefert werden muss. Sind beide bekannt, werden beide angegeben.
- **Zeitliche Gültigkeit auch für Gruppen:** Über `valid_from`/`valid_through` lassen sich z. B. nur während einer Legislatur bestehende Kommissionen oder Umbenennungen und Fusionen von Parteien abbilden.

{{include:ech-0294_actors/output/docs/Group.md}}

{{include:ech-0294_actors/output/docs/GroupType.md}}

{{include:ech-0294_actors/output/docs/GroupTypeEnum.md}}