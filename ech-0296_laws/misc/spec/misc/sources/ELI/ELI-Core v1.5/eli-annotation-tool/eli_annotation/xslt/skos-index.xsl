<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE xsl:stylesheet
 [
  <!ENTITY rdf "http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <!ENTITY skos "http://www.w3.org/2004/02/skos/core#">
 ]>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0"
                xmlns:elit="urn:eli:annotation-tool:template:"
                xmlns:elid="urn:eli:annotation-tool:data:"
                xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                xmlns:skos="http://www.w3.org/2004/02/skos/core#"
                exclude-result-prefixes="elit elid rdf skos">

  <xsl:import href="template-generation.xsl"/>
  <xsl:include href="terms-translation.xsl"/>

  <xsl:output method="xml" version="1.0" encoding="UTF-8"/>

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


  <!-- Template for the root element of the source XML (SKOS vocabulary).

       Selects all the concept schemes that have a RDF description and
       produces one file per scheme. Please note that the concept schemes
       that are used inside the concepts (e.g. with the inScheme property)
       but that are not properly declared with a RDF description will not be
       processed.
  -->
  <xsl:template match="rdf:RDF">
    <!-- Variable containing all the <rdf:Description> that describe a
         ConceptScheme. -->
    <xsl:variable name="conceptSchemes"
                  select="/rdf:RDF/rdf:Description[
                          rdf:type/@rdf:resource='&skos;ConceptScheme' ]"/>

    <xsl:for-each select="$conceptSchemes">
      <xsl:call-template name="create.html.file">
        <xsl:with-param name="filename" select="concat('file-',position(),'.html')"/>
        <xsl:with-param name="nodeId" select="@rdf:about"/>
        <xsl:with-param name="data" select="."/>
        <xsl:with-param name="langCode" select="$indexLangCode"/>
        <xsl:with-param name="htmlInsertionMode" select="'whole-page'"/>
      </xsl:call-template>
    </xsl:for-each>

  </xsl:template>


  <!-- Template called by the template-generation.xsl stylesheet to generate
       the title of the page.

       This template just outputs the URI of the current Concept Scheme
       (current node). -->
  <xsl:template name="insert.title">
    <xsl:param name="langCode"/>

    <xsl:value-of select="@rdf:about"/>
  </xsl:template>


  <!-- Template called by the template-generation.xsl stylesheet to generate
       the HTML content that will be inserted in the Web page.

       This template displays the URI of the Concept Scheme (current node) and
       inserts an empty list. -->
  <xsl:template name="insert.html.content">
    <xsl:param name="langCode"/>

    <h1>
      <xsl:value-of select="@rdf:about"/>
    </h1>

    <ul id="concept-scheme"/>
  </xsl:template>

</xsl:stylesheet>
