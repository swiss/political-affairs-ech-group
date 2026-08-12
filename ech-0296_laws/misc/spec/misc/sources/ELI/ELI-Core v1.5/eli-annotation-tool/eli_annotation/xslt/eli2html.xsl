<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE xsl:stylesheet
 [
  <!ENTITY rdf "http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <!ENTITY eli "http://data.europa.eu/eli/ontology#">
  <!ENTITY elix "urn:eli-annotation-tool:eli:ontology-extension:">
  <!ENTITY skos "http://www.w3.org/2004/02/skos/core#">
  <!ENTITY prov "http://www.w3.org/ns/prov#">
 ]>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0"
                xmlns:elit="urn:eli:annotation-tool:template:"
                xmlns:eli="http://data.europa.eu/eli/ontology#"
                xmlns:elix="urn:eli-annotation-tool:eli:ontology-extension:"
                xmlns:prov="http://www.w3.org/ns/prov#"
                xmlns:elid="urn:eli:annotation-tool:data:"
                xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                xmlns:skos="http://www.w3.org/2004/02/skos/core#"
                exclude-result-prefixes="eli elix elit elid rdf skos prov">

  <xsl:import href="template-generation.xsl"/>
  <xsl:include href="terms-translation.xsl"/>
  <xsl:include href="eli-rdfa-production.xsl"/>
  <xsl:include href="eli-schema-org-production.xsl"/>

  <xsl:output method="xml" version="1.0" encoding="UTF-8"/>

  <!-- Stylesheet parameter: level of ELI entities where the HTML files are
       generated.
       When set to "expression", one HTML files is produced for each existing
       eli:LegalResource;
       When set to "format", one HTML files is produced for each existing
       eli:Format.
       Default value is "expression" -->
  <xsl:param name="htmlFilesLevel" select="'expression'"/>
  <!-- Stylesheet parameter: Lang code for the index page.
       Default value is "en". -->
  <xsl:param name="indexLangCode" select="'en'"/>
  <!-- Stylesheet parameter: type of output to be produced.
       When set to "alone", only outputs the HTML content inside a <div>;
       When set to "none", only outputs an HTML page with the RDFa and the
       Schema.Org properties in the HTML header (and nothing in the body);
       When set to "whole-page", output a whole HTML page with the HTML content
       in the body, the RDFa properties and the Schema.Org properties in the
       header.
       Default value is "whole-page". -->
  <xsl:param name="htmlContent" select="'whole-page'"/>
  <!-- Stylesheet parameter: save HTML produced by the stylesheet in different
       files.
       When set to "yes", the various HTML files produced by the stylesheet are
       saved in different files thanks to the exsl:document extension;
       When set to "no", the stylesheet outputs a global XML file with several
       <elid:file> elements each containing one HTML document.
       Default value is "yes". -->
  <xsl:param name="saveHtmlFiles" select="'yes'"/>


  <!-- XSL key indexing the <rdf:Description> with their attribute rdf:about -->
  <xsl:key name="rdfDesc" match="/rdf:RDF/rdf:Description"
           use="@rdf:about"/>
  <!-- XSL key indexing the <rdf:Description> with the attribute rdf:resource
       found in their properties. This is a key useful to find all the resources
       linked to a given resource. -->
  <xsl:key name="rdfDescInverse" match="/rdf:RDF/rdf:Description"
           use="*/@rdf:resource"/>


  <!-- Template for the root element of the source XML (ELI graph).
  -->
  <xsl:template match="rdf:RDF">

    <!-- Variable containing all the <rdf:Description> that describe a
         LegalResource that is not abstract ie that have no child with the
         is_member_of property. -->
    <xsl:variable name="concreteLegalResources"
                  select="/rdf:RDF/rdf:Description[
                            rdf:type/@rdf:resource='&eli;LegalResource'
                            and not(
                              key('rdfDescInverse', @rdf:about)
                                /eli:is_member_of/@rdf:resource = @rdf:about
                            ) ]"/>

    <xsl:for-each select="$concreteLegalResources">

      <!-- Variable containing all the <rdf:Description> that describe a
           Legal Expression child of the current Legal Resource -->
      <xsl:variable name="legalExpressions"
                    select="key('rdfDescInverse', @rdf:about)[
                              eli:realizes/@rdf:resource = current()/@rdf:about
                              and rdf:type/@rdf:resource='&eli;LegalExpression'
                            ]"/>

      <xsl:for-each select="$legalExpressions">

        <!-- Variable containing the language code of the current legal
             expression -->
        <xsl:variable name="lang"
                      select="translate(
                                key('rdfDesc', eli:language/@rdf:resource)
                                  /skos:notation,
                                'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                'abcdefghijklmnopqrstuvwxyz')"/>

        <!-- Variable containing all the <rdf:Description> that describe a
             Format child of the current Legal Expression -->
        <xsl:variable name="legalFormat"
                      select="key('rdfDescInverse', @rdf:about)[
                                eli:embodies/@rdf:resource
                                  = current()/@rdf:about
                                and rdf:type/@rdf:resource='&eli;Format'
                              ]"/>

        <xsl:choose>

          <!-- Produces one HTML file for each legal expression -->
          <xsl:when test="$htmlFilesLevel = 'expression'">

            <xsl:call-template name="create.html.file">
              <xsl:with-param name="filename"
                              select="concat('file-',position(),'.html')"/>
              <xsl:with-param name="nodeId" select="@rdf:about"/>
              <xsl:with-param name="data" select="."/>
              <xsl:with-param name="langCode" select="$lang"/>
            </xsl:call-template>

          </xsl:when>

          <!-- Produces one HTML file for each format -->
          <xsl:when test="$htmlFilesLevel = 'format'">

            <!-- Variable containing the position of the current legal
                 expression. -->
            <xsl:variable name="exprPos" select="position()"/>

            <xsl:for-each select="$legalFormat">
              <xsl:call-template name="create.html.file">
                <xsl:with-param name="filename"
                                select="concat('file-', $exprPos, '-',
                                               position(), '.html')"/>
                <xsl:with-param name="nodeId" select="@rdf:about"/>
                <xsl:with-param name="data" select="."/>
                <xsl:with-param name="langCode" select="$lang"/>
              </xsl:call-template>
            </xsl:for-each>

          </xsl:when>
        </xsl:choose>

      </xsl:for-each>

      <!-- Produces an empty index page for the LegalResource. This page will
           be filled in Python with the list of all the produced HTML pages. -->
      <xsl:call-template name="create.html.file">
        <xsl:with-param name="filename"
                        select="'index.html'"/>
        <xsl:with-param name="nodeId" select="@rdf:about"/>
        <xsl:with-param name="data" select="."/>
        <xsl:with-param name="langCode" select="$indexLangCode"/>
        <xsl:with-param name="htmlInsertionMode" select="'whole-page'"/>
      </xsl:call-template>

    </xsl:for-each>

  </xsl:template>


  <!-- Template called by the template-generation.xsl stylesheet to generate
       the title of the page.

       If the current element is a Legal Expression, outputs the title of this
       current Legal Expression. If the current element is a Format, outputs
       the title of the LegalExpression embodied by this Format and the label
       of this format. -->
  <xsl:template name="insert.title">
    <xsl:param name="langCode"/>

    <xsl:choose>

      <!-- Current node corresponds to an eli:LegalResource entity
           (the produced file is an index) -->
      <xsl:when test="rdf:type/@rdf:resource='&eli;LegalResource'">
        <xsl:value-of select="@rdf:about"/>
      </xsl:when>

      <!-- Current node corresponds to an eli:Format entity -->
      <xsl:when test="rdf:type/@rdf:resource='&eli;Format'">

        <!-- Legal Expression that is embodied by the current Format -->
        <xsl:variable name="parentExpr"
                      select="key('rdfDesc', eli:embodies/@rdf:resource)"/>

        <!-- vocabulary value describing the format of the current Format -->
        <xsl:variable name="formatDesc"
                      select="key('rdfDesc', eli:format/@rdf:resource)"/>

        <xsl:choose>

          <!-- Writes the title of the expression and the label of the
               format -->
          <xsl:when test="$parentExpr/eli:title and $formatDesc">
            <xsl:value-of select="$parentExpr/eli:title"/>
            <xsl:text> - </xsl:text>
            <xsl:call-template name="write.term.label">
              <xsl:with-param name="termDesc" select="$formatDesc"/>
              <xsl:with-param name="langCode" select="$langCode"/>
            </xsl:call-template>
          </xsl:when>

          <!-- Writes the title of the expression and the end of the
               format URI -->
          <xsl:when test="$parentExpr/eli:title">
            <xsl:value-of select="$parentExpr/eli:title"/>
            <xsl:text> - </xsl:text>
            <xsl:value-of select="substring-after(@rdf:about,
                                                  $parentExpr/@rdf:about)"/>
          </xsl:when>

          <!-- Writes the format URI -->
          <xsl:otherwise>
            <xsl:value-of select="@rdf:about"/>
          </xsl:otherwise>
        </xsl:choose>

      </xsl:when>

      <!-- Current node corresponds to an eli:LegalExpression entity -->
      <xsl:otherwise>

        <xsl:choose>
          <!-- Writes the title of the expression -->
          <xsl:when test="eli:title">
            <xsl:value-of select="eli:title"/>
          </xsl:when>

          <!-- Writes the resource URI -->
          <xsl:otherwise>
            <xsl:value-of select="@rdf:about"/>
          </xsl:otherwise>
        </xsl:choose>

      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>


  <!-- Template called by the template-generation.xsl stylesheet to generate
       the HTML content that will be inserted in the Web page.

       This template displays the current Concept Scheme (current node) and
       all the Concepts inside this scheme. -->
  <xsl:template name="insert.html.content">
    <xsl:param name="langCode"/>

    <xsl:choose>

      <!-- Current node corresponds to an eli:LegalResource entity
           (the produced file is an empty index that will be filled in Python
           with the list of the produced HTML pages) -->
      <xsl:when test="rdf:type/@rdf:resource='&eli;LegalResource'">
        <h1>
          <xsl:call-template name="insert.title">
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
        </h1>

        <h3>
          <xsl:call-template name="translate">
            <xsl:with-param name="term" select="'&eli;LegalExpression'"/>
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
        </h3>
        <ul id="legal-expressions"/>

        <h3>
          <xsl:call-template name="translate">
            <xsl:with-param name="term" select="'&eli;Format'"/>
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
        </h3>
        <ul id="formats"/>

        <xsl:call-template name="insertCreationData">
          <xsl:with-param name="legalResUri" select="@rdf:about"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:when>

      <!-- Current node corresponds to an eli:Format entity -->
      <xsl:when test="rdf:type/@rdf:resource='&eli;Format'">

        <!-- Legal Expression that is embodied by the current Format -->
        <xsl:variable name="legalExpr"
                      select="key('rdfDesc', eli:embodies/@rdf:resource)"/>

        <!-- Legal Resource that is realized by the previous Legal Expression -->
        <xsl:variable name="legalRes"
                      select="key('rdfDesc',
                              $legalExpr/eli:realizes/@rdf:resource)"/>

        <xsl:apply-templates select="$legalRes" mode="htmlResource">
          <xsl:with-param name="langCode" select="$langCode"/>
          <xsl:with-param name="eliExpressions" select="$legalExpr"/>
        </xsl:apply-templates>

        <xsl:apply-templates select="$legalExpr" mode="htmlExpression">
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:apply-templates>

        <xsl:apply-templates select="." mode="htmlFormat">
          <xsl:with-param name="langCode" select="$langCode"/>
          <xsl:with-param name="eliExpression" select="$legalExpr"/>
        </xsl:apply-templates>

        <xsl:call-template name="insertCreationData">
          <xsl:with-param name="legalResUri" select="$legalRes/@rdf:about"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:when>

      <!-- Current node corresponds to an eli:LegalExpression entity -->
      <xsl:otherwise>

        <!-- Legal Resource that is realized by the current Legal Expression -->
        <xsl:variable name="legalRes"
                      select="key('rdfDesc', eli:realizes/@rdf:resource)"/>

        <!-- Formats that embodies the current LegalExpression -->
        <xsl:variable name="legalFormats"
                      select="key('rdfDescInverse', @rdf:about)[
                               eli:embodies/@rdf:resource = current()/@rdf:about
                              ]"/>

        <xsl:apply-templates select="$legalRes" mode="htmlResource">
          <xsl:with-param name="langCode" select="$langCode"/>
          <xsl:with-param name="eliExpressions" select="."/>
        </xsl:apply-templates>

        <xsl:apply-templates select="." mode="htmlExpression">
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:apply-templates>

        <xsl:apply-templates select="$legalFormats" mode="htmlFormat">
          <xsl:with-param name="langCode" select="$langCode"/>
          <xsl:with-param name="eliExpression" select="."/>
        </xsl:apply-templates>

        <xsl:call-template name="insertCreationData">
          <xsl:with-param name="legalResUri" select="$legalRes/@rdf:about"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>

  </xsl:template>


  <!-- Template transforming a given <rdf:Description> describing an
       eli:LegalResource into HTML.

       This template writes several tables with all the properties that
       describe the entity. -->
  <xsl:template match="rdf:Description" mode="htmlResource">
    <xsl:param name="langCode"/>
    <xsl:param name="eliExpressions" select="empty[not(self::empty)]"/>

    <div class="row">
      <div class="col-md-12">
        <h3>
          <xsl:call-template name="writePropertyValue">
            <xsl:with-param name="node" select="."/>
            <xsl:with-param name="propName" select="'&eli;type_document'"/>
            <xsl:with-param name="propRendering" select="'coma-sep'"/>
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
        </h3>
      </div>
      <xsl:variable name="resIsPartOf">
        <xsl:call-template name="writePropertyValue">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="propName" select="'&eli;is_part_of'"/>
          <xsl:with-param name="propRendering" select="'paragraph'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:variable>
      <xsl:if test="string($resIsPartOf)">
        <div class="col-md-2 col-md-offset-6">
          <xsl:call-template name="translate">
            <xsl:with-param name="term" select="'officialJournal'"/>
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
        </div>
        <div class="col-md-4">
          <xsl:copy-of select="$resIsPartOf"/>
        </div>
      </xsl:if>
    </div>

    <xsl:call-template name="writePropertyTable">
      <xsl:with-param name="rows">
        <xsl:call-template name="writeUriIdRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="$eliExpressions"/>
          <xsl:with-param name="prop1Name" select="'&eli;title'"/>
          <xsl:with-param name="prop1Rendering" select="'paragraph'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="$eliExpressions"/>
          <xsl:with-param name="prop1Name" select="'&eli;title_alternative'"/>
          <xsl:with-param name="prop1Rendering" select="'paragraph'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="$eliExpressions"/>
          <xsl:with-param name="prop1Name" select="'&eli;title_short'"/>
          <xsl:with-param name="prop1Rendering" select="'paragraph'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:with-param>
    </xsl:call-template>

    <xsl:call-template name="writePropertyTable">
      <xsl:with-param name="rows">
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&elix;resource_type'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="prop2Name" select="'&eli;date_document'"/>
          <xsl:with-param name="prop2Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;juridiction'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;passed_by'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;responsibility_of'"/>
          <xsl:with-param name="altProp1Name" select="'&eli;responsibility_of_agent'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:with-param>
    </xsl:call-template>

    <xsl:call-template name="writePropertyTable">
      <xsl:with-param name="rows">
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;is_about'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;related_to'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;relevant_for'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;description'"/>
          <xsl:with-param name="prop1Rendering" select="'paragraph'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:with-param>
    </xsl:call-template>

    <xsl:call-template name="writePropertyTable">
      <xsl:with-param name="rows">
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;date_publication'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="prop2Name" select="'&eli;number'"/>
          <xsl:with-param name="prop2Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;is_part_of'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;in_force'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;first_date_entry_in_force'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="prop2Name" select="'&eli;date_no_longer_in_force'"/>
          <xsl:with-param name="prop2Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;date_applicability'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;version'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="prop2Name" select="'&eli;version_date'"/>
          <xsl:with-param name="prop2Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:with-param>
    </xsl:call-template>

    <xsl:call-template name="writePropertyTable">
      <xsl:with-param name="rows">
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;based_on'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;commences'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;amends'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;repeals'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;applies'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;transposes'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;cites'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;corrects'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;changes'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:with-param>
    </xsl:call-template>

    <xsl:call-template name="writePropertyTable">
      <xsl:with-param name="rows">
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;is_another_publication_of'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;consolidates'"/>
          <xsl:with-param name="prop1Rendering" select="'paragraph'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;has_part'"/>
          <xsl:with-param name="prop1Rendering" select="'paragraph'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:with-param>
    </xsl:call-template>

  </xsl:template>


  <!-- Template transforming a given <rdf:Description> describing an
       eli:LegalExpression into HTML.

       This template writes several tables with all the properties that
       describe the entity. -->
  <xsl:template match="rdf:Description" mode="htmlExpression">
    <xsl:param name="langCode"/>

    <div class="row">
      <div class="col-md-12">
        <h3>
          <xsl:call-template name="translate">
            <xsl:with-param name="term" select="'linguisticVersion'"/>
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
          <xsl:text> </xsl:text>
          <xsl:call-template name="writePropertyValue">
            <xsl:with-param name="node" select="."/>
            <xsl:with-param name="propName" select="'&eli;language'"/>
            <xsl:with-param name="propRendering" select="'coma-sep'"/>
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
        </h3>
      </div>
    </div>

    <xsl:call-template name="writePropertyTable">
      <xsl:with-param name="rows">
        <xsl:call-template name="writeUriIdRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;title'"/>
          <xsl:with-param name="prop1Rendering" select="'paragraph'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;title_alternative'"/>
          <xsl:with-param name="prop1Rendering" select="'paragraph'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;title_short'"/>
          <xsl:with-param name="prop1Rendering" select="'paragraph'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;juridiction'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;related_to'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;relevant_for'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;description'"/>
          <xsl:with-param name="prop1Rendering" select="'paragraph'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:with-param>
    </xsl:call-template>

    <xsl:call-template name="writePropertyTable">
      <xsl:with-param name="rows">
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;publisher'"/>
          <xsl:with-param name="altProp1Name" select="'&eli;publisher_agent'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;date_publication'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="prop2Name" select="'&eli;number'"/>
          <xsl:with-param name="prop2Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;in_force'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;first_date_entry_in_force'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="prop2Name" select="'&eli;date_no_longer_in_force'"/>
          <xsl:with-param name="prop2Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;date_applicability'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;version'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="prop2Name" select="'&eli;version_date'"/>
          <xsl:with-param name="prop2Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:with-param>
    </xsl:call-template>

    <xsl:call-template name="writePropertyTable">
      <xsl:with-param name="rows">
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;consolidates'"/>
          <xsl:with-param name="prop1Rendering" select="'paragraph'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:with-param>
    </xsl:call-template>

    <xsl:call-template name="writePropertyTable">
      <xsl:with-param name="rows">
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;commences'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;amends'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;repeals'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;transposes'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;cites'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;corrects'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;changes'"/>
          <xsl:with-param name="pro1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:with-param>
    </xsl:call-template>

  </xsl:template>


  <!-- Template transforming a given <rdf:Description> describing an
       eli:Format into HTML.

       This template writes several tables with all the properties that
       describe the entity. -->
  <xsl:template match="rdf:Description" mode="htmlFormat">
    <xsl:param name="langCode"/>
    <xsl:param name="eliExpression"/>

    <div class="row">
      <div class="col-md-12">
        <h3>
          <xsl:call-template name="translate">
            <xsl:with-param name="term" select="'linguisticVersion'"/>
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
          <xsl:text> </xsl:text>
          <xsl:call-template name="writePropertyValue">
            <xsl:with-param name="node" select="$eliExpression"/>
            <xsl:with-param name="propName" select="'&eli;language'"/>
            <xsl:with-param name="propRendering" select="'coma-sep'"/>
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
          <xsl:text> — </xsl:text>
          <xsl:call-template name="translate">
            <xsl:with-param name="term" select="'format'"/>
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
          <xsl:text> </xsl:text>
          <xsl:call-template name="writePropertyValue">
            <xsl:with-param name="node" select="."/>
            <xsl:with-param name="propName" select="'&eli;format'"/>
            <xsl:with-param name="propRendering" select="'coma-sep'"/>
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
        </h3>
      </div>
    </div>

    <xsl:call-template name="writePropertyTable">
      <xsl:with-param name="rows">
        <xsl:call-template name="writeUriIdRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;legal_value'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;publisher'"/>
          <xsl:with-param name="altProp1Name" select="'&eli;publisher_agent'"/>
          <xsl:with-param name="propR1endering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;licence'"/>
          <xsl:with-param name="prop1Rendering" select="'paragraph'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;rights'"/>
          <xsl:with-param name="prop1Rendering" select="'paragraph'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;rightsholder'"/>
          <xsl:with-param name="altProp1Name" select="'&eli;rightsholder_agent'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;published_in'"/>
          <xsl:with-param name="altProp1Name" select="'&eli;published_in_format'"/>
          <xsl:with-param name="prop1Rendering" select="'coma-sep'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:with-param>
    </xsl:call-template>

    <xsl:call-template name="writePropertyTable">
      <xsl:with-param name="rows">
        <xsl:call-template name="writePropertyRow">
          <xsl:with-param name="node" select="."/>
          <xsl:with-param name="prop1Name" select="'&eli;is_exemplified_by'"/>
          <xsl:with-param name="prop1Rendering" select="'paragraph'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:with-param>
    </xsl:call-template>

  </xsl:template>

  <xsl:template name="insertCreationData">
    <xsl:param name="legalResUri" select="''"/>
    <xsl:param name="langCode" select="$lang"/>

    <xsl:variable name="provEntities"
                  select="/rdf:RDF/rdf:Description[
                            rdf:type/@rdf:resource='&prov;Entity'
                            and prov:specializationOf/@rdf:resource = $legalResUri]"/>

    <footer>
      <xsl:for-each select="$provEntities[prov:generatedAtTime and prov:wasAttributedTo]">
        <p>
          <xsl:call-template name="translate">
            <xsl:with-param name="term" select="'created'"/>
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
          <xsl:if test="prov:generatedAtTime">
            <xsl:text> </xsl:text>
            <xsl:call-template name="translate">
              <xsl:with-param name="term" select="'onDatetime'"/>
              <xsl:with-param name="langCode" select="$langCode"/>
            </xsl:call-template>
            <xsl:text> </xsl:text>
            <xsl:value-of select="translate(prov:generatedAtTime/text(), 'TZ', ' ')"/>
          </xsl:if>
          <xsl:if test="prov:wasAttributedTo">
            <xsl:text> </xsl:text>
            <xsl:call-template name="translate">
              <xsl:with-param name="term" select="'byUser'"/>
              <xsl:with-param name="langCode" select="$langCode"/>
            </xsl:call-template>
            <xsl:text> </xsl:text>
            <xsl:value-of select="prov:wasAttributedTo/@rdf:resource"/>
          </xsl:if>
        </p>
      </xsl:for-each>
    </footer>

  </xsl:template>

  <!-- Template that writes properties into several rows inside a table. If there
       are no row, just inserts nothing. -->
  <xsl:template name="writePropertyTable">
    <xsl:param name="rows" select="''"/>

    <xsl:if test="normalize-space(string($rows)) != ''">
      <table class="table table-bordered">
        <tbody>
          <xsl:copy-of select="$rows"/>
        </tbody>
      </table>
    </xsl:if>
  </xsl:template>

  <!-- Template that writes the URI and the local identifiers of an
       entity in a table row. -->
  <xsl:template name="writeUriIdRow">
    <xsl:param name="node" select="empty[not(self::empty)]"/>
    <xsl:param name="langCode" select="$lang"/>

    <xsl:variable name="idLocal">
      <xsl:call-template name="writePropertyValue">
        <xsl:with-param name="node" select="$node"/>
        <xsl:with-param name="propName" select="'&eli;id_local'"/>
        <xsl:with-param name="propRendering" select="'coma-sep'"/>
      </xsl:call-template>
    </xsl:variable>

    <tr>
      <td class="col-md-2">
        <xsl:call-template name="translate">
          <xsl:with-param name="term" select="'identifierUri'"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </td>
      <xsl:choose>
        <xsl:when test="normalize-space(string($idLocal)) = ''">
          <td class="col-md-10" colspan="3">
            <xsl:value-of select="$node/@rdf:about"/>
          </td>
        </xsl:when>
        <xsl:otherwise>
          <td class="col-md-4">
            <xsl:value-of select="$node/@rdf:about"/>
          </td>
          <td class="col-md-2">
            <xsl:call-template name="translate">
              <xsl:with-param name="term" select="'&eli;id_local'"/>
              <xsl:with-param name="langCode" select="$langCode"/>
            </xsl:call-template>
          </td>
          <td class="col-md-4">
            <xsl:copy-of select="$idLocal"/>
          </td>
        </xsl:otherwise>
      </xsl:choose>
    </tr>
  </xsl:template>


  <!-- Template that writes one or two properties with their name and their
       values inside a table row. If there is only one property, it is spanned
       over all the row, else each property takes half of the row. -->
  <xsl:template name="writePropertyRow">
    <xsl:param name="node" select="empty[not(self::empty)]"/>
    <xsl:param name="prop1Name" select="''"/>
    <xsl:param name="altProp1Name" select="''"/>
    <xsl:param name="prop1Rendering" select="'coma-sep'"/>
    <xsl:param name="prop2Name" select="''"/>
    <xsl:param name="altProp2Name" select="''"/>
    <xsl:param name="prop2Rendering" select="'coma-sep'"/>
    <xsl:param name="langCode" select="$lang"/>

    <xsl:variable name="prop1Value">
      <xsl:call-template name="writePropertyValue">
        <xsl:with-param name="node" select="$node"/>
        <xsl:with-param name="propName" select="$prop1Name"/>
        <xsl:with-param name="altPropName" select="$altProp1Name"/>
        <xsl:with-param name="propRendering" select="$prop1Rendering"/>
        <xsl:with-param name="langCode" select="$langCode"/>
      </xsl:call-template>
    </xsl:variable>

    <xsl:variable name="prop2Value">
      <xsl:if test="$prop2Name != ''">
        <xsl:call-template name="writePropertyValue">
          <xsl:with-param name="node" select="$node"/>
          <xsl:with-param name="propName" select="$prop2Name"/>
          <xsl:with-param name="altPropName" select="$altProp2Name"/>
          <xsl:with-param name="propRendering" select="$prop2Rendering"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </xsl:if>
    </xsl:variable>

    <xsl:choose>
      <xsl:when test="normalize-space(string($prop1Value)) = '' and
                      normalize-space(string($prop2Value)) = ''"/>
      <xsl:when test="normalize-space(string($prop1Value)) != '' and
                      normalize-space(string($prop2Value)) != ''">
        <tr>
          <td class="col-md-2">
            <xsl:call-template name="translate">
              <xsl:with-param name="term" select="$prop1Name"/>
              <xsl:with-param name="langCode" select="$langCode"/>
            </xsl:call-template>
          </td>
          <td class="col-md-4">
            <xsl:copy-of select="$prop1Value"/>
          </td>
          <td class="col-md-2">
            <xsl:call-template name="translate">
              <xsl:with-param name="term" select="$prop2Name"/>
              <xsl:with-param name="langCode" select="$langCode"/>
            </xsl:call-template>
          </td>
          <td class="col-md-4">
            <xsl:copy-of select="$prop2Value"/>
          </td>
        </tr>
      </xsl:when>
      <xsl:when test="normalize-space(string($prop1Value)) != ''">
        <tr>
          <td class="col-md-2">
            <xsl:call-template name="translate">
              <xsl:with-param name="term" select="$prop1Name"/>
              <xsl:with-param name="langCode" select="$langCode"/>
            </xsl:call-template>
          </td>
          <td class="col-md-10" colspan="3">
            <xsl:copy-of select="$prop1Value"/>
          </td>
        </tr>
      </xsl:when>
      <xsl:when test="normalize-space(string($prop2Value)) != ''">
        <tr>
          <td class="col-md-2">
            <xsl:call-template name="translate">
              <xsl:with-param name="term" select="$prop2Name"/>
              <xsl:with-param name="langCode" select="$langCode"/>
            </xsl:call-template>
          </td>
          <td class="col-md-10" colspan="3">
            <xsl:copy-of select="$prop2Value"/>
          </td>
        </tr>
      </xsl:when>
    </xsl:choose>
  </xsl:template>


  <!-- Template that writes the values of a given property of an
       ELI entity.

       The value can be a URI towards another resource (cf. rdf:resource
       attribute on the property element in the source XML) or a textual value.

       The "node" parameter contains the <rdf:Description> element that
       contains all the properties about the current entity. The "propName"
       parameter contains the property name. The "altPropName" contains the
       name of an alternative property whose values will be written with the
       one of the previous property. The "propRendering" parameter contains
       either "paragraph" or "coma-sep" depending how the multiple values
       should be rendered: one paragraph for each value or all the values
       separated by comas. The "langCode" parameter contains the code of the
       chosen language (two letters code).

       It is possible to specify the name of a second property in the
       "prop2Name" parameter. If so, the values of the two properties are
       written.
  -->
  <xsl:template name="writePropertyValue">
    <xsl:param name="node" select="empty[not(self::empty)]"/>
    <xsl:param name="propName" select="''"/>
    <xsl:param name="altPropName" select="''"/>
    <xsl:param name="propRendering" select="'coma-sep'"/>
    <xsl:param name="langCode" select="$lang"/>

    <!-- All the XML elements inside <rdf:Description> whose name is the
         name of the current property. -->
    <xsl:variable name="directNodes"
                  select="$node/*[
                            concat(namespace-uri(),local-name())
                            = $propName
                          or
                            concat(namespace-uri(),local-name())
                            = $altPropName
                          ]"/>

    <!-- From these XML property elements, all the textual values of the
         XML elements. -->
    <xsl:variable name="texts"
                  select="$directNodes[not(@rdf:resource)]/text()"/>
    <!-- From these XML property elements, all the URIs of the XML elements
         that points towards a resource. -->
    <xsl:variable name="resourceURIs"
                  select="$directNodes[@rdf:resource]/@rdf:resource"/>
    <!-- Vocabulary concepts locally defined and corresponding to previous
         URIs.
         Here, we use the 'rdfDesc' XSL key to optimize the search of the
         resources corresponding to the URIs. -->
    <xsl:variable name="concepts"
                  select="key('rdfDesc', $resourceURIs)
                            [rdf:type/@rdf:resource = '&skos;Concept']"/>
    <!-- All the other URIs that don't correspond to vocabulary concepts. -->
    <xsl:variable name="otherURIs"
                  select="$resourceURIs[not($concepts/@rdf:about = .)]"/>

    <!-- Tests if we have any value for the current property-->
    <xsl:if test="$texts | $concepts | $otherURIs">

      <!-- All textual values. -->
      <xsl:for-each select="$texts">

        <xsl:choose>
          <xsl:when test="$propRendering='paragraph'">
            <p>
              <xsl:value-of select="."/>
            </p>
          </xsl:when>
          <xsl:otherwise>
            <xsl:if test="position() != 1">
              <xsl:text>, </xsl:text>
            </xsl:if>
            <xsl:value-of select="."/>
          </xsl:otherwise>
        </xsl:choose>

      </xsl:for-each>

      <!-- The labels of the vocabulary concepts. -->
      <xsl:for-each select="$concepts">

        <xsl:choose>
          <xsl:when test="$propRendering='paragraph'">
            <p>
              <xsl:call-template name="write.term.label">
                <xsl:with-param name="termDesc" select="."/>
                <xsl:with-param name="langCode" select="$langCode"/>
                <xsl:with-param name="insertLink" select="1"/>
              </xsl:call-template>
            </p>
          </xsl:when>
          <xsl:otherwise>
            <xsl:if test="position() != 1 or $texts">
              <xsl:text>, </xsl:text>
            </xsl:if>
            <xsl:call-template name="write.term.label">
              <xsl:with-param name="termDesc" select="."/>
              <xsl:with-param name="langCode" select="$langCode"/>
              <xsl:with-param name="insertLink" select="1"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>

      </xsl:for-each>

      <!-- The other URIs.
           We call the "translate" template in case the URI
           corresponds to a term that exists in one of the glossary
           (if not, the URI will be written). -->
      <xsl:for-each select="$otherURIs">

        <xsl:choose>
          <xsl:when test="$propRendering='paragraph'">
            <p>
              <xsl:choose>
                <xsl:when test="starts-with(., 'http://') or starts-with(., 'https://')">
                  <a href="{.}">
                    <xsl:call-template name="translate">
                      <xsl:with-param name="term" select="."/>
                      <xsl:with-param name="langCode" select="$langCode"/>
                    </xsl:call-template>
                  </a>
                </xsl:when>
                <xsl:otherwise>
                  <xsl:call-template name="translate">
                    <xsl:with-param name="term" select="."/>
                      <xsl:with-param name="langCode" select="$langCode"/>
                  </xsl:call-template>
                </xsl:otherwise>
              </xsl:choose>
            </p>
          </xsl:when>
          <xsl:otherwise>
            <xsl:if test="position() != 1 or $texts | $concepts">
              <xsl:text>, </xsl:text>
            </xsl:if>
            <xsl:choose>
              <xsl:when test="starts-with(., 'http://') or starts-with(., 'https://')">
                <a href="{.}">
                  <xsl:call-template name="translate">
                    <xsl:with-param name="term" select="."/>
                    <xsl:with-param name="langCode" select="$langCode"/>
                  </xsl:call-template>
                </a>
              </xsl:when>
              <xsl:otherwise>
                <xsl:call-template name="translate">
                  <xsl:with-param name="term" select="."/>
                  <xsl:with-param name="langCode" select="$langCode"/>
                </xsl:call-template>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:otherwise>
        </xsl:choose>

      </xsl:for-each>

    </xsl:if>
  </xsl:template>


  <!-- Template writing the label of a vocabulary term in a given language.

       "termDesc" contains the rdf:Description of the vocabulary term. -->
  <xsl:template name="write.term.label">
    <xsl:param name="termDesc"/>
    <xsl:param name="langCode"/>
    <xsl:param name="insertLink" select="0"/>

    <xsl:variable name="text">
      <xsl:choose>
        <xsl:when test="$termDesc/skos:prefLabel[@xml:lang=$langCode]">
          <xsl:value-of select="$termDesc/skos:prefLabel[@xml:lang=$langCode]"/>
        </xsl:when>
        <xsl:when test="$termDesc/skos:prefLabel[not(@xml:lang)]">
          <xsl:value-of select="$termDesc/skos:prefLabel[not(@xml:lang)]"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="$termDesc/@rdf:about"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <xsl:choose>
      <xsl:when test="$insertLink and (starts-with($termDesc/@rdf:about, 'http://') or starts-with($termDesc/@rdf:about, 'https://'))">
        <a href="{$termDesc/@rdf:about}">
          <xsl:value-of select="$text"/>
        </a>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$text"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
</xsl:stylesheet>
