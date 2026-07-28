## Enum: GroupTypeEnum 




_Typen politischer Gruppen und Organisationen. Es gelten drei Konventionen._

__

_Der Wert benennt die politische Funktion, das Label der Gruppe bewahrt die örtliche Bezeichnung. Büro, Ratsleitung und Ufficio presidenziale werden alle als council_bureau erfasst und bleiben so vergleichbar._

__

_Zusammengehörende Werte tragen ein Präfix. Die Familie council_ unterscheidet nicht nach Rat: Staatskanzlei und Parlamentsdienste sind beide ein council_secretariat; welchem Rat ein Organ zugehört, sagt die übergeordnete Gruppe. Ebenso die Familie committee_ mit committee als Grundfall._

__

_Die drei Ratsorgane grenzen sich so ab: council_presidency führt die Sitzungen und vertritt den Rat; council_bureau leitet den Geschäftsgang und ist um die Fraktionsvertretung erweitert; council_secretariat ist die Verwaltungseinheit, besetzt mit Angestellten statt mit gewählten Mitgliedern._

__

_Die Rechtsform gehört nicht hierher, sondern in legal_form._

__



<div data-search-exclude markdown="1">

URI: [act:GroupTypeEnum](https://ld.ech.ch/schema/0294/actors/GroupTypeEnum)

### Zulässige Werte
| Wert | Beschreibung |
| --- | --- |
| party |  Politische Partei auf Bundes-, Kantons- oder Gemeindeebene. Jede föderale Ebene wird als eigene Gruppe geführt (z.B. Bundespartei, Kantonspartei, Gemeindesektion).  |
| | [act:enum/group_type/party](act:enum/group_type/party) |
| list |  Wahlliste (kann Teil einer Partei sein oder unabhängig).  |
| | [act:enum/group_type/list](act:enum/group_type/list) |
| workgroup |  Ad-hoc-Arbeitsgruppe, typischerweise mit begrenzter Laufzeit.  |
| | [act:enum/group_type/workgroup](act:enum/group_type/workgroup) |
| assembly |  Versammlung der Stimmberechtigten als gesetzgebendes Organ, insbesondere die Gemeindeversammlung. Anders als ein Rat ist sie kein gewähltes Gremium.  |
| | [act:enum/group_type/assembly](act:enum/group_type/assembly) |
| council_legislative |  Parlament auf Bundes-, Kantons- oder Gemeindeebene (z.B. Bundesversammlung, Nationalrat, Ständerat, Grosser Rat, Kantonsrat, Gemeindeparlament).  |
| | [act:enum/group_type/council_legislative](act:enum/group_type/council_legislative) |
| delegation |  Delegation.  |
| | [act:enum/group_type/delegation](act:enum/group_type/delegation) |
| committee |  Ständige Kommission, einschliesslich Aufsichtskommissionen (z.B. GPK), Sachkommissionen, Parlamentarische Untersuchungskommissionen (PUK) und Rechnungsprüfungskommissionen.  |
| | [act:enum/group_type/committee](act:enum/group_type/committee) |
| committee_ad_hoc |  Kommission, die für eine einzelne Aufgabe eingesetzt und nach deren Erledigung wieder aufgelöst wird, im Unterschied zur ständigen Kommission.  |
| | [act:enum/group_type/committee_ad_hoc](act:enum/group_type/committee_ad_hoc) |
| parliamentary_group |  Parlamentsfraktion.  |
| | [act:enum/group_type/parliamentary_group](act:enum/group_type/parliamentary_group) |
| council_bureau |  Organ, das den Geschäftsgang eines Rates leitet, unabhängig von der örtlichen Bezeichnung (Büro, Ratsleitung, Geschäftsleitung). Wird für den Legislativ- wie für den Exekutivrat verwendet; die örtliche Benennung wird im Label festgehalten.  |
| | [act:enum/group_type/council_bureau](act:enum/group_type/council_bureau) |
| council_presidency |  Präsidium eines Rates, für den Legislativ- wie für den Exekutivrat.  |
| | [act:enum/group_type/council_presidency](act:enum/group_type/council_presidency) |
| council_executive |  Regierung / Exekutive als Gesamtorgan (z.B. Bundesrat, Regierungsrat, Stadtrat / Gemeinderat).  |
| | [act:enum/group_type/council_executive](act:enum/group_type/council_executive) |
| department |  Departement.  |
| | [act:enum/group_type/department](act:enum/group_type/department) |
| office |  Amt.  |
| | [act:enum/group_type/office](act:enum/group_type/office) |
| committee_extraparliamentary |  Kommission, die in der Regel von der Regierung eingesetzt wird, um die Verwaltung fachlich zu beraten und deren Geschäfte vorzuberaten; einzelne verfügen darüber hinaus über eigene Entscheidbefugnisse. Sie unterscheidet sich von einer parlamentarischen Kommission durch Zusammensetzung und Rechtsgrundlage: Ihre Mitglieder sind externe Fachleute und Interessenvertreterinnen und -vertreter statt Ratsmitglieder, und sie stützt sich auf das Organisationsrecht von Regierung und Verwaltung statt auf das Parlamentsrecht. Den Typ gibt es auf Bundes- wie auf Kantonsebene (z.B. die Wettbewerbskommission des Bundes; im Kanton Waadt die commissions extraparlementaires). Eine Kommission, deren Mitglieder Ratsmitglieder sind, fällt auch dann nicht unter diesen Wert, wenn sie bei der Exekutive angesiedelt ist; sie wird als Kommission oder Ad-hoc-Kommission mit dem Exekutivrat als übergeordneter Gruppe erfasst.  |
| | [act:enum/group_type/committee_extraparliamentary](act:enum/group_type/committee_extraparliamentary) |
| interest_group |  Interessengruppe aus der Zivilgesellschaft.  |
| | [act:enum/group_type/interest_group](act:enum/group_type/interest_group) |
| control_body |  Kontroll- oder Aufsichtsorgan (z.B. Eidgenössische Finanzkontrolle EFK, Aufsichtsbehörde AB-BA).  |
| | [act:enum/group_type/control_body](act:enum/group_type/control_body) |
| council_secretariat |  Verwaltungseinheit, die einen Rat bedient, unabhängig von der örtlichen Bezeichnung (Parlamentsdienste, Ratssekretariat, Staats-, Kantons-, Standes-, Stadt- oder Gemeindekanzlei). Wird für den Legislativ- wie für den Exekutivrat verwendet: Die Staatskanzlei ist die Stabsstelle des Exekutivrates, die Parlamentsdienste sind jene des Legislativrates.  |
| | [act:enum/group_type/council_secretariat](act:enum/group_type/council_secretariat) |
| court |  Gericht / Judikative auf jeder Ebene (z.B. Bundesgericht, Kantonsgericht, Bezirksgericht).  |
| | [act:enum/group_type/court](act:enum/group_type/court) |
| association |  Verein.  |
| | [act:enum/group_type/association](act:enum/group_type/association) |
| petition_carrier |  Petitionsträger.  |
| | [act:enum/group_type/petition_carrier](act:enum/group_type/petition_carrier) |
| university |  Universität oder Bildungseinrichtung als ausgelagerter Träger öffentlicher Aufgaben.  |
| | [act:enum/group_type/university](act:enum/group_type/university) |
| other |  Anderer Gruppentyp, nicht durch Standardkategorien abgedeckt.  |
| | [act:enum/group_type/other](act:enum/group_type/other) |







</div>