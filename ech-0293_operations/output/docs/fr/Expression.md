

## Classe: Expression 


_FRBR Expression : une version linguistique concrète d'un Work._




<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
|------------------------|----------------------|------------------------------------------------------|
| id | 1 <br/> [String](String.md) | Identifiant univoque de l'élément.  |
| dates | * <br/> [Date](Date.md) | Dates relatives à l'élément, chacune assortie d'une indication de type.  |
| expression_language | 1 <br/> [String](String.md) | Code de langue au format ISO 639-1.  |
| expression_title | 1 <br/> [String](String.md) | Titre de la version linguistique.  |
| expression_description | 0..1 <br/> [String](String.md) | Texte descriptif de la version linguistique.  |
| manifestations | * <br/> [Manifestation](Manifestation.md) | Les formes de fichier (Manifestations) d'une Expression.  |





### Utilisations

| Utilisé par | Dans le slot | Rôle | Élément |
| ---  | --- | --- | --- |
| [Work](Work.md) | [expressions](expressions.md) | range | [Expression](Expression.md) |



















</div>