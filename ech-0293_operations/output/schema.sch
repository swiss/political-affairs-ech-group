<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron">
  <sch:title>Schematron rules for LinkML schema: operations</sch:title>
  <sch:ns prefix="ns" uri="https://ch.paf.link/schema/operations/"/>
  <sch:pattern>
    <sch:rule context="ns:PersonReference | ns:person_reference">
      <sch:assert test="(((ns:local_id)) or ((ns:global_uri)))">PersonReference: any_of: local_id | global_uri</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:rule context="ns:GroupReference | ns:group_reference | ns:group_id">
      <sch:assert test="(((ns:local_id)) or ((ns:global_uri)))">GroupReference: any_of: local_id | global_uri</sch:assert>
    </sch:rule>
  </sch:pattern>
</sch:schema>
