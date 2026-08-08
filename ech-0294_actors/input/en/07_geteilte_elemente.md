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

An address is recorded twice: as a reference into swisstopo's official building address register (`address_uri`) and as a written address in `street_address`, `postal_code`, `postal_locality` and `country`. The final number of the URI is the EGAID, the federal building address identifier – `https://geo.ld.admin.ch/location/address/101009806` thus denotes "Rue de Genève 17, 1003 Lausanne" as an officially registered building address.

The reference is the more stable statement: street names change, municipalities merge, postal codes are recut, yet the EGAID remains and can be joined with the Register of Buildings and Dwellings as well as with geodata. It does not make the written address redundant, because that often carries more than the register knows – an organisation name, a PO box, a "c/o" line. The example of the Fédération romande des consommateurs shows this plainly: the EGAID denotes the physical address at Rue de Genève 17 in 1003 Lausanne, while the written address states PO box 585 with its own postal code 1001. Both statements are correct, and neither can be derived from the other.

To arrive at the EGAID, one can use the [search API of geo.admin.ch](https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=Rue+de+Gen%C3%A8ve+17+1003+Lausanne&type=locations&origins=address) or match against the [official directory of building addresses](https://www.swisstopo.admin.ch/en/official-directory-of-building-addresses). The result is recorded in `address_uri`.

Not every address can be found in the register, a foreign address for instance. `address_uri` is therefore optional; where it is known, it should be set.

{{include:ech-0294_actors/output/docs/Address.md}}

{{include:ech-0294_actors/output/docs/AddressTypeEnum.md}}

{{include:ech-0294_actors/output/docs/Contact.md}}
