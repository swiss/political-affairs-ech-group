\newpage

# Shared Elements

## Reference Classes

`PersonReference` and `GroupReference` are used to reference persons or groups **locally** within another entity. In addition to the actual link to the complete entity, only the relevant information at the **time of linking** is stored – so it is not necessary to repeat all the information about a person or group at every mention.

An example: A motion references the person who submitted it. In addition to the link to the complete person entity, the motion stores locally information such as the person's political party or role **at the time of submission**. If the person later changes party or role, the information in the motion nevertheless remains correct and immutable.

This serves three purposes:

- **Useful local data** without costly queries of the complete entity
- **No redundancy**, since not all information has to be repeated at every mention
- **Implicit versioning**, since the local reference remains unchanged even if the linked entity changes later

Unlike an entity, a reference is not identified in its own right – it merely names an identified entity. The `global_uri` is therefore not mandatory here: all that is required is that at least one of `local_id` or `global_uri` is set. A system that only knows the local id of the referenced entity states that id; it is resolved within the same delivery. Beyond the delivery, the `global_uri` provides the link.

{{include:ech-0294_actors/output/docs/PersonReference.md}}

{{include:ech-0294_actors/output/docs/GroupReference.md}}

## Reused Classes

An address is written in `street_address`, `postal_code`, `postal_locality` and `country` and may point into swisstopo's official building address register via `address_uri`. The final number of that URI is the EGAID, the federal building address identifier; `https://geo.ld.admin.ch/location/address/101009806` thus denotes "Rue de Genève 17, 1003 Lausanne" as an officially registered building address.

`address_uri` is optional. The written address on its own is permissible, but the reference via the EGAID is preferable: it is an unambiguous identifier and stable over time, whereas street names change, municipalities merge and postal codes are recut. Not every address can be found in the register, a foreign one for instance; the slot therefore remains optional.

To arrive at the EGAID, one can use the [search API of geo.admin.ch](https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=Rue+de+Gen%C3%A8ve+17+1003+Lausanne&type=locations&origins=address) or match against the [official directory of building addresses](https://www.swisstopo.admin.ch/en/official-directory-of-building-addresses). The result is recorded in `address_uri`.

{{include:ech-0294_actors/output/docs/Address.md}}

{{include:ech-0294_actors/output/docs/AddressTypeEnum.md}}

{{include:ech-0294_actors/output/docs/Contact.md}}
