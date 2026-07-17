

## Classe: IsProcessStep 


_Une classe mixin pour une étape unique dans un processus_

_à plusieurs étapes (par ex. une étape de délibération d'une affaire ou_

_une étape de phase d'une consultation). Combine les slots d'identification_

_et de durée d'événement et ajoute un slot de remarque en texte libre._

_Les classes d'étape concrètes ajoutent leurs propres slots spécifiques au type._

__



<div data-search-exclude markdown="1">




### Attributs

| Nom | Cardinalité et plage | Description |
| ---  | --- | --- |
| local_id | 0..1 <br/> [String](String.md) | Identifiant local. Par exemple, un UUID issu du système d'information du conseil.  |
| global_uri | 1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI unique et globalement valide pour l'entité.  |
| wikidata_uri | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | Une URI qui renvoie à une entité Wikidata, par ex. http://www.wikidata.org/entity/Q39 pour la Suisse.  |
| date_begin_actual | 0..1 <br/> [Date](Date.md) | La date de début effective d'un événement ou d'une occurrence avec durée.  |
| datetime_begin_actual | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de début effectives d'un événement ou d'une occurrence avec durée.  |
| date_begin_planned | 0..1 <br/> [Date](Date.md) | La date de début planifiée d'un événement ou d'une occurrence avec durée.  |
| datetime_begin_planned | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de début planifiées d'un événement ou d'une occurrence avec durée.  |
| date_end_actual | 0..1 <br/> [Date](Date.md) | La date de fin effective d'un événement ou d'une occurrence avec durée.  |
| datetime_end_actual | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de fin effectives d'un événement ou d'une occurrence avec durée.  |
| date_end_planned | 0..1 <br/> [Date](Date.md) | La date de fin planifiée d'un événement ou d'une occurrence avec durée.  |
| datetime_end_planned | 0..1 <br/> [Datetime](Datetime.md) | La date et l'heure de fin planifiées d'un événement ou d'une occurrence avec durée.  |
| remark | 0..1 <br/> [String](String.md) | Remarque ou note en texte libre pour les cas particuliers ou pour un contexte supplémentaire relatif à une étape de processus ou à une entité.  |



### Utilisation de mixin

| mixed into | description |
| --- | --- |





















</div>