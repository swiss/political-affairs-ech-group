

## Class: TotalOther 


_Vote count for one option of a multiple-choice voting. If several proposals pointing in the same direction are put to the vote at the same time, the members vote on more than two variants and the variant with most votes prevails (in Zurich colloquially a „Cup-Abstimmung“, cast via several voting buttons). Such a voting is represented with voting_type other and a descriptive type_label; total_count_yes, total_count_no and total_count_abstention remain empty, and each option receives an entry with count and label. Example: Gemeinderat of the City of Zurich, sitting of 28 February 2024, affair 2023/361, four options with 75, 25, 12 and 0 votes._




<div data-search-exclude markdown="1">




### Attribute

| Name | Cardinality and Range | Description |
|------------------------|----------------------|------------------------------------------------------|
| count | 0..1 <br/> [Integer](Integer.md) | The count of votes for the total other category.  |
| label | 0..1 <br/> [String](String.md) | Assign a label to a structured piece of information (e.g., display name, position, etc.).  |





### Usages

| Used by | In slot | Role | Element |
| ---  | --- | --- | --- |
| [Voting](Voting.md) | [total_other](total_other.md) | range | [TotalOther](TotalOther.md) |



















</div>