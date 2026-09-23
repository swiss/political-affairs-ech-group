

## Klasse: TotalOther 


_Stimmenzahl für eine Option einer Auswahlabstimmung. Liegen zu derselben Sachfrage mehrere gleichgerichtete Anträge vor, stimmen die Mitglieder über mehr als zwei Varianten gleichzeitig ab, und es obsiegt die Variante mit den meisten Stimmen (in Zürich umgangssprachlich „Cup-Abstimmung“, technisch über mehrere Abstimmungsknöpfe). Eine solche Abstimmung wird mit voting_type other und einem sprechenden type_label abgebildet; total_count_yes, total_count_no und total_count_abstention bleiben leer, und jede Option erhält einen Eintrag mit count und label. Beispiel: Gemeinderat der Stadt Zürich, Sitzung vom 28. Februar 2024, Geschäft 2023/361, vier Optionen mit 75, 25, 12 und 0 Stimmen._




<div data-search-exclude markdown="1">




### Attribute

| Name | Kardinalität und Wertebereich | Beschreibung |
|------------------------|----------------------|------------------------------------------------------|
| count | 0..1 <br/> [Integer](Integer.md) | Die Anzahl der Stimmen für die Kategorie „Andere“.  |
| label | 0..1 <br/> [String](String.md) | Möglichkeit bei einer strukturierten Information, ein Label zu vergeben (bspw. Anzeigename, Anstellung, etc.).  |





### Verwendungen

| Verwendet von | Im Slot | Rolle | Element |
| ---  | --- | --- | --- |
| [Voting](Voting.md) | [total_other](total_other.md) | range | [TotalOther](TotalOther.md) |



















</div>