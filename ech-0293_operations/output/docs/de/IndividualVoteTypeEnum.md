## Enum: IndividualVoteTypeEnum 




_Art der Einzelstimme eines Mitglieds._




<div data-search-exclude markdown="1">

URI: [ops:IndividualVoteTypeEnum](https://ch.paf.link/schema/operations/IndividualVoteTypeEnum)

### Zulässige Werte
| Wert | Beschreibung |
|------------------------|----------------------------------------------------------------------------|
| yes |  Ja-Stimme: Das Mitglied stimmt der Vorlage oder dem Antrag zu.  |
| | [ops:enum/individual_vote_type/yes](ops:enum/individual_vote_type/yes) |
| no |  Nein-Stimme: Das Mitglied lehnt die Vorlage oder den Antrag ab.  |
| | [ops:enum/individual_vote_type/no](ops:enum/individual_vote_type/no) |
| abstention |  Enthaltung: Das Mitglied nimmt an der Abstimmung teil, enthält sich aber der Stimme; bei elektronischer Stimmabgabe drückt es den Knopf „Enthaltung“.  |
| | [ops:enum/individual_vote_type/abstention](ops:enum/individual_vote_type/abstention) |
| not_voted |  Nicht gestimmt: Das Mitglied hat keine Stimme abgegeben, etwa weil es anwesend war, aber nicht gestimmt hat, oder abwesend war.  |
| | [ops:enum/individual_vote_type/not_voted](ops:enum/individual_vote_type/not_voted) |
| tie_breaker |  Stichentscheid, den die Präsidentin oder der Präsident bei Stimmengleichheit fällt (siehe voting_type tie_breaker_president).  |
| | [ops:enum/individual_vote_type/tie_breaker](ops:enum/individual_vote_type/tie_breaker) |
| other |  Stimme, die sich nicht auf die Ja/Nein-Achse bringen lässt — etwa bei einer Auswahlabstimmung, bei der das Mitglied gestimmt hat, aber weder Ja noch Nein; welche Option es gewählt hat, hält type_label fest (z.B. „Auswahl A“). Gegenstück zu total_other auf der Abstimmung; so bleibt die Einzelstimme auswertbar, ohne dass jede kantonale Auswahlmechanik einen eigenen Enum-Wert braucht.  |
| | [ops:enum/individual_vote_type/other](ops:enum/individual_vote_type/other) |







</div>