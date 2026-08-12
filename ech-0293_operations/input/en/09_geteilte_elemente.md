\newpage

# Shared elements

## Reference classes

`PersonReference` and `GroupReference` name a person or a group without describing them here: what a person or a body is, is defined by eCH-0294; council operations merely point to it. Besides the pointer, the reference retains the key characteristics **at the time of linking** — for a speech, for instance, the parliamentary group the speaker belonged to back then.

This serves three purposes:

- **Useful local data** without costly queries of the complete entity
- **No redundancy**, since not all information has to be repeated at every mention
- **Implicit versioning**, as the reference stays unchanged even if the linked person or group changes later

Unlike an entity, a reference is not identified in its own right — it merely names an identified entity. That is why `global_uri` is not mandatory here: all that is required is that at least one of `local_id` or `global_uri` is set. A system that only knows the local id of the referenced entity states that; it is resolved within the same delivery. Beyond the delivery, the `global_uri` does the pointing.

{{include:ech-0293_operations/output/docs/PersonReference.md}}

{{include:ech-0293_operations/output/docs/GroupReference.md}}

## Multilingual texts

In Switzerland, designations, titles and descriptions often exist in several languages. Rather than keeping a separate field per language, a slot of type `MultilingualString` takes a list of entries with `text` and `language`. Those who keep only one language deliver a single entry — the language is to be stated there as well. Links are modelled the same way: many parliamentary information systems keep a separate address per language, which is why `url` is multilingual too.

{{include:ech-0293_operations/output/docs/MultilingualString.md}}

## Mixin classes

Three classes carry no data of their own; they bundle slots that look the same across many classes — the identification of an entity, its creation and modification dates, and the temporal course of an event with planned and actual start and end. They come from the specialist group's common schema (eCH-0292) and are imported by its standards so that the same information is named alike and behaves alike everywhere.

A mixin is not a superclass: no instance of a mixin class is ever created, and nothing of it shows in the data. The attribute tables of the classes therefore list the inherited slots individually and note their origin under "Inheritance" — the three sections below explain what stands behind that note.

{{include:ech-0293_operations/output/docs/HasIdentification.md}}

{{include:ech-0293_operations/output/docs/HasCreationModificationDates.md}}

{{include:ech-0293_operations/output/docs/IsEventWithDuration.md}}
