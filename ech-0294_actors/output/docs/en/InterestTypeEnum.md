## Enum: InterestTypeEnum 




_Types of interest links (conflicts of interest, political financing)._




<div data-search-exclude markdown="1">

URI: [act:InterestTypeEnum](https://ld.ech.ch/schema/0294/actors/InterestTypeEnum)

### Permissible Values
| Value | Description |
| --- | --- |
| professional_activity |  Gainful employment outside the political mandate: employment, self-employment, the own operationally run company. Where the person is an employee, employer and function are stated. Test question: is this where the person earns their living?  |
| | [act:enum/interest_type/professional_activity](act:enum/interest_type/professional_activity) |
| governing_body |  Seat in a management, supervisory or advisory body of an organisation that pursues a purpose of its own — board of directors, foundation board, advisory board — irrespective of legal form and remuneration. Test question: does the person help steer an organisation without being employed by it?  |
| | [act:enum/interest_type/governing_body](act:enum/interest_type/governing_body) |
| interest_group_mandate |  Permanent management or advisory function for an interest group or federation — an organisation whose very purpose is to represent interests. Decisive is the counterpart, not the function: where the purpose of the organisation is to represent interests, this value applies even if the function is a seat on a governing body. Unlike `governing_body` it also covers permanent advisory mandates without any seat on a body.  |
| | [act:enum/interest_type/interest_group_mandate](act:enum/interest_type/interest_group_mandate) |
| public_mandate |  Office or seat in the public sector at another federal level or in another public body: a seat in a communal executive or legislature, on a school board or in a parish, and likewise participation in a committee or another body of the Confederation, a canton, a commune or of intercantonal and intercommunal cooperation. Most registers do not distinguish the two cases, which is why the standard keeps them in one value. The mandate for which the disclosure is made is never stated here; whether the person holds the mandate as a delegate of their own public body is stated by `is_ex_officio`.  |
| | [act:enum/interest_type/public_mandate](act:enum/interest_type/public_mandate) |
| association |  Plain membership in an association, federation or interest organisation, without a management function and without a seat on a body. Where a function is held, `governing_body` or `interest_group_mandate` applies.  |
| | [act:enum/interest_type/association](act:enum/interest_type/association) |
| other |  Interest link that none of the other values covers. The published designation belongs in `function_role` or `organization_name`, so that the entry remains readable.  |
| | [act:enum/interest_type/other](act:enum/interest_type/other) |







</div>