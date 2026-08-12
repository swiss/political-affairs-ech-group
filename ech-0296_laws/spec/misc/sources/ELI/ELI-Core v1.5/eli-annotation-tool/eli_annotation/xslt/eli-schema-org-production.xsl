<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE xsl:stylesheet
 [
  <!ENTITY rdf "http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <!ENTITY eli "http://data.europa.eu/eli/ontology#">
 ]
>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0"
                xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                xmlns:eli="http://data.europa.eu/eli/ontology#"
                exclude-result-prefixes="rdf eli">


  <!-- Template called by the template-generation.xsl stylesheet to generate
       the Schema.Org content that will be inserted in the Web page.

       This template transforms all the <rdf:Description> elements in the
       file into into <meta> tags that will be inserted in the HTML
       header. -->
  <xsl:template name="insert.schema-org.content">
    <xsl:param name="langCode"/>

    <script type="application/ld+json">
      <xsl:call-template name="writeJsonSequence">
        <xsl:with-param name="strContent">

          <!-- Calls the correct template depending on the ELI type of the
               current resource (e.g. LegalExpression, Format). -->
          <xsl:choose>
            <xsl:when test="rdf:type/@rdf:resource = '&eli;LegalResource'">
              <xsl:apply-templates select="." mode="resourceConv"/>
            </xsl:when>
            <xsl:when test="rdf:type/@rdf:resource = '&eli;LegalExpression'">
              <xsl:apply-templates select="." mode="expressionConv"/>
            </xsl:when>
            <xsl:when test="rdf:type/@rdf:resource = '&eli;Format'">
              <xsl:apply-templates select="." mode="formatConv"/>
            </xsl:when>
          </xsl:choose>

        </xsl:with-param>
      </xsl:call-template>
    </script>

  </xsl:template>


  <!-- Template buiding a ``CreativeWork`` entity from an ELI LegalResource.
       The mode parameter indicates how the entity must be built: as a main
       entity corresponding to the document described in the page or a
       sub-entity that appears into one of the properties of another main
       entity. In such a case, it can be a parent sub-entity or a child
       sub-entity. -->
  <xsl:template match="rdf:Description" mode="resourceConv">
    <xsl:param name="mode" select="'main'"/>

    <xsl:text>{</xsl:text>
    <xsl:call-template name="writeJsonSequence">
      <xsl:with-param name="strContent">
        <!-- If the LegalResource is not inserted as a sub-entity, adds the
             @context property -->
        <xsl:if test="$mode ='main'">
          <xsl:text> "@context": "http://schema.org/",</xsl:text>
        </xsl:if>

        <!-- Inserts the type and the identifier of the entity -->
        <xsl:text> "@type": "CreativeWork", "@id": "</xsl:text>
        <xsl:value-of select="@rdf:about"/>
        <xsl:text>",</xsl:text>

        <!-- If the LegalResource is not inserted as a parent sub-entity -->
        <xsl:if test="$mode !='parent'">
          <!-- Inserts descriptive properties of the LegalResource -->
          <xsl:call-template name="insertResourceDescProps">
            <xsl:with-param name="inputDesc" select="."/>
          </xsl:call-template>
        </xsl:if>

        <!-- If the LegalResource is not inserted as a child sub-entity,
             inserts a link towards the parent abstract LegalResource -->
        <xsl:if test="$mode != 'child'">
          <xsl:call-template name="buildProp">
            <xsl:with-param name="name"
                            select="'exampleOfWork'"/>
            <xsl:with-param name="values"
                            select="eli:is_member_of/@rdf:resource"/>
          </xsl:call-template>
        </xsl:if>

        <!-- If the LegalResource is not inserted as a parent sub-entity -->
        <xsl:if test="$mode != 'parent'">
          <xsl:variable name="childExpressions"
                        select="key('rdfDescInverse', @rdf:about)[
                              eli:realizes/@rdf:resource = current()/@rdf:about
                                ]"/>
          <!-- Inserts the child ELI LegalExpression as sub-entities in the
               ``workExample`` property -->
          <xsl:if test="count($childExpressions) > 0">
            <xsl:text> "workExample": </xsl:text>

            <xsl:if test="count($childExpressions) > 1">
              <xsl:text>[ </xsl:text>
            </xsl:if>

            <xsl:call-template name="writeJsonSequence">
              <xsl:with-param name="strContent">

                <xsl:apply-templates select="$childExpressions"
                                     mode="expressionConv">
                  <xsl:with-param name="mode" select="'child'"/>
                </xsl:apply-templates>

              </xsl:with-param>
            </xsl:call-template>

            <xsl:if test="count($childExpressions) > 1">
              <xsl:text>]</xsl:text>
            </xsl:if>
            <xsl:text>,</xsl:text>

          </xsl:if>
        </xsl:if>
      </xsl:with-param>
    </xsl:call-template>
    <xsl:text>},</xsl:text>
  </xsl:template>


  <!-- Template buiding a ``CreativeWork`` entity from an ELI LegalExpression.
       The mode parameter indicates how the entity must be built: as a main
       entity corresponding to the document described in the page or a
       sub-entity that appears into one of the properties of another main
       entity. In such a case, it can be a parent sub-entity or a child
       sub-entity. -->
  <xsl:template match="rdf:Description" mode="expressionConv">
    <xsl:param name="mode" select="'main'"/>

    <xsl:text>{</xsl:text>
    <xsl:call-template name="writeJsonSequence">
      <xsl:with-param name="strContent">
        <!-- If the LegalExpression is not inserted as a sub-entity, adds the
             @context property -->
        <xsl:if test="$mode ='main'">
          <xsl:text> "@context": "http://schema.org/",</xsl:text>
        </xsl:if>

        <!-- Inserts the type and the identifier of the entity -->
        <xsl:text> "@type": "CreativeWork", "@id": "</xsl:text>
        <xsl:value-of select="@rdf:about"/>
        <xsl:text>",</xsl:text>

        <!-- If the LegalExpression is not inserted as a sub-entity -->
        <xsl:if test="$mode ='main'">
          <xsl:variable name="parentResources"
                        select="key('rdfDesc', eli:realizes/@rdf:resource)"/>
          <!-- Inserts descriptive properties inherited from the parent
               LegalResource -->
          <xsl:call-template name="insertResourceDescProps">
            <xsl:with-param name="inputDesc" select="$parentResources[1]"/>
          </xsl:call-template>
        </xsl:if>

        <!-- If the LegalExpression is not inserted as a parent sub-entity -->
        <xsl:if test="$mode !='parent'">
          <!-- Inserts descriptive properties of the LegalExpression -->
          <xsl:call-template name="insertExpressionDescProps">
            <xsl:with-param name="inputDesc" select="."/>
          </xsl:call-template>
        </xsl:if>

        <!-- If the LegalExpression is not inserted as a child sub-entity -->
        <xsl:if test="$mode != 'child'">
          <xsl:variable name="parentResources"
                        select="key('rdfDesc', eli:realizes/@rdf:resource)"/>
          <!-- Inserts the parent ELI LegalResource as sub-entities in the
               ``exampleOfWork`` property -->
          <xsl:if test="count($parentResources) > 0">
            <xsl:text> "exampleOfWork": </xsl:text>

            <xsl:if test="count($parentResources) > 1">
              <xsl:text>[ </xsl:text>
            </xsl:if>

            <xsl:call-template name="writeJsonSequence">
              <xsl:with-param name="strContent">

                <xsl:apply-templates select="$parentResources"
                                     mode="resourceConv">
                  <xsl:with-param name="mode" select="'parent'"/>
                </xsl:apply-templates>

              </xsl:with-param>
            </xsl:call-template>

            <xsl:if test="count($parentResources) > 1">
              <xsl:text>]</xsl:text>
            </xsl:if>
            <xsl:text>,</xsl:text>

          </xsl:if>
        </xsl:if>

        <!-- If the LegalExpression is not inserted as a parent sub-entity -->
        <xsl:if test="$mode != 'parent'">
          <xsl:variable name="childFormats"
                        select="key('rdfDescInverse', @rdf:about)[
                              eli:embodies/@rdf:resource = current()/@rdf:about
                                ]"/>
          <!-- Inserts the child ELI Format as sub-entities in the
               ``encoding`` property -->
          <xsl:if test="count($childFormats) > 0">
            <xsl:text> "encoding": </xsl:text>

            <xsl:if test="count($childFormats) > 1">
              <xsl:text>[ </xsl:text>
            </xsl:if>

            <xsl:call-template name="writeJsonSequence">
              <xsl:with-param name="strContent">

                <xsl:apply-templates select="$childFormats"
                                     mode="formatConv">
                  <xsl:with-param name="mode" select="'child'"/>
                </xsl:apply-templates>

              </xsl:with-param>
            </xsl:call-template>

            <xsl:if test="count($childFormats) > 1">
              <xsl:text>]</xsl:text>
            </xsl:if>
            <xsl:text>,</xsl:text>

          </xsl:if>
        </xsl:if>
      </xsl:with-param>
    </xsl:call-template>
    <xsl:text>},</xsl:text>
  </xsl:template>


  <!-- Template buiding a ``MediaObject`` entity from an ELI Format
       The mode parameter indicates how the entity must be built: as a main
       entity corresponding to the document described in the page or a
       sub-entity that appears into one of the properties of another main
       entity. In such a case, it can be a parent sub-entity or a child
       sub-entity. -->
  <xsl:template match="rdf:Description" mode="formatConv">
    <xsl:param name="mode" select="'main'"/>

    <xsl:text>{</xsl:text>
    <xsl:call-template name="writeJsonSequence">
      <xsl:with-param name="strContent">
        <!-- If the Format is not inserted as a sub-entity, adds the
             @context property -->
        <xsl:if test="$mode ='main'">
          <xsl:text> "@context": "http://schema.org/",</xsl:text>
        </xsl:if>

        <!-- Inserts the type and the identifier of the entity -->
        <xsl:text> "@type": "MediaObject", "@id": "</xsl:text>
        <xsl:value-of select="@rdf:about"/>
        <xsl:text>",</xsl:text>

        <!-- If the Format is not inserted as a sub-entity -->
        <xsl:if test="$mode ='main'">
          <xsl:variable name="parentExpressions"
                        select="key('rdfDesc', eli:embodies/@rdf:resource)"/>
          <xsl:variable name="parentResources"
                        select="key('rdfDesc',
                                    $parentExpressions/eli:realizes
                                      /@rdf:resource)"/>
          <!-- Inserts descriptive properties inherited from the parent
               LegalExpresionn and the grand-parent LegalResource -->
          <xsl:call-template name="insertResourceDescProps">
            <xsl:with-param name="inputDesc"
                            select="$parentResources[1]"/>
          </xsl:call-template>
          <xsl:call-template name="insertExpressionDescProps">
            <xsl:with-param name="inputDesc"
                            select="$parentExpressions[1]"/>
          </xsl:call-template>
        </xsl:if>

        <!-- If the Format is not inserted as a parent sub-entity -->
        <xsl:if test="$mode !='parent'">
          <!-- Inserts descriptive properties of the Format -->
          <xsl:call-template name="insertFormatDescProps">
            <xsl:with-param name="inputDesc" select="."/>
          </xsl:call-template>
        </xsl:if>

        <!-- If the Format is not inserted as a child sub-entity -->
        <xsl:if test="$mode != 'child'">
          <xsl:variable name="parentExpressions"
                        select="key('rdfDesc', eli:embodies/@rdf:resource)"/>
          <!-- Inserts the parent ELI LegalExpression as sub-entities in the
               ``encodesCreativeWork`` property -->
          <xsl:if test="count($parentExpressions) > 0">
            <xsl:text> "encodesCreativeWork": </xsl:text>

            <xsl:if test="count($parentExpressions) > 1">
              <xsl:text>[ </xsl:text>
            </xsl:if>

            <xsl:call-template name="writeJsonSequence">
              <xsl:with-param name="strContent">

                <xsl:apply-templates select="$parentExpressions"
                                     mode="expressionConv">
                  <xsl:with-param name="mode" select="'parent'"/>
                </xsl:apply-templates>

              </xsl:with-param>
            </xsl:call-template>

            <xsl:if test="count($parentExpressions) > 1">
              <xsl:text>]</xsl:text>
            </xsl:if>
            <xsl:text>,</xsl:text>

          </xsl:if>
        </xsl:if>
      </xsl:with-param>
    </xsl:call-template>
    <xsl:text>},</xsl:text>
  </xsl:template>


  <!-- Template building various Schema.Org properties,that will be inserted
       into a Schema.Org entity, from an ELI LegalResource.
       This properties can be inserted into the Schema.Org entity built for
       the ELI LegalResource or into the Schema.Org entity corresponding to
       one of its ELI children. The idea is to have a maximum of properties
       describing the main entity of the page. -->
  <xsl:template name="insertResourceDescProps">
    <xsl:param name="inputDesc"/>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'additionalType'"/>
      <xsl:with-param name="values"
                      select="$inputDesc/eli:type_document/@rdf:resource"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'identifier'"/>
      <xsl:with-param name="values"
                      select="$inputDesc/eli:number | $inputDesc/eli:id_local"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'version'"/>
      <xsl:with-param name="values"
                      select="$inputDesc/eli:version/@rdf:resource"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'datePublished'"/>
      <xsl:with-param name="values"
                      select="$inputDesc/eli:date_publication"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'about'"/>
      <xsl:with-param name="values"
                      select="$inputDesc/eli:is_about"/>
      <xsl:with-param name="targetType"
                      select="'Thing'"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'spatialCoverage'"/>
      <xsl:with-param name="values"
                      select="$inputDesc/eli:relevant_for"/>
      <xsl:with-param name="targetType"
                      select="'Place'"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'locationCreated'"/>
      <xsl:with-param name="values"
                      select="$inputDesc/eli:juridiction"/>
      <xsl:with-param name="targetType"
                      select="'Place'"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'sourceOrganization'"/>
      <xsl:with-param name="values"
                      select="$inputDesc/eli:passed_by"/>
      <xsl:with-param name="targetType"
                      select="'Organization'"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'accountablePerson'"/>
      <xsl:with-param name="values"
                      select="  $inputDesc/eli:responsability_of
                              | $inputDesc/eli:responsability_of_agent"/>
      <xsl:with-param name="targetType"
                      select="'Organization'"/>
      <xsl:with-param name="targetProp"
                      select="'name'"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'isBasedOn'"/>
      <xsl:with-param name="values"
                      select="  $inputDesc/eli:based_on | $inputDesc/eli:applies
                              | $inputDesc/eli:transposes"/>
      <xsl:with-param name="targetType"
                      select="'CreativeWork'"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'mentions'"/>
      <xsl:with-param name="values"
                      select="$inputDesc/eli:related_to"/>
      <xsl:with-param name="targetType"
                      select="'Thing'"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'cites'"/>
      <xsl:with-param name="values"
                      select="$inputDesc/eli:cites"/>
      <xsl:with-param name="targetType"
                      select="'Thing'"/>
    </xsl:call-template>
  </xsl:template>


  <!-- Template building various Schema.Org properties,that will be inserted
       into a Schema.Org entity, from an ELI LegalExpression.
       This properties can be inserted into the Schema.Org entity built for
       the ELI LegalExpression or into the Schema.Org entity corresponding to
       one of its ELI children. The idea is to have a maximum of properties
       describing the main entity of the page. -->
  <xsl:template name="insertExpressionDescProps">
    <xsl:param name="inputDesc"/>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'inLanguage'"/>
      <xsl:with-param name="values"
                      select="$inputDesc/eli:language"/>
      <xsl:with-param name="targetType"
                      select="'Language'"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'name'"/>
      <xsl:with-param name="values"
                      select="$inputDesc/eli:title"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'alternateName'"/>
      <xsl:with-param name="values"
                      select="  $inputDesc/eli:title_short
                              | $inputDesc/eli:title_alternative"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'description'"/>
      <xsl:with-param name="values"
                      select="$inputDesc/eli:description"/>
    </xsl:call-template>
  </xsl:template>


  <!-- Template building various Schema.Org properties,that will be inserted
       into a Schema.Org entity, from an ELI Format.
       This properties can be inserted into the Schema.Org entity built for
       the ELI Format or into the Schema.Org entity corresponding to
       one of its ELI children. The idea is to have a maximum of properties
       describing the main entity of the page. -->
  <xsl:template name="insertFormatDescProps">
    <xsl:param name="inputDesc"/>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'fileFormat'"/>
      <xsl:with-param name="values"
                      select="$inputDesc/eli:format/@rdf:resource"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'contentUrl'"/>
      <xsl:with-param name="values"
                      select="$inputDesc/eli:is_exemplified_by/@rdf:resource"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'isPartOf'"/>
      <xsl:with-param name="values"
                      select="  $inputDesc/eli:published_in
                              | $inputDesc/eli:published_in_format"/>
      <xsl:with-param name="targetType"
                      select="'PublicationIssue'"/>
      <xsl:with-param name="targetProp"
                      select="'name'"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'publisher'"/>
      <xsl:with-param name="values"
                      select="  $inputDesc/eli:publisher
                              | $inputDesc/eli:publisher_agent"/>
      <xsl:with-param name="targetType"
                      select="'Organization'"/>
      <xsl:with-param name="targetProp"
                      select="'name'"/>
    </xsl:call-template>

    <xsl:call-template name="buildProp">
      <xsl:with-param name="name"
                      select="'copyrightHolder'"/>
      <xsl:with-param name="values"
                      select="  $inputDesc/eli:rightsholder
                              | $inputDesc/eli:rightsholder_agent"/>
      <xsl:with-param name="targetType"
                      select="'Organization'"/>
      <xsl:with-param name="targetProp"
                      select="'name'"/>
    </xsl:call-template>
  </xsl:template>


  <!-- Template building a Schema.Org property that will be inserted into
       a Schema.Org entity.
  -->
  <xsl:template name="buildProp">
    <xsl:param name="name" select="''"/>
    <xsl:param name="values"/>
    <xsl:param name="targetType" select="''"/>
    <xsl:param name="targetProp" select="''"/>

    <xsl:if test="count($values) > 0">
      <!-- Writes the property name -->
      <xsl:text> "</xsl:text>
      <xsl:value-of select="$name"/>
      <xsl:text>":</xsl:text>
      <!-- Inserts an array if there are multiple values -->
      <xsl:if test="count($values) > 1">
        <xsl:text> [</xsl:text>
      </xsl:if>

      <xsl:call-template name="writeJsonSequence">
        <xsl:with-param name="strContent">

          <xsl:for-each select="$values">
            <xsl:choose>
              <!-- If there is no target type, just outputs the string value -->
              <xsl:when test="$targetType=''">
                <xsl:text> "</xsl:text>
                <xsl:call-template name="escapeJsonString">
                  <xsl:with-param name="strContent" select="string(.)"/>
                </xsl:call-template>
                <xsl:text>"</xsl:text>
              </xsl:when>
              <!-- If there is a target type and the current value has an URI,
                   builds a Schema.Org entity of the specified type and inserts
                   the URI as its id -->
              <xsl:when test="@rdf:resource">
                <xsl:text> { "@type": "</xsl:text>
                <xsl:value-of select="$targetType"/>
                <xsl:text>", "@id": "</xsl:text>
                <xsl:value-of select="@rdf:resource"/>
                <xsl:text>"}</xsl:text>
              </xsl:when>
              <!-- If there is a target type, a target property and the current
                   value doesn't have an URI, builds a Schema.Org entity of the
                   specified type and inserts the text from the current value
                   into the target property -->
              <xsl:when test="$targetProp != ''">
                <xsl:text> { "@type": "</xsl:text>
                <xsl:value-of select="$targetType"/>
                <xsl:text>", "</xsl:text>
                <xsl:value-of select="$targetProp"/>
                <xsl:text>": "</xsl:text>
                <xsl:call-template name="escapeJsonString">
                  <xsl:with-param name="strContent" select="string(.)"/>
                </xsl:call-template>
                <xsl:text>"}</xsl:text>
              </xsl:when>
            </xsl:choose>
            <xsl:text>,</xsl:text>
          </xsl:for-each>

        </xsl:with-param>
      </xsl:call-template>

      <!-- Closes the array if there were multiple values -->
      <xsl:if test="count($values) > 1">
        <xsl:text>]</xsl:text>
      </xsl:if>
      <xsl:text>,</xsl:text>
    </xsl:if>
  </xsl:template>


  <!-- Template writing in JSON a sequence of coma-separated elements.
       The last element mustn't be followed by a coma.
  -->
  <xsl:template name="writeJsonSequence">
    <xsl:param name="strContent" select="''"/>

    <xsl:choose>
      <xsl:when test="$strContent = ''"/>
      <xsl:when test="substring($strContent,string-length($strContent),
                                string-length($strContent)+1) = ','">
        <xsl:value-of select="substring($strContent, 1,
                                        string-length($strContent)-1)"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$strContent"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>


  <!-- Template escaping a string in order to write it in JSON. Basically,
       the quotes (") are replaced with antislash-quotes (\")
  -->
  <xsl:template name="escapeJsonString">
    <xsl:param name="strContent" select="''"/>

    <xsl:choose>

      <xsl:when test="not(contains($strContent, '&quot;'))">
        <xsl:value-of select="$strContent"/>
      </xsl:when>

      <xsl:otherwise>
        <xsl:value-of select="substring-before($strContent, '&quot;')"/>
        <xsl:text>\"</xsl:text>

        <xsl:call-template name="escapeJsonString">
          <xsl:with-param name="strContent"
                          select="substring-after($strContent, '&quot;')"/>
        </xsl:call-template>
      </xsl:otherwise>

    </xsl:choose>
  </xsl:template>

</xsl:stylesheet>
