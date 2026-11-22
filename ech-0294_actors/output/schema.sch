<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron">
  <sch:title>Schematron rules for LinkML schema: actors-schema</sch:title>
  <sch:ns prefix="ns" uri="https://ld.ech.ch/schema/0294/actors/"/>
  <sch:pattern>
    <sch:rule context="ns:PersonReference | ns:person_reference">
      <sch:assert test="(((ns:local_id)) or ((ns:global_uri)))">PersonReference: any_of: local_id | global_uri</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:rule context="ns:GroupReference | ns:parent_groups | ns:group_reference">
      <sch:assert test="(((ns:local_id)) or ((ns:global_uri)))">GroupReference: any_of: local_id | global_uri</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:rule context="ns:InterestLink | ns:interest_links">
      <sch:assert test="(((ns:organization_uid)) or ((ns:organization_name)))">InterestLink: any_of: organization_uid | organization_name</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:rule context="ns:Address | ns:addresses">
      <sch:assert test="(((ns:postal_locality)) or ((ns:address_uri)))">Address: any_of: postal_locality | address_uri</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:rule context="ns:Occupation | ns:occupations">
      <sch:assert test="(((ns:occupation_code)) or ((ns:label)))">Occupation: any_of: occupation_code | label</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:rule context="ns:Training | ns:trainings">
      <sch:assert test="(((ns:training_type)) or ((ns:training_code)) or ((ns:value)))">Training: any_of: training_type | training_code | value</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:rule context="ns:RoleType | ns:role_type">
      <sch:assert test="not((ns:role_type_enum = 'other')) or ((ns:role_label))">If the role type is 'other', a descriptive label must be provided.</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:rule context="ns:RoleType | ns:role_type">
      <sch:assert test="(((ns:role_type_enum)) or ((ns:role_label)))">RoleType: any_of: role_type_enum | role_label</sch:assert>
    </sch:rule>
  </sch:pattern>
</sch:schema>
