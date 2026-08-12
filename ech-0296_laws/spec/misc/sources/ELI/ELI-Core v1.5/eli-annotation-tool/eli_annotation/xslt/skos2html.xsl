<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE xsl:stylesheet
 [
  <!ENTITY rdf "http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <!ENTITY skos "http://www.w3.org/2004/02/skos/core#">
  <!ENTITY dct "http://purl.org/dc/terms/">
  <!ENTITY euvoc "http://publications.europa.eu/ontology/euvoc#">
  <!ENTITY elis "urn:eli-annotation-tool:skos:ontology-extension:">
 ]>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0"
                xmlns:elixt="urn:eli:annotation-tool:xslt:extension:"
                xmlns:elid="urn:eli:annotation-tool:data:"
                xmlns:elis="urn:eli-annotation-tool:skos:ontology-extension:"
                xmlns:elit="urn:eli:annotation-tool:template:"
                xmlns:dct="http://purl.org/dc/terms/"
                xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                xmlns:skos="http://www.w3.org/2004/02/skos/core#"
                xmlns:euvoc="http://publications.europa.eu/ontology/euvoc#"
                xmlns:func="http://exslt.org/functions"
                extension-element-prefixes="func"
                exclude-result-prefixes="elixt elid elis elit dct rdf skos euvoc">

  <xsl:import href="template-generation.xsl"/>
  <xsl:include href="terms-translation.xsl"/>
  <xsl:include href="skos-rdfa-production.xsl"/>

  <xsl:output method="xml" version="1.0" encoding="UTF-8"/>

  <!-- Stylesheet parameter: chosen language for the HTML output page. -->
  <xsl:param name="lang" select="'en'"/>
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
  <!-- XSL key indexing the <rdf:Description> with the URI of the ConceptScheme
       they belong to (skos:InScheme and skos:topConceptOf properties). -->
  <xsl:key name="rdfDescInScheme" match="/rdf:RDF/rdf:Description"
           use="skos:inScheme/@rdf:resource|skos:topConceptOf/@rdf:resource"/>


  <!-- Global variable containing the ordered list of the properties we will
       display for each resource (cf. <elid:display-properties> element at
       the end of this stylesheet and "displayProperties" template). -->
  <xsl:variable name="displayProps"
                select="document('')/xsl:stylesheet
                          /elid:display-properties/elid:property"/>


  <!-- Template for the root element of the source XML (SKOS vocabulary).

       Selects all the concept schemes that have a RDF description and
       produces one file per scheme. Please note that the concept schemes
       that are used inside the concepts (e.g. with the inScheme property)
       but that are not properly declared with a RDF description will not be
       transformed into HTML. Consequently, the concepts that only are in an
       undeclared concept scheme will never appear into an HTML document.
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
        <xsl:with-param name="langCode" select="$lang"/>
      </xsl:call-template>
    </xsl:for-each>

  </xsl:template>


  <!-- Template called by the template-generation.xsl stylesheet to generate
       the title of the page.

       This template just outputs the title of the current Concept Scheme
       (current node). -->
  <xsl:template name="insert.title">
    <xsl:param name="langCode"/>

    <xsl:apply-templates select="." mode="resourceName">
      <xsl:with-param name="textOnly" select="1"/>
      <xsl:with-param name="langCode" select="$langCode"/>
    </xsl:apply-templates>
  </xsl:template>


  <!-- Template called by the template-generation.xsl stylesheet to generate
       the HTML content that will be inserted in the Web page.

       This template displays the current Concept Scheme (current node) and
       all the Concepts inside this scheme. -->
  <xsl:template name="insert.html.content">
    <xsl:param name="langCode"/>

    <h1>
      <xsl:apply-templates select="." mode="resourceName">
        <xsl:with-param name="insertAnchor" select="1"/>
        <xsl:with-param name="currentSchemeURI" select="@rdf:about"/>
        <xsl:with-param name="langCode" select="$langCode"/>
      </xsl:apply-templates>
    </h1>

    <table class="table table-bordered">
      <tbody>
        <!-- URI -->
        <tr>
          <th class="col-xs-2">URI</th>
          <td class="col-xs-10">
            <xsl:value-of select="@rdf:about"/>
          </td>
        </tr>
        <!-- Type -->
        <tr>
          <th class="col-xs-2">
            <xsl:call-template name="translate">
              <xsl:with-param name="term" select="'&rdf;type'"/>
              <xsl:with-param name="langCode" select="$langCode"/>
            </xsl:call-template>
          </th>
          <td class="col-xs-10">
            <xsl:call-template name="translate">
              <xsl:with-param name="term" select="'&skos;ConceptScheme'"/>
              <xsl:with-param name="langCode" select="$langCode"/>
            </xsl:call-template>
          </td>
        </tr>
        <!-- Various properties describing the Concept Scheme -->
        <xsl:call-template name="writeAllProperties">
          <xsl:with-param name="currentSchemeURI" select="@rdf:about"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </tbody>
    </table>

    <!-- Variable containing all the <rdf:Description> that describe a
         Concept inside the current ConceptScheme. -->
    <xsl:variable name="concepts"
                  select="  key('rdfDescInScheme', @rdf:about)
                          | key('rdfDesc', skos:hasTopConcept/@rdf:resource)"/>

    <!-- Displays the Concepts inside this Concept Scheme. -->

    <!-- If possible (extension available), we use the customized
         elixt:concept-name function to sort the <rdf:Description>
         corresponding to the Concepts, else we use several sorting
         keys (but the resulting sorting is not correct if all the Concept
         don't use the same sorting key). -->
    <xsl:choose>
      <xsl:when test="function-available('elixt:concept-name')">

        <xsl:apply-templates select="$concepts" mode="htmlConcept">
          <xsl:sort select="elixt:concept-name(.,$langCode)"/>
          <xsl:with-param name="currentSchemeURI" select="@rdf:about"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:apply-templates>

      </xsl:when>
      <xsl:otherwise>

        <xsl:apply-templates select="$concepts" mode="htmlConcept">
          <xsl:sort select="skos:prefLabel[@xml:lang=$langCode]"/>
          <xsl:sort select="dct:title[@xml:lang=$langCode]"/>
          <xsl:sort select="skos:altLabel[@xml:lang=$langCode][1]"/>
          <xsl:sort select="dct:alternative[@xml:lang=$langCode][1]"/>
          <xsl:sort select="skos:prefLabel[not(@xml:lang)]"/>
          <xsl:sort select="dct:title[not(@xml:lang)]"/>
          <xsl:sort select="skos:altLabel[not(@xml:lang)][1]"/>
          <xsl:sort select="dct:alternative[not(@xml:lang)][1]"/>
          <xsl:sort select="@rdf:about"/>

          <xsl:with-param name="currentSchemeURI" select="@rdf:about"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:apply-templates>

      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>


  <!-- Template transforming a given <rdf:Description> describing a
       Concept into HTML.

       This template writes a table with all the defined properties that
       describe the Concept (cf. "writeAllProperties" template). -->
  <xsl:template match="rdf:Description" mode="htmlConcept">
    <xsl:param name="currentSchemeURI" select="''"/>
    <xsl:param name="langCode"/>

    <h2>
      <xsl:apply-templates select="." mode="resourceName">
        <xsl:with-param name="insertAnchor" select="1"/>
        <xsl:with-param name="currentSchemeURI" select="$currentSchemeURI"/>
        <xsl:with-param name="langCode" select="$langCode"/>
      </xsl:apply-templates>
    </h2>


    <table class="table table-bordered">
      <tbody>
        <!-- URI -->
        <tr>
          <th class="col-xs-2">URI</th>
          <td class="col-xs-10">
            <xsl:value-of select="@rdf:about"/>
          </td>
        </tr>
        <!-- Type -->
        <tr>
          <th class="col-xs-2">
            <xsl:call-template name="translate">
              <xsl:with-param name="term" select="'&rdf;type'"/>
              <xsl:with-param name="langCode" select="$langCode"/>
            </xsl:call-template>
          </th>
          <td class="col-xs-10">
            <xsl:call-template name="translate">
              <xsl:with-param name="term" select="'&skos;Concept'"/>
              <xsl:with-param name="langCode" select="$langCode"/>
            </xsl:call-template>
          </td>
        </tr>
        <!-- Various properties describing the Concept -->
        <xsl:call-template name="writeAllProperties">
          <xsl:with-param name="currentSchemeURI" select="$currentSchemeURI"/>
          <xsl:with-param name="langCode" select="$langCode"/>
        </xsl:call-template>
      </tbody>
    </table>
  </xsl:template>


  <!-- Template giving the name of a <rdf:Description> (describing a
       Concept Scheme or a Concept).

       The name is inserted in an HTML <span> and is localised in the desired
       language. It is possible to insert an anchor with an identifier built
       from the resource URI or to insert an internal link (using the same
       identifier).
       The internal identifier of the links is built thanks to the
       "buildLink" template.

       The "langCode" parameter contains the code of the chosen language (two
       letters code).
       The "textOnly" parameter is set to 1 if only the text must be generated;
       in such a case, no anchor and no link will be generated.
       The "insertAnchor" parameter is set to 1 if an anchor must be generated.
       The "insertLink" parameter is set to 1 if an internal link must be
       generated.
  -->
  <xsl:template match="rdf:Description" mode="resourceName">
    <xsl:param name="langCode"/>
    <xsl:param name="insertAnchor" select="0"/>
    <xsl:param name="insertLink" select="0"/>
    <xsl:param name="textOnly" select="0"/>
    <xsl:param name="currentSchemeURI" select="''"/>

    <!-- Name of the Concept Scheme of the Concept. If possible (extension
         available), we use the customized elixt:concept-name function that
         computes the name. Else, we compute it thanks to an XSL
         multi-choice. -->
    <xsl:variable name="name">
      <xsl:choose>
        <xsl:when test="function-available('elixt:concept-name')">
          <xsl:value-of select="elixt:concept-name(.,$langCode)"/>
        </xsl:when>
        <xsl:when test="normalize-space(skos:prefLabel[@xml:lang=$langCode])">
          <xsl:value-of select="skos:prefLabel[@xml:lang=$langCode]"/>
        </xsl:when>
        <xsl:when test="normalize-space(dct:title[@xml:lang=$langCode])">
          <xsl:value-of select="dct:title[@xml:lang=$langCode]"/>
        </xsl:when>
        <xsl:when test="normalize-space(skos:altLabel[@xml:lang=$langCode])">
          <xsl:value-of select="skos:altLabel[@xml:lang=$langCode][1]"/>
        </xsl:when>
        <xsl:when test="normalize-space(dct:alternative[@xml:lang=$langCode])">
          <xsl:value-of select="dct:alternative[@xml:lang=$langCode][1]"/>
        </xsl:when>
        <xsl:when test="normalize-space(skos:prefLabel[not(@xml:lang)])">
          <xsl:value-of select="skos:prefLabel[not(@xml:lang)]"/>
        </xsl:when>
        <xsl:when test="normalize-space(dct:title[not(@xml:lang)])">
          <xsl:value-of select="dct:title[not(@xml:lang)]"/>
        </xsl:when>
        <xsl:when test="normalize-space(skos:altLabel[not(@xml:lang)])">
          <xsl:value-of select="skos:altLabel[not(@xml:lang)][1]"/>
        </xsl:when>
        <xsl:when test="normalize-space(dct:alternative[not(@xml:lang)])">
          <xsl:value-of select="dct:alternative[not(@xml:lang)][1]"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="@rdf:about"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>

    <!-- Internal identifier of the Concept Scheme or the Concept for the links
         or the anchor. -->
    <xsl:variable name="linkTarget">
      <xsl:call-template name="buildLink">
        <xsl:with-param name="uri" select="@rdf:about"/>
        <xsl:with-param name="currentSchemeURI" select="$currentSchemeURI"/>
      </xsl:call-template>
    </xsl:variable>

    <!-- Builds the HTML containing the name and eventually the link or the
         anchor. -->
    <xsl:choose>
      <!-- Text only -->
      <xsl:when test="$textOnly!=0">
        <xsl:value-of select="$name"/>
      </xsl:when>
      <!-- No link to be inserted -->
      <xsl:when test="$insertLink=0">
        <span>
          <!-- If wanted, inserts the anchor (HTML id attribute). -->
          <xsl:if test="$insertAnchor!=0">
            <xsl:attribute name="id">
              <xsl:value-of select="$linkTarget"/>
            </xsl:attribute>
          </xsl:if>
          <xsl:value-of select="$name"/>
        </span>
      </xsl:when>
      <!-- Internal link to be inserted -->
      <xsl:otherwise>
        <a href="#{$linkTarget}">
          <!-- If wanted, inserts the anchor (HTML id attribute) event if it
               doesn't make any sense to have the anchor and the link on the
               same HTML node. -->
          <xsl:if test="$insertAnchor!=0">
            <xsl:attribute name="id">
              <xsl:value-of select="$linkTarget"/>
            </xsl:attribute>
          </xsl:if>
          <xsl:value-of select="$name"/>
        </a>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>


  <!-- Template building the link towards a Concept Scheme or a Concept
       described in the SKOS vocabulary. It can either be an internal
       link if the resource is displayed in the same HTML page (current
       Concept Scheme or Concept in this scheme) or an external link.

       If it is an internal link, removes from the URI the Concept Scheme
       URI to only keep the local identifier.
       If it is an external link, keeps the URI unchanged. -->
  <xsl:template name="buildLink">
    <xsl:param name="uri" select="@rdf:about"/>
    <xsl:param name="currentSchemeURI" select="''"/>

    <xsl:choose>
      <xsl:when test="not(starts-with($uri, $currentSchemeURI))">
        <xsl:value-of select="$uri"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:variable name="localUri" select="substring-after($uri, $currentSchemeURI)"/>
        <xsl:choose>
          <xsl:when test="normalize-space($localUri) = ''">
            <xsl:choose>
              <xsl:when test="starts-with($uri, 'http://')">
                <xsl:value-of select="translate(
                                        substring-after($uri, 'http://'),
                                        ':#','//')"/>
              </xsl:when>
              <xsl:when test="starts-with($uri, 'urn:')">
                <xsl:value-of select="translate(
                                        substring-after($uri, 'urn:'),
                                        ':#','//')"/>
              </xsl:when>
              <xsl:otherwise>
                <xsl:value-of select="translate($uri, ':#', '//')"/>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:when>
          <xsl:when test="starts-with($localUri, '#')">
            <xsl:value-of select="substring-after($localUri, '#')"/>
          </xsl:when>
          <xsl:when test="starts-with($localUri, '/')">
            <xsl:value-of select="substring-after($localUri, '/')"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$localUri"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>


  <!-- If the "http://exslt.org/functions" extension is available, the
       following template defines a function that can used inside the XSL select
       attributes, for example for sorting the elements (that's the main reason
       why we use this extension).

       This function gives the name of a Concept or a Concept Scheme defined
       into a <rdf:Description> element.

       The Function returns the text value of the first property that exists
       amongst skos:prefLabel for the chosen language, dct:title for the
       chosen language, skos:altLabel for the chosen language, dct:alternative
       for the chosen language, skos:prefLabel with no specified language,
       dct:title with no specified language, skos:altLabel with no specified
       language, dct:alternative with no specified language. If nothing is
       found in these properties, returns the URI (from rdf:about attribute).

       The "node" parameter contains the <rdf:Description> element describing
       the Concept Scheme or the Concept whose name is wanted.
       The "langCode" parameter contains the code of the chosen language (two
       letters code).
  -->
  <func:function name="elixt:concept-name">
    <xsl:param name="node" select="."/>
    <xsl:param name="langCode"/>

    <xsl:choose>
      <!-- skos:prefLabel in chosen language -->
      <xsl:when test="normalize-space(
                        $node/skos:prefLabel[@xml:lang=$langCode] )">
        <func:result select="$node/skos:prefLabel[@xml:lang=$langCode]"/>
      </xsl:when>
      <!-- dct:title in chosen language -->
      <xsl:when test="normalize-space(
                        $node/dct:title[@xml:lang=$langCode] )">
        <func:result select="$node/dct:title[@xml:lang=$langCode]"/>
      </xsl:when>
      <!-- first skos:altLabel in chosen language -->
      <xsl:when test="normalize-space(
                        $node/skos:altLabel[@xml:lang=$langCode][1] )">
        <func:result select="$node/skos:altLabel[@xml:lang=$langCode][1]"/>
      </xsl:when>
      <!-- first dct:alternative in chosen language -->
      <xsl:when test="normalize-space(
                        $node/dct:alternative[@xml:lang=$langCode][1] )">
        <func:result select="$node/dct:alternative[@xml:lang=$langCode][1]"/>
      </xsl:when>
      <!-- skos:prefLabel with no specified language -->
      <xsl:when test="normalize-space(
                        $node/skos:prefLabel[not(@xml:lang)] )">
        <func:result select="$node/skos:prefLabel[not(@xml:lang)]"/>
      </xsl:when>
      <!-- dct:title with no specified language -->
      <xsl:when test="normalize-space(
                        $node/dct:title[not(@xml:lang)] )">
        <func:result select="$node/dct:title[not(@xml:lang)]"/>
      </xsl:when>
      <!-- first skos:altLabel with no specified language -->
      <xsl:when test="normalize-space(
                        $node/skos:altLabel[not(@xml:lang)][1] )">
        <func:result select="$nodeskos:altLabel[not(@xml:lang)][1]"/>
      </xsl:when>
      <!-- first dct:alternative with no specified language -->
      <xsl:when test="normalize-space(
                        $node/dct:alternative[not(@xml:lang)][1] )">
        <func:result select="$node/dct:alternative[not(@xml:lang)][1]"/>
      </xsl:when>
      <!-- URI from rdf:about -->
      <xsl:otherwise>
        <func:result select="$node/@rdf:about"/>
      </xsl:otherwise>
    </xsl:choose>
  </func:function>


  <!-- Template that writes inside a HTML table the properties that describe
       the Concept Schemes and the Concepts alongside their values. Only the
       properties with a value are written.

       This template is called by the template that transforms the
       <rdf:Description> elements describing a Concept (cf. "htmlConcept" mode).

       The properties to be written are described, in the desired order, in the
       following <elid:display-properties> element. Therefore, not all the
       properties will be displayed. These properties can be found in the
       global "displayProps" variable.

       This template creates a table row (<tr>) for each existing property and
       inserts in the first cell the translation of the property name in the
       chosen language and in the second cell the value or the values of
       this property. The value can be a URI towards other resource (cf.
       rdf:resource attribute on the property element in the source XML) or a
       textual value (eventually with a language specification). If the URI
       is the URI of another resource described on this page (Concept or
       Concept Scheme), an internal link is inserted.

       The "node" parameter contains the <rdf:Description> element that
       contains all the properties about the current Concept or Concept Scheme.
       The "langCode" parameter contains the code of the chosen language (two
       letters code). -->
  <xsl:template name="writeAllProperties">
    <xsl:param name="node" select="."/>
    <xsl:param name="langCode"/>
    <xsl:param name="currentSchemeURI" select="''"/>

    <!-- Loops on all the properties defined in the  <elid:display-properties>
         element. -->
    <xsl:for-each select="$displayProps">

      <xsl:variable name="currProp" select="."/>

      <!-- The following for-each is just used to go back in the main XML
           document and therefore be able to use the XSL keys for the
           selections in the "writeProperty" template. -->
      <xsl:for-each select="$node[1]">

        <!-- Writes the property in the HTML table if it has one or more
             values. -->
        <xsl:call-template name="writeProperty">
          <xsl:with-param name="node" select="$node"/>
          <xsl:with-param name="currProp" select="$currProp"/>
          <xsl:with-param name="langCode" select="$langCode"/>
          <xsl:with-param name="currentSchemeURI" select="$currentSchemeURI"/>
        </xsl:call-template>

      </xsl:for-each>

    </xsl:for-each>
  </xsl:template>


  <!-- Template that writes inside a HTML table the row corresponding to one
       of the properties that describe the Concept Schemes and the Concepts.

       This template is called by the "writeAllProperties" template for
       each of the properties described in the following
       <elid:display-properties> element (available in the global
       "displayProps" variable), or can be directly called for
       one of the <elid:property> found in the global "displayProps" variable.

       This template creates a table row (<tr>) for the property if it exists
       and have one or several values. It inserts in the first cell the
       translation of the property name in the chosen language and in the
       second cell the value or the values of this property. The value can be
       a URI towards other resource (cf. rdf:resource attribute on the
       property element in the source XML) or a textual value (eventually with
       a language specification). If the URI is the URI of another resource
       described on this page (Concept or Concept Scheme), an internal link is
       inserted.

       The "node" parameter contains the <rdf:Description> element that
       contains all the properties about the current Concept or Concept Scheme.
       The "prop" parameter contains the <elid:property> element read inside
       this stylesheet (they are in the global "displayProps" variable).
       The "langCode" parameter contains the code of the chosen language (two
       letters code). -->
  <xsl:template name="writeProperty">
    <xsl:param name="node" select="empty[not(self::empty)]"/>
    <xsl:param name="nodeURI" select="$node/@rdf:about"/>
    <xsl:param name="currProp" select="empty[not(self::empty)]"/>
    <xsl:param name="langCode"/>
    <xsl:param name="currentSchemeURI" select="''"/>

    <!-- All the XML elements inside <rdf:Description> whose name is the
         name of the current property. -->
    <xsl:variable name="directNodes"
                  select="$node/*[
                            concat(namespace-uri(),local-name())
                            = $currProp/@name
                          ]"/>
    <!-- From these XML property elements, all the textual values of the
         XML elements associated to the chosen language. -->
    <xsl:variable name="langTexts"
                  select="$directNodes[
                            not(@rdf:resource) and @xml:lang = $langCode
                          ]/text()"/>
    <!-- From these XML property elements, all the textual values of the
         XML elements that are not associated to any language. -->
    <xsl:variable name="noLangTexts"
                  select="$directNodes[
                            not(@rdf:resource) and not(@xml:lang)
                          ]/text()"/>
    <!-- From these XML property elements, all the URIs of the XML elements
         that points towards a resource. -->
    <xsl:variable name="resourceURIs"
                  select="$directNodes[
                            @rdf:resource
                          ]/@rdf:resource"/>
    <!-- Inside the same <rdf:Description>, all the URIs of the XML
         property elements whose name is the name of a derived property of
         the current property. -->
    <xsl:variable name="derivedResourceURIs"
                  select="$node/*[
                            concat(namespace-uri(),local-name())
                            = $currProp/elid:sub-property/@name
                          ]/@rdf:resource"/>
    <!-- All the URIs of other <rdf:Description> that have an XML property
         containing the URI of the current node and whose name is the name
         of an inverse property of the current property.
         Here, we use the 'rdfDescInverse' XSL key to optimize the search
         of the other <rdf:Description> pointing towards the current
         node. -->
    <xsl:variable name="inverseResourceURIs"
                  select="key('rdfDescInverse', $nodeURI)[
                            *[ concat(namespace-uri(),local-name())
                               = $currProp/elid:inverse-property/@name ]
                             [ @rdf:resource = $nodeURI ]
                           ]/@rdf:about"/>
    <!-- Local resources associated to the URIs gathered above. A local
         resource is another <rdf:Description> element defined in the source
         XML.
         Here, we use the 'rdfDesc' XSL key to optimize the search of the
         resources corresponding to the URIs. -->
    <xsl:variable name="localResources"
                  select="key('rdfDesc',
                                $resourceURIs | $derivedResourceURIs
                              | $inverseResourceURIs )"/>
    <!-- All the other URIs that don't correspond to local resources. -->
    <xsl:variable name="otherURIs"
                  select="(  $resourceURIs | $derivedResourceURIs
                           | $inverseResourceURIs)[
                            not($localResources/@rdf:about = .)
                          ]"/>
    <!-- Tests if we have any value for the current property-->
    <xsl:if test="$langTexts | $noLangTexts | $localResources | $otherURIs">
      <tr>
        <!-- Translated name of the property -->
        <th>
          <xsl:call-template name="translate">
            <xsl:with-param name="term" select="$currProp/@name"/>
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
        </th>
        <!-- Values of the property -->
        <td>
          <!-- All textual values associated to the chosen language. -->
          <xsl:for-each select="$langTexts">

            <xsl:if test="position() != 1">
              <xsl:text>, </xsl:text>
            </xsl:if>

            <xsl:value-of select="."/>
          </xsl:for-each>
          <!-- If no language textual value exist, all textual values
               not associated with any language. -->
          <xsl:if test="not($langTexts)">
            <xsl:for-each select="$noLangTexts">

              <xsl:if test="position() != 1">
                <xsl:text>, </xsl:text>
              </xsl:if>

              <xsl:value-of select="."/>

            </xsl:for-each>
          </xsl:if>
          <!-- The names of the local resources with an internal link
               towards them.
               If possible (extension available), we use the customized
               elixt:concept-name function to sort the <rdf:Description>
               corresponding to the Concepts, else we use several sorting
               keys (but the resulting sorting is not correct if all the
               Concept don't use the same sorting key).
          -->
          <xsl:choose>
            <xsl:when test="function-available('elixt:concept-name')">

              <xsl:for-each select="$localResources">
                <xsl:sort select="elixt:concept-name(.,$langCode)"/>

                <xsl:if test="position() != 1 or $langTexts|$noLangTexts">
                  <xsl:text>, </xsl:text>
                </xsl:if>

                <xsl:apply-templates select="." mode="resourceName">
                  <xsl:with-param name="langCode" select="$langCode"/>
                  <xsl:with-param name="insertLink" select="1"/>
                  <xsl:with-param name="currentSchemeURI" select="$currentSchemeURI"/>
                </xsl:apply-templates>
              </xsl:for-each>

            </xsl:when>
            <xsl:otherwise>

              <xsl:for-each select="$localResources">
                <xsl:sort select="skos:prefLabel[@xml:lang=$langCode]"/>
                <xsl:sort select="dct:title[@xml:lang=$langCode]"/>
                <xsl:sort select="skos:altLabel[@xml:lang=$langCode][1]"/>
                <xsl:sort select="dct:alternative[@xml:lang=$langCode][1]"/>
                <xsl:sort select="skos:prefLabel[not(@xml:lang)]"/>
                <xsl:sort select="dct:title[not(@xml:lang)]"/>
                <xsl:sort select="skos:altLabel[not(@xml:lang)][1]"/>
                <xsl:sort select="dct:alternative[not(@xml:lang)][1]"/>
                <xsl:sort select="@rdf:about"/>

                <xsl:if test="position() != 1 or $langTexts|$noLangTexts">
                  <xsl:text>, </xsl:text>
                </xsl:if>

                <xsl:apply-templates select="." mode="resourceName">
                  <xsl:with-param name="langCode" select="$langCode"/>
                  <xsl:with-param name="insertLink" select="1"/>
                  <xsl:with-param name="currentSchemeURI" select="$currentSchemeURI"/>
                </xsl:apply-templates>
              </xsl:for-each>

            </xsl:otherwise>
          </xsl:choose>
          <!-- Finally, the URIs towards other resources.

               We call the "translate" template in case the URI
               corresponds to a term that exists in one of the glossary
               (if not, the URI will be written). -->
          <xsl:for-each select="$otherURIs">

            <xsl:if test="position() != 1
                          or $langTexts | $noLangTexts | $localResources">
              <xsl:text>, </xsl:text>
            </xsl:if>

            <a href="{.}">
              <xsl:call-template name="translate">
                <xsl:with-param name="term" select="."/>
                <xsl:with-param name="langCode" select="$langCode"/>
              </xsl:call-template>
            </a>

          </xsl:for-each>

        </td>
      </tr>
    </xsl:if>
  </xsl:template>


  <!-- This element contains all the properties we want to display to describe
       the Concept Schemes and the Concepts. These properties are XML children
       of the <rdf:Description> element and contains either textual data or
       an rdf:resource attribute pointing towards another resource.

       The properties are given in the order in which they will appear in the
       HTML (the identifiers, then the titles, then the notes, etc.)

       For some properties (cf. narrower/broader), we must gather the
       values for the actual property and from the inverse property that might
       point onto the current resource. In such situations, the name of the
       inverse properties are given below inside the property.

       For some properties (cf. inScheme), we must gather the values from
       the actual property and from other properties that derive from this
       one. In such situations, the name of the inverse properties are given
       below inside the property.

       Cf. "writeProperties" template that will process the <elid:property>
       elements.  -->
  <elid:display-properties>
    <elid:property name="&skos;notation"/>
    <elid:property name="&dct;identifier"/>
    <elid:property name="&euvoc;status"/>
    <elid:property name="&skos;prefLabel"/>
    <elid:property name="&dct;title"/>
    <elid:property name="&skos;altLabel"/>
    <elid:property name="&dct;alternative"/>
    <elid:property name="&skos;hiddenLabel"/>
    <elid:property name="&skos;definition"/>
    <elid:property name="&skos;scopeNote"/>
    <elid:property name="&skos;editorialNote"/>
    <elid:property name="&skos;historyNote"/>
    <elid:property name="&skos;changeNote"/>
    <elid:property name="&skos;note"/>
    <elid:property name="&skos;example"/>
    <elid:property name="&dct;abstract"/>
    <elid:property name="&dct;description"/>
    <elid:property name="&dct;subject"/>
    <elid:property name="&euvoc;domain"/>
    <elid:property name="&dct;audience"/>
    <elid:property name="&dct;educationLevel"/>
    <elid:property name="&dct;instructionalMethod"/>
    <elid:property name="&dct;coverage"/>
    <elid:property name="&dct;spatial"/>
    <elid:property name="&dct;temporal"/>
    <elid:property name="&dct;language"/>
    <elid:property name="&dct;type"/>
    <elid:property name="&dct;format"/>
    <elid:property name="&dct;medium"/>
    <elid:property name="&dct;extent"/>
    <elid:property name="&euvoc;downloadURL"/>
    <elid:property name="&dct;rights"/>
    <elid:property name="&dct;rightsHolder"/>
    <elid:property name="&dct;accessRights"/>
    <elid:property name="&dct;license"/>
    <elid:property name="&euvoc;license"/>
    <elid:property name="&euvoc;startDate"/>
    <elid:property name="&euvoc;endDate"/>
    <elid:property name="&dct;created"/>
    <elid:property name="&dct;issued"/>
    <elid:property name="&dct;modified"/>
    <elid:property name="&dct;dateSubmitted"/>
    <elid:property name="&dct;dateAccepted"/>
    <elid:property name="&dct;dateCopyrighted"/>
    <elid:property name="&dct;available"/>
    <elid:property name="&dct;valid"/>
    <elid:property name="&dct;date"/>
    <elid:property name="&dct;creator"/>
    <elid:property name="&dct;contributor"/>
    <elid:property name="&euvoc;contributor"/>
    <elid:property name="&dct;publisher"/>
    <elid:property name="&dct;mediator"/>
    <elid:property name="&dct;provenance"/>
    <elid:property name="&euvoc;positionStatus"/>
    <elid:property name="&euvoc;positionComplement"/>
    <elid:property name="&euvoc;officialGivenName"/>
    <elid:property name="&euvoc;officialBirthName"/>
    <elid:property name="&euvoc;officialFamilyName"/>
    <elid:property name="&euvoc;officeAddress"/>
    <elid:property name="&euvoc;localityCode"/>
    <elid:property name="&euvoc;countryCode"/>
    <elid:property name="&euvoc;inhabitantNameForm"/>
    <elid:property name="&euvoc;protocolLevel"/>
    <elid:property name="&euvoc;represents"/>
    <elid:property name="&euvoc;roleQualification"/>
    <elid:property name="&euvoc;reportsTo"/>
    <elid:property name="&euvoc;getsReportingFrom"/>
    <elid:property name="&skos;related">
      <elid:inverse-property name="&skos;related"/>
    </elid:property>
    <elid:property name="&skos;broader">
      <elid:inverse-property name="&skos;narrower"/>
    </elid:property>
    <elid:property name="&skos;narrower">
      <elid:inverse-property name="&skos;broader"/>
    </elid:property>
    <elid:property name="&skos;exactMatch"/>
    <elid:property name="&skos;closeMatch"/>
    <elid:property name="&skos;relatedMatch"/>
    <elid:property name="&skos;broadMatch"/>
    <elid:property name="&skos;narrowMatch"/>
    <elid:property name="&skos;inScheme">
      <elid:sub-property name="&skos;topConceptOf"/>
      <!-- below is the inverse sub-property-->
      <elid:inverse-property name="&skos;hasTopConcept"/>
    </elid:property>
    <elid:property name="&skos;topConceptOf">
      <elid:inverse-property name="&skos;hasTopConcept"/>
    </elid:property>
    <elid:property name="&skos;hasTopConcept">
      <elid:inverse-property name="&skos;topConceptOf"/>
    </elid:property>
    <elid:property name="&elis;hasConcept">
      <!-- Inverse property of skos:inScheme that gives, for a Concept Scheme,
           all the Concepts that exist in this scheme. -->
      <elid:sub-property name="&skos;hasTopConcept"/>
      <elid:inverse-property name="&skos;inScheme"/>
      <elid:inverse-property name="&skos;topConceptOf"/>
    </elid:property>
    <elid:property name="&dct;hasPart"/>
    <elid:property name="&dct;isPartOf"/>
    <elid:property name="&dct;hasVersion"/>
    <elid:property name="&dct;isVersionOf"/>
    <elid:property name="&dct;tableOfContents"/>
    <elid:property name="&dct;hasFormat"/>
    <elid:property name="&dct;isFormatOf"/>
    <elid:property name="&dct;conformsTo"/>
    <elid:property name="&dct;source"/>
    <elid:property name="&dct;requires"/>
    <elid:property name="&dct;isRequiredBy"/>
    <elid:property name="&dct;replaces"/>
    <elid:property name="&dct;isReplacedBy"/>
    <elid:property name="&dct;references"/>
    <elid:property name="&dct;isReferencedBy"/>
    <elid:property name="&dct;relation"/>
    <elid:property name="&dct;bibliographicCitation"/>
  </elid:display-properties>

</xsl:stylesheet>
