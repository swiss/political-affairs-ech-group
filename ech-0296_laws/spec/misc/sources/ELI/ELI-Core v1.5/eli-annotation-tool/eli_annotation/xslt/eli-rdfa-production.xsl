<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE xsl:stylesheet>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0"
                xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                exclude-result-prefixes="rdf">

  <xsl:include href="rdfa-production.xsl"/>


  <!-- Template called by the template-generation.xsl stylesheet to generate
       the RDF-a content that will be inserted in the Web page.

       This template transforms all the <rdf:Description> elements in the
       file into into <meta> tags that will be inserted in the HTML
       header. -->
  <xsl:template name="insert.rdfa.content">
    <xsl:param name="langCode"/>

    <!-- Processes all the RDF entities found in the file -->
    <xsl:apply-templates select="/rdf:RDF/rdf:Description" mode="rdfa"/>

  </xsl:template>

</xsl:stylesheet>
