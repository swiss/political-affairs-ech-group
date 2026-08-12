<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE xsl:stylesheet>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0"
                xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                xmlns:skos="http://www.w3.org/2004/02/skos/core#"
                exclude-result-prefixes="rdf skos">

  <xsl:include href="rdfa-production.xsl"/>


  <!-- Template called by the template-generation.xsl stylesheet to generate
       the RDF-a content that will be inserted in the Web page.

       This template will transform the current Concept Scheme (current node)
       and all the Concepts inside this scheme. This template describes all
       the RDF properties into <meta> tags that will be inserted in the HTML
       header. -->
  <xsl:template name="insert.rdfa.content">
    <xsl:param name="langCode"/>

    <!-- Processes the current Concept Scheme -->
    <xsl:apply-templates select="." mode="rdfa"/>

    <!-- Variable containing all the <rdf:Description> that describe a
         Concept inside the current ConceptScheme. -->
    <xsl:variable name="concepts"
                  select="  key('rdfDescInScheme', @rdf:about)
                          | key('rdfDesc', skos:hasTopConcept/@rdf:resource)"/>

    <!-- Processes the Concepts inside this Concept Scheme. -->
    <xsl:apply-templates select="$concepts" mode="rdfa"/>

  </xsl:template>

</xsl:stylesheet>
