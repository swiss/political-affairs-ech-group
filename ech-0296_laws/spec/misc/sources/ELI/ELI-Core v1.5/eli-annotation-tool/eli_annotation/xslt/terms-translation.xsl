<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE xsl:stylesheet
 [
  <!ENTITY rdf "http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <!ENTITY skos "http://www.w3.org/2004/02/skos/core#">
  <!ENTITY dct "http://purl.org/dc/terms/">
  <!ENTITY euvoc "http://publications.europa.eu/ontology/euvoc#">
  <!ENTITY eli "http://data.europa.eu/eli/ontology#">
 ]>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:elid="urn:eli:annotation-tool:data:"
                version="1.0"
                exclude-result-prefixes="elid">

  <!-- Parameter containing the path to the XML file that contains the glossary
  -->
  <xsl:param name="glossaryFile" select="''"/>

  <!-- Global variable containing the root element of the XML document defining
       the glossary. -->
  <xsl:variable name="glossary" select="document($glossaryFile)/glossary"/>

  <!-- XSL key indexing the <term> elements of the glossary with their name
       attribute. -->
  <xsl:key name="glossterm" match="glossary/term" use="@name"/>

  <!-- Global variable containing the known namespaces and their prefixes. If
       the term can't be translated and it starts with a known namespace, we
       replace the namespace with the associated prefix before writing the term
       (which is indeed a URI). (cf. <elid:known-namespaces> element at
       the end of this stylesheet). -->
  <xsl:variable name="knownNamespaces"
                select="document('')/xsl:stylesheet/elid:known-namespaces
                          /elid:namespace"/>

  <!-- Template that translates a given term into the chosen language. The
       mapping between the terms and their translations is given in the
       glossary XML file loaded into the "glossary" global variable.

       If the translation in the chosen language can't be found, the template
       outputs the term itself. If the term is a property beginning with a
       known namespace (cf. "knownNamespaces" global variable), the namespace
       is replaced by a prefix.

       The "term" parameter contains the term to be translated. It actually is
       the name of a property (with its namespace).
       The "langCode" parameter contains the code of the chosen language (2
       letters code). -->
  <xsl:template name="translate">
    <xsl:param name="term" select="''"/>
    <xsl:param name="langCode" select="'en'"/>

    <xsl:choose>
      <xsl:when test="$glossary">

        <!-- This for-each is only used to change the current document and
             therefore be able to use the 'glossterm' XSL key. The "glossary"
             variable just contains the root element of the XML document
             defining the glossary. -->
        <xsl:for-each select="$glossary">

          <!-- Labels extracted from the glossary that correspond to the term
               and to the chosen language. -->
          <xsl:variable name="langLabel"
                        select="key('glossterm', $term)
                                /label[ @lang = $langCode ]"/>

          <xsl:choose>
            <!-- Tries to find a translation in the chosen language. -->
            <xsl:when test="$langLabel">
              <xsl:value-of select="$langLabel"/>
            </xsl:when>
            <!-- Else, outputs the literal value of the term. -->
            <xsl:otherwise>
              <xsl:call-template name="write.term.qname">
                <xsl:with-param name="term" select="$term"/>
              </xsl:call-template>
            </xsl:otherwise>
          </xsl:choose>

        </xsl:for-each>
      </xsl:when>
      <xsl:otherwise>
        <xsl:call-template name="write.term.qname">
          <xsl:with-param name="term" select="$term"/>
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>


  <!-- Template that returns the help message associated to a given term, in
       the chosen language. The mapping between the terms and their help
       messages is given in the glossary XML file loaded into the "glossary"
       global variable.

       The "term" parameter contains the term whose help must be outputted. It
       actually is the name of a property (with its namespace).
       The "langCode" parameter contains the code of the chosen language (2
       letters code). -->
  <xsl:template name="getHelpText">
    <xsl:param name="term" select="''"/>
    <xsl:param name="langCode" select="'en'"/>

    <!-- This for-each is only used to change the current document and
         therefore be able to use the 'glossterm' XSL key. The "glossary"
         variable just contains the root element of the XML document defining
         the glossary. -->
    <xsl:for-each select="$glossary">

      <!-- Outputs the help section of the glossary that corresponds to
           the term and the chosen language. -->
      <xsl:copy-of select="key('glossterm', $term)
                              /help[ @lang = $langCode ]/node()"/>

    </xsl:for-each>
  </xsl:template>


  <!-- Template that writes the qualified name of a term that couldn't be
       translated.

       If the term starts with a known namespace, uses the associated standard
       prefix, else writes the entire qualified name. -->
  <xsl:template name="write.term.qname">
    <xsl:param name="term"/>

    <!-- Selects the known namespace that begins the literal value of
         the term. -->
    <xsl:variable name="nspace"
                  select="$knownNamespaces[starts-with($term, text())]"/>
    <xsl:choose>
      <!-- If a known namespace begins the literal value of the term,
           replaces this namespace with its prefix. -->
      <xsl:when test="$nspace">
        <xsl:value-of select="$nspace/@prefix"/>
        <xsl:text>:</xsl:text>
        <xsl:value-of select="substring-after($term, $nspace/text())"/>
      </xsl:when>
      <!-- Else, writes the literal value of the term. -->
      <xsl:otherwise>
        <xsl:value-of select="$term"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>


  <!-- This element contains the known namespaces and associates a prefix
       to each namespace.

       This association will be used if a term can't be translated and is, in
       fact a URI that starts with the namepace URI: before writing the term
       the namespace is replaced by the prefix in order to have something
       easily readable. -->
  <elid:known-namespaces>
    <elid:namespace prefix="rdf">&rdf;</elid:namespace>
    <elid:namespace prefix="skos">&skos;</elid:namespace>
    <elid:namespace prefix="dct">&dct;</elid:namespace>
    <elid:namespace prefix="euvoc">&euvoc;</elid:namespace>
    <elid:namespace prefix="eli">&eli;</elid:namespace>
  </elid:known-namespaces>

</xsl:stylesheet>
