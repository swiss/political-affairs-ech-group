

## Classe: TotalOther 


_Nombre de voix pour une option d'un vote à choix multiple. Lorsque plusieurs propositions de même sens portent sur la même question, les membres votent simultanément sur plus de deux variantes, et la variante qui obtient le plus de voix l'emporte (à Zurich, familièrement « Cup-Abstimmung », au moyen de plusieurs boutons de vote). Un tel vote est représenté avec voting_type other et un type_label explicite ; total_count_yes, total_count_no et total_count_abstention restent vides, et chaque option reçoit une entrée avec count et label. Exemple : Gemeinderat de la Ville de Zurich, séance du 28 février 2024, affaire 2023/361, quatre options avec 75, 25, 12 et 0 voix._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| count | 0..1 <br/> [Integer](Integer.md) | Le nombre de voix pour la catégorie « autres ».  |
| label | 0..1 <br/> [String](String.md) | Attribuer un label à une information structurée (par ex. nom d'affichage, poste, etc.).  |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Voting](Voting.md) | [total_other](total_other.md) | range | [TotalOther](TotalOther.md) |



















</div>