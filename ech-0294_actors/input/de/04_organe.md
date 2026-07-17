\newpage

# Gruppen und Organe (Groups)

Das Group-Schema bildet politische Gruppen, Organisationen und Körperschaften ab.

- **Ein generisches Modell statt vieler Spezialklassen:** Parlamente, Parteien, Fraktionen, Kommissionen, Departemente, Gerichte und zivilgesellschaftliche Organisationen werden alle als *eine* Klasse `Group` abgebildet und über `group_type` unterschieden. Das hält das Modell einfach und ohne Schemaänderung erweiterbar – Legislative, Exekutive, Judikative und Zivilgesellschaft sind damit gleichermassen abbildbar.
- **Gruppen und Sub-Gruppen über `parent_groups`:** Untergeordnete Gruppen verweisen auf ihre übergeordnete Gruppe – z. B. eine Kommission des Ständerats, eine Subkommission innerhalb einer Kommission, eine Kantonalpartei unter ihrer Mutterpartei oder eine Behörde innerhalb einer Direktion. Die Hierarchie entsteht so aus diesen Verweisen statt aus einer festen Ebenenstruktur. Sie bleibt meist innerhalb desselben `group_type`; typenübergreifende und mehrfache Verweise sind aber möglich (z. B. eine Fraktion, die zugleich auf ihr Parlament und ihre Partei verweist).
- **Zeitliche Gültigkeit auch für Gruppen:** Über `valid_from`/`valid_through` lassen sich z. B. nur während einer Legislatur bestehende Kommissionen oder Umbenennungen und Fusionen von Parteien abbilden.

{{include:ech-0294_actors/output/docs/Group.md}}

{{include:ech-0294_actors/output/docs/GroupType.md}}

{{include:ech-0294_actors/output/docs/GroupTypeEnum.md}}