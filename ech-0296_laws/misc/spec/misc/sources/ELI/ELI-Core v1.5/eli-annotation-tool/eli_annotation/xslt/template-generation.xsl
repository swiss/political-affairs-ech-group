<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                version="1.0"
                xmlns:elit="urn:eli:annotation-tool:template:"
                xmlns:elid="urn:eli:annotation-tool:data:"
                xmlns:exsl="http://exslt.org/common"
                extension-element-prefixes="exsl"
                exclude-result-prefixes="elit elid">

  <!-- Global variable containing the code of the chosen language for the HTML
       output pages (2 letters code). -->
  <xsl:variable name="lang" select="'en'"/>
  <!-- Global variable controlling the type of output to be produced.
       When set to "alone", only outputs the HTML content inside a <div>;
       When set to "none", only outputs an HTML page with the RDFa and the
       Schema.Org properties in the HTML header (and nothing in the body);
       When set to "whole-page", output a whole HTML page with the HTML content
       in the body, the RDFa properties and the Schema.Org properties in the
       header. -->
  <xsl:variable name="htmlContent" select="'whole-page'"/>
  <!-- Global variable indicating if the HTML files produced by the XSLT must
       be saved thanks to the exsl:document extension or should just be
       inserted inside a <elid:file> element. -->
  <xsl:variable name="saveHtmlFiles" select="'yes'"/>
  <!-- Global variable containing the XHTML template used to build the output
       page. This template is in the template.xhtml page and contains HTML
       tags and specific commands to insert the HTML content, the RDFa tags,
       the title, etc.-->
  <xsl:variable name="template" select="document('template.xhtml')"/>


  <!-- Main template starting the transformation on the root node of the source
       XML file (e.g. SKOS vocabulary or ELI notice).

       When "htmlContent" global variable is set to "alone", this template
       calls the "insert.html.content" template to generate the HTML content.
       Otherwise, this template starts the transformation of the XHTML template
       found in the "template" global variable in "templateGeneration" mode. -->
  <xsl:template match="/">

    <!-- Applies the template defined for the root element of the source XML
         (e.g. SKOS vocabulary or ELI notice).

         Inside this template, the create.html.file template will be called
         each time we want to create a new HTML file. -->
    <xsl:choose>
      <xsl:when test="$htmlContent = 'alone'">
        <div class="elid_root">
          <xsl:apply-templates select="*"/>
        </div>
      </xsl:when>
      <xsl:otherwise>
        <elid:root>
          <xsl:apply-templates select="*"/>
        </elid:root>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>


  <xsl:template name="create.html.file">
    <xsl:param name="filename" select="'file.html'"/>
    <xsl:param name="nodeId" select="''"/>
    <xsl:param name="data" select="empty[not(self::empty)]"/>
    <xsl:param name="langCode" select="$lang"/>
    <xsl:param name="htmlInsertionMode" select="$htmlContent"/>

    <xsl:choose>
      <xsl:when test="$htmlInsertionMode = 'alone'">
        <div class="file" data-filename="{$filename}" data-node-id="{$nodeId}">
          <!-- The following for-each is used to set the current node to the
               root of the source XML (in the "data" global variable). -->
          <xsl:for-each select="$data">
            <!-- Calls the "insert.html.content" to generate the HTML content
                 for the source XML. -->
            <xsl:call-template name="insert.html.content">
              <xsl:with-param name="langCode" select="$langCode"/>
            </xsl:call-template>
          </xsl:for-each>
        </div>
      </xsl:when>
      <xsl:when test="$saveHtmlFiles = 'yes'">
        <elid:file filename="{$filename}" node-id="{$nodeId}"/>
        <!-- Opens a new file and outputs all the produced elements inside
             this new file. -->
        <exsl:document href="{$filename}" method="html" version="5.0"
                       encoding="UTF-8">
          <!-- Starts the processing of the XHTML template.
               The XHTML template is in the "template" global variable. -->
          <xsl:apply-templates select="$template" mode="templateGeneration">
            <xsl:with-param name="data" select="$data"/>
            <xsl:with-param name="langCode" select="$langCode"/>
            <xsl:with-param name="htmlInsertionMode"
                            select="$htmlInsertionMode"/>
          </xsl:apply-templates>
        </exsl:document>
      </xsl:when>
      <xsl:otherwise>
        <elid:file filename="{$filename}" node-id="{$nodeId}">
          <!-- Starts the processing of the XHTML template.
               The XHTML template is in the "template" global variable. -->
          <xsl:apply-templates select="$template" mode="templateGeneration">
            <xsl:with-param name="data" select="$data"/>
            <xsl:with-param name="langCode" select="$langCode"/>
            <xsl:with-param name="htmlInsertionMode"
                            select="$htmlInsertionMode"/>
         </xsl:apply-templates>
        </elid:file>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>


  <!-- Template dedicated to the XHTML template transformation, for the root
       of the XHTML template (cf. "template" global variable).

       HTML tags from the template are just copied to the output; commands
       represented by tags in the "elit" namespace are executed to insert
       title, language, content, etc.

       Starts the XHTML template transformation for the children of the
       template tree root. -->
  <xsl:template match="/" mode="templateGeneration">
    <xsl:param name="data"/>
    <xsl:param name="langCode"/>
    <xsl:param name="htmlInsertionMode" select="$htmlContent"/>

    <xsl:apply-templates select="node()" mode="templateGeneration">
      <xsl:with-param name="data" select="$data"/>
      <xsl:with-param name="langCode" select="$langCode"/>
      <xsl:with-param name="htmlInsertionMode" select="$htmlInsertionMode"/>
    </xsl:apply-templates>
  </xsl:template>

  <!-- Template dedicated to the XHTML template transformation, for the XML
       elements (default behaviour).

       Copies the element and its attributes, keeps on the XHTML template
       transformation for the children. -->
  <xsl:template match="*" mode="templateGeneration">
    <xsl:param name="data"/>
    <xsl:param name="langCode"/>
    <xsl:param name="htmlInsertionMode" select="$htmlContent"/>

    <xsl:element name="{name()}">
      <xsl:copy-of select="@*"/>
      <xsl:apply-templates select="elit:create-attribute"
                           mode="templateGeneration">
        <xsl:with-param name="data" select="$data"/>
        <xsl:with-param name="langCode" select="$langCode"/>
        <xsl:with-param name="htmlInsertionMode" select="$htmlInsertionMode"/>
      </xsl:apply-templates>
      <xsl:apply-templates select="node()[not(self::elit:create-attribute)]"
                           mode="templateGeneration">
        <xsl:with-param name="data" select="$data"/>
        <xsl:with-param name="langCode" select="$langCode"/>
        <xsl:with-param name="htmlInsertionMode" select="$htmlInsertionMode"/>
      </xsl:apply-templates>
    </xsl:element>
  </xsl:template>

  <!-- Template dedicated to the XHTML template transformation, for the text
       nodes, the comments, the processing instructions.

       Copies the item. -->
  <xsl:template match="text()|comment()|processing-instruction()"
                mode="templateGeneration">
    <xsl:param name="data"/>
    <xsl:param name="langCode"/>
    <xsl:param name="htmlInsertionMode" select="$htmlContent"/>

    <xsl:copy-of select="."/>
  </xsl:template>

  <!-- Template dedicated to the XHTML template transformation, for the
       create-attribute command.

       Creates the XML attribute, keeps on the XHTML template
       transformation for the children (actually copying a text or inserting
       an item such as the language or the title). -->
  <xsl:template match="elit:create-attribute" mode="templateGeneration">
    <xsl:param name="data"/>
    <xsl:param name="langCode"/>
    <xsl:param name="htmlInsertionMode" select="$htmlContent"/>

    <xsl:attribute name="{current()/@name}">
      <xsl:apply-templates select="node()" mode="templateGeneration">
        <xsl:with-param name="data" select="$data"/>
        <xsl:with-param name="langCode" select="$langCode"/>
        <xsl:with-param name="htmlInsertionMode" select="$htmlInsertionMode"/>
      </xsl:apply-templates>
    </xsl:attribute>
  </xsl:template>

  <!-- Template dedicated to the XHTML template transformation, for the
       insert-content command.

       Depending on the type on content to be inserted (RDF-a, Schema.Org,
       HTML), calls the "insert.XX.content" template. If the "htmlContent"
       global variable is set to "none", the insertion of the HTML content
       is skipped.
  -->
  <xsl:template match="elit:insert-content" mode="templateGeneration">
    <xsl:param name="data"/>
    <xsl:param name="langCode"/>
    <xsl:param name="htmlInsertionMode" select="$htmlContent"/>

    <xsl:choose>
      <xsl:when test="@type='html' and $htmlInsertionMode != 'none'">
        <!-- The following for-each is used to set the current node to the
             root of the source XML (in the "data" global variable). -->
        <xsl:for-each select="$data">
          <!-- Calls the "insert.html.content" to generate the HTML content
               for the source XML. -->
          <xsl:call-template name="insert.html.content">
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
        </xsl:for-each>
      </xsl:when>
      <xsl:when test="@type='rdfa'">
        <!-- The following for-each is used to set the current node to the
             root of the source XML (in the "data" global variable). -->
        <xsl:for-each select="$data">
          <!-- Calls the "insert.rdfa.content" to generate the RDF-a content
               for the source XML. -->
          <xsl:call-template name="insert.rdfa.content">
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
        </xsl:for-each>
      </xsl:when>
      <xsl:when test="@type='schema-org'">
        <!-- The following for-each is used to set the current node to the
             root of the source XML (in the "data" global variable). -->
        <xsl:for-each select="$data">
          <!-- Calls the "insert.html.content" to generate the Schema.Org
               content for the source XML. -->
          <xsl:call-template name="insert.schema-org.content">
            <xsl:with-param name="langCode" select="$langCode"/>
          </xsl:call-template>
        </xsl:for-each>
      </xsl:when>
    </xsl:choose>
  </xsl:template>

  <!-- Template dedicated to the XHTML template transformation, for the
       insert-title command.

       Calls the "insert.title" template that will output the title. -->
  <xsl:template match="elit:insert-title" mode="templateGeneration">
    <xsl:param name="data"/>
    <xsl:param name="langCode"/>
    <xsl:param name="htmlInsertionMode" select="$htmlContent"/>

    <xsl:for-each select="$data">
      <xsl:call-template name="insert.title">
        <xsl:with-param name="langCode" select="$langCode"/>
      </xsl:call-template>
    </xsl:for-each>
  </xsl:template>

  <!-- Template dedicated to the XHTML template transformation, for the
       insert-title command.

       Calls the "insert.lang" template that will output the language. -->
  <xsl:template match="elit:insert-lang" mode="templateGeneration">
    <xsl:param name="data"/>
    <xsl:param name="langCode"/>
    <xsl:param name="htmlInsertionMode" select="$htmlContent"/>

    <xsl:for-each select="$data">
      <xsl:call-template name="insert.lang">
        <xsl:with-param name="langCode" select="$langCode"/>
      </xsl:call-template>
    </xsl:for-each>
  </xsl:template>


  <!-- Template that inserts the HTML content inside the HTML body of the
       page.

       This template can be called either by the main template to only output
       the HTML content ("onlyHTMLcontent" global variable set to 1), or by
       the templates in the "templateGeneration" mode ("onlyHTMLcontent" global
       variable set to 0, insertion inside the page and the XHTML tags). -->
  <xsl:template name="insert.html.content">
    <xsl:param name="langCode"/>

  </xsl:template>

  <!-- Template that inserts the tags for describing the RDFa content.

       These HTML tags are inserted inside the HTML header. -->
  <xsl:template name="insert.rdfa.content">
    <xsl:param name="langCode"/>

  </xsl:template>

  <!-- Template that inserts the tags for describing the Schema.Org content.

       These HTML tags are inserted inside the HTML header. -->
  <xsl:template name="insert.schema-org.content">
    <xsl:param name="langCode"/>

  </xsl:template>

  <!-- Template that inserts the title (string). -->
  <xsl:template name="insert.title">
    <xsl:param name="langCode"/>

  </xsl:template>

  <!-- Template that inserts the language code (from the "lang" global
       variable). -->
  <xsl:template name="insert.lang">
    <xsl:param name="langCode"/>
    <xsl:param name="htmlInsertionMode" select="$htmlContent"/>

    <xsl:value-of select="$langCode"/>
  </xsl:template>

</xsl:stylesheet>
