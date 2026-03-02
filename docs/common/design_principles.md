# Design Principles and LinkML Guidelines

## Data Exchange Focus

The eCH Specialist Group Political Affairs focuses on **data exchange** between different systems. Therefore, the data schema is designed to facilitate interoperability and data sharing. It is not intended to model the internal workings of any specific system.

## Identifiers and URIs

There is always the possibility to identify an entity with either an internal/local identifier (`ID`) or a global `URI`. The design principle is to always have both, so that data can be linked globally but also work in isolated systems.

## Normalization

The data schema follows a pragmatic approach to normalization. The basic principle is to avoid redundancy where possible. The main reason for not fully normalizing the data schema is that there is no single authority for many entities in the political domain. Therefore, some redundancy is accepted to allow for easier data integration and historical tracking.

## Versioning

There is no general versioning of entities in the data schema. The main reason for this is that versioning can lead to significant complexity in data management and querying. However, versioning can be implemented for specific entities where it makes sense and is required by the use case. In such a case, the versioning mechanism is part of the data model for that specific entity.

An example of this would be the occupation of a person. Each occupation can have a start and end date, allowing to track changes over time without versioning the person entity itself.

## Local References

Some entities are referenced "locally" in addition to linking to the full entity. This is done to have useful local data without too much query complexity. This will also generate some form of Versioning implicitly, as the local reference will not change when the full entity changes.

An example of this would be that a motion links to the person who submitted it. In addition to the link to the full person entity, the information of e.g. the political party at the time of the submission or the role of the person is stored "locally" in the motion entity. This way, even if the person changes party and/or role later on, the motion still contains the correct information at the time of submission.

### Example of Local Reference

The following example shows a motion with a local reference to the submitter (person) and the actual person entity. The motion contains the correct information about the submitter at the time of submission, even if the person changes party and/or role later on.

In this case, the information about the person only shows the current data (no versioning at all).

This is a simplified example, in a real use case there would be more information about the motion and the person.

```yaml
motion:
  id: ex:m1
  title: "Motion 1"
  submitter: # local reference to person, class PersonReference
    id: ex:p1
    name: "John Doe"
    party: "Party A"
    role: "Member of Parliament"
```

```yaml
person:
  id: ex:p1
  name: "John Doe"
  party: "Party B"
  role: "Minister"
```