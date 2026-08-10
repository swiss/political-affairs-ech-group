## Enum: InterestTypeEnum 




_Typen von Interessenbindungen (Interessenkonflikte, Politikfinanzierung)._




<div data-search-exclude markdown="1">

URI: [act:InterestTypeEnum](https://ld.ech.ch/schema/0294/actors/InterestTypeEnum)

### Zulässige Werte
| Wert | Beschreibung |
| --- | --- |
| professional_activity |  Erwerbstätigkeit ausserhalb des politischen Mandats: Anstellung, selbstständige Tätigkeit, das eigene operativ geführte Unternehmen. Bei Angestellten werden Arbeitgeber und Funktion angegeben. Prüffrage: Verdient die Person hier ihren Lebensunterhalt?  |
| | [act:enum/interest_type/professional_activity](act:enum/interest_type/professional_activity) |
| governing_body |  Sitz in einem Führungs-, Aufsichts- oder Beratungsgremium einer Organisation, die einem eigenen Zweck nachgeht — Verwaltungsrat, Stiftungsrat, Beirat —, unabhängig von Rechtsform und Entschädigung. Prüffrage: Steuert die Person eine Organisation mit, ohne dort angestellt zu sein?  |
| | [act:enum/interest_type/governing_body](act:enum/interest_type/governing_body) |
| interest_group_mandate |  Dauernde Leitungs- oder Beratungsfunktion für eine Interessengruppe oder einen Verband — also für eine Organisation, deren Zweck die Interessenvertretung selbst ist. Massgebend ist das Gegenüber, nicht die Funktion: Ist der Zweck der Organisation die Vertretung von Interessen, gilt dieser Wert auch dann, wenn die Funktion ein Sitz in einem Führungsgremium ist. Anders als `governing_body` erfasst er zudem dauernde Beratungsmandate ohne Sitz in einem Gremium.  |
| | [act:enum/interest_type/interest_group_mandate](act:enum/interest_type/interest_group_mandate) |
| public_committee |  Mitwirkung in einer Kommission oder einem anderen Gremium der öffentlichen Hand — des Bundes, eines Kantons, einer Gemeinde oder der interkantonalen und interkommunalen Zusammenarbeit, einschliesslich ausserparlamentarischer Kommissionen und der Aufsichtsgremien öffentlich-rechtlicher Anstalten. Der Unterschied zum `political_office` liegt nicht darin, wie der Sitz besetzt wird, sondern worum es sich handelt: nicht um ein eigenes Amt in einer Behörde, sondern um die Mitwirkung in einem ihrer Gremien. Ob die Person dort für ihr eigenes Gemeinwesen sitzt, sagt `is_ex_officio`.  |
| | [act:enum/interest_type/public_committee](act:enum/interest_type/public_committee) |
| political_office |  Eigenes Amt in einer Behörde auf einer anderen föderalen Ebene oder in einer anderen Körperschaft — Gemeindeexekutive oder -parlament, Schulpflege, Kirchgemeinde —, in der Regel durch Wahl besetzt. Das Mandat, für das offengelegt wird, gehört nie hierher.  |
| | [act:enum/interest_type/political_office](act:enum/interest_type/political_office) |
| association |  Blosse Mitgliedschaft in einem Verein, Verband oder einer Interessenorganisation, ohne Leitungsfunktion und ohne Sitz in einem Gremium. Wird eine Funktion ausgeübt, gilt `governing_body` oder `interest_group_mandate`.  |
| | [act:enum/interest_type/association](act:enum/interest_type/association) |
| other |  Interessenbindung, die keiner der übrigen Werte abdeckt. Die publizierte Bezeichnung gehört in `function_role` oder `organization_name`, damit der Eintrag lesbar bleibt.  |
| | [act:enum/interest_type/other](act:enum/interest_type/other) |







</div>