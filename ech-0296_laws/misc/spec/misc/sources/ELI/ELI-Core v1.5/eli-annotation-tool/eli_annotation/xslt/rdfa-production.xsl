<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE xsl:stylesheet>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0"
                xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                exclude-result-prefixes="rdf">

  <!-- Template transforming the rdf:Description into a set of HTML <meta>
       tags inserted in the header, each one containing a RDF property.
  -->
  <xsl:template match="rdf:Description" mode="rdfa">

    <!-- First, selects the rdf:type property and transforms it in a <meta>
         tag containing RDFa. -->
    <xsl:apply-templates select="rdf:type" mode="rdfa">
      <xsl:with-param name="about" select="@rdf:about"/>
    </xsl:apply-templates>

    <!-- Then, selects all the remaining properties and transforms them in
         <meta> tags containing RDFa. -->
    <xsl:apply-templates select="*[not(self::rdf:type)]" mode="rdfa">
      <xsl:with-param name="about" select="@rdf:about"/>
    </xsl:apply-templates>

  </xsl:template>


  <!-- Template transforming any property (described in RDF XML) into RDFa
       inside a HTML <meta> tag that will be inserted in the header of the page.

       The "about" parameter contains the URI of the subject of the RDF
       predicate. -->
  <xsl:template match="*" mode="rdfa">
    <xsl:param name="about" select="''"/>

    <!-- Creates the <meta> tag with the URI of the subject of the predicate
         in an about attribute and the name of the RDF property in a property
         attribute. -->
    <meta about="{$about}" property="{concat(namespace-uri(), local-name())}">
      <xsl:choose>

        <!-- The RDF property points towards another resource. -->
        <xsl:when test="@rdf:resource">
          <!-- Adds a resource attribute containing the URI of the object. -->
          <xsl:attribute name="resource">
            <xsl:value-of select="@rdf:resource"/>
          </xsl:attribute>
        </xsl:when>

        <!-- The RDF property contains textual data. -->
        <xsl:otherwise>
          <!-- Adds a lang attribute containing the language specification (if
               any) -->
          <xsl:if test="@xml:lang">
            <xsl:attribute name="lang">
              <xsl:value-of select="@xml:lang"/>
            </xsl:attribute>
          </xsl:if>

          <!-- Adds a datatype attribute containing the type of the content
               (if any) -->
          <xsl:if test="@rdf:datatype">
            <xsl:attribute name="datatype">
              <xsl:value-of select="@rdf:datatype"/>
            </xsl:attribute>
          </xsl:if>

          <!-- Adds a content attribute with the actual textual content -->
          <xsl:attribute name="content">
            <xsl:value-of select="text()"/>
          </xsl:attribute>
        </xsl:otherwise>
      </xsl:choose>
    </meta>
  </xsl:template>


  <!-- Template transforming an RDF type (described in XML) into RDFa
       inside a HTML <meta> tag that will be inserted in the header of the page.

       The "about" parameter contains the URI of the subject of the RDF
       predicate. -->
  <xsl:template match="rdf:type" mode="rdfa">
    <xsl:param name="about" select="''"/>

    <meta about="{$about}" typeof="{@rdf:resource}"/>
  </xsl:template>


</xsl:stylesheet>
