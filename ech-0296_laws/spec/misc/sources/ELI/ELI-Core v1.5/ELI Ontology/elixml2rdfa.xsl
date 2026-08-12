<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet 
	version="2.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
	xmlns:eli="http://data.europa.eu/eli/ontology#"
>
	
	<xsl:output indent="yes" method="xml" />
	
	<xsl:template match="/">
		<html prefix="eli: http://data.europa.eu/eli/ontology#">
			<head>
			<xsl:apply-templates />
			</head>
		</html>
	</xsl:template>
	
	<xsl:template match="eli:LegalResource">
		<meta about="{@eli:URI}" typeof="eli:LegalResource" />
		
		<!-- process the eli:in_force attribute -->
		<xsl:if test="@eli:in_force">
			<meta about="{@eli:URI}" property="eli:in_force" resource="http://data.europa.eu/eli/ontology#{@eli:in_force}" />
		</xsl:if>
		
		<!-- process the eli:uri_schema attribute -->
		<xsl:if test="@eli:uri_schema">
			<meta about="{@eli:URI}" property="eli:uri_schema" resource="{@eli:uri_schema}" />
		</xsl:if>
		
		<!-- process all property subelements -->
		<xsl:apply-templates select="*[not(local-name()='LegalExpression' or local-name()='LegalResource' or local-name()='LegalResourceSubdivision')]" />
		
		<!-- keep current URI in a variable for future reference -->
		<xsl:variable name="legalResource-URI" select="@eli:URI" />
		
		<!-- process all included LegalExpressions -->		
		<xsl:for-each select="eli:LegalExpression">
			<meta about="{$legalResource-URI}" property="eli:is_realized_by" resource="{@eli:URI}" />
			<xsl:apply-templates select="." />
		</xsl:for-each>		
		
		<!-- process all included LegalResource -->
		<xsl:for-each select="eli:LegalResource">
			<meta about="{$legalResource-URI}" property="eli:has_member" resource="{@eli:URI}" />
			<xsl:apply-templates select="." />
		</xsl:for-each>
		
		<!-- process all included LegalResourceSubdivision -->
		<xsl:for-each select="eli:LegalResourceSubdivision">
			<meta about="{$legalResource-URI}" property="eli:has_part" resource="{@eli:URI}" />
			<xsl:apply-templates select="." />
		</xsl:for-each>
	</xsl:template>

	<xsl:template match="eli:LegalResourceSubdivision">
		<meta about="{@eli:URI}" typeof="eli:LegalResourceSubdivision" />
	
		<!-- keep current URI in a variable for future reference -->
		<xsl:variable name="legalResourceSubdivision-URI" select="@eli:URI" />
		
		<!-- process the eli:in_force attribute -->
		<xsl:if test="@eli:in_force">
			<meta about="{@eli:URI}" property="eli:in_force" resource="http://data.europa.eu/eli/ontology#{@eli:in_force}" />
		</xsl:if>
		
		<!-- process the eli:uri_schema attribute -->
		<xsl:if test="@eli:uri_schema">
			<meta about="{@eli:URI}" property="eli:uri_schema" resource="{@eli:uri_schema}" />
		</xsl:if>
		
		<!-- process all property subelements -->
		<xsl:apply-templates select="*[not(local-name()='LegalExpression' or local-name()='LegalResource' or local-name()='LegalResourceSubdivision')]" />
		
		<!-- process all included LegalExpressions -->		
		<xsl:for-each select="eli:LegalExpression">
			<meta about="{$legalResourceSubdivision-URI}" property="eli:is_realized_by" resource="{@eli:URI}" />
		</xsl:for-each>
		<xsl:apply-templates select="eli:LegalExpression" />
		
		<!-- process all included LegalResourceSubdivision -->
		<xsl:for-each select="eli:LegalResourceSubdivision">
			<meta about="{$legalResourceSubdivision-URI}" property="eli:has_part" resource="{@eli:URI}" />
		</xsl:for-each>
		<xsl:apply-templates select="eli:LegalResourceSubdivision" />
	</xsl:template>
	
	<xsl:template match="eli:LegalExpression">
		<meta about="{@eli:URI}" typeof="eli:LegalExpression" />
	
		<!-- keep current URI in a variable for future reference -->
		<xsl:variable name="legalExpression-URI" select="@eli:URI" />
		
		<!-- process the eli:in_force attribute -->
		<xsl:if test="@eli:in_force">
			<meta about="{@eli:URI}" property="eli:in_force" resource="http://data.europa.eu/eli/ontology#{@eli:in_force}" />
		</xsl:if>
		
		<!-- process the eli:language attribute -->
		<xsl:if test="@eli:language">
			<xsl:for-each select="tokenize(@eli:language,' ')">
				<meta about="{$legalExpression-URI}" property="eli:language" resource="http://publications.europa.eu/resource/authority/language/{.}" />
			</xsl:for-each>
		</xsl:if>
		
		<!-- process the eli:uri_schema attribute -->
		<xsl:if test="@eli:uri_schema">
			<meta about="{@eli:URI}" property="eli:uri_schema" resource="{@eli:uri_schema}" />
		</xsl:if>
		
		<!-- process all property subelements -->
		<xsl:apply-templates select="*[not(local-name()='Format')]" />
		
		<!-- process all included Format -->
		<xsl:for-each select="eli:Format">
			<meta about="{$legalExpression-URI}" property="eli:is_embodied_by" resource="{@eli:URI}" />
		</xsl:for-each>
		<xsl:apply-templates select="eli:Format" />
	</xsl:template>
	
	<xsl:template match="eli:Format">
		<meta about="{@eli:URI}" typeof="eli:Format" />
		
		<!-- process the eli:format attribute -->
		<xsl:if test="@eli:format">
			<meta about="{@eli:URI}" property="eli:format" resource="http://www.iana.org/assignments/media-types/{@eli:format}" />
		</xsl:if>
		
		<!-- process the eli:legal_value attribute -->
		<xsl:if test="@eli:legal_value">
			<meta about="{@eli:URI}" property="eli:legal_value" resource="http://data.europa.eu/eli/ontology#{@eli:legal_value}" />
		</xsl:if>
		
		<!-- process the eli:uri_schema attribute -->
		<xsl:if test="@eli:uri_schema">
			<meta about="{@eli:URI}" property="eli:uri_schema" resource="{@eli:uri_schema}" />
		</xsl:if>
		
		<!-- process all property subelements -->
		<xsl:apply-templates />
	</xsl:template>
	
	<xsl:template match="
		eli:amended_by |
		eli:amends |
		eli:applied_by |
		eli:applies |
		eli:based_on |
		eli:basis_for |
		eli:changed_by |
		eli:changes |
		eli:cited_by |
		eli:cites |
		eli:commenced_by |
		eli:commences |
		eli:consolidated_by |
		eli:consolidates |
		eli:corrected_by |
		eli:corrects |
		eli:has_another_publication |
		eli:is_about |
		eli:is_another_publication_of |
		eli:jurisdiction |
		eli:passed_by |
		eli:related_to |
		eli:relevant_for |
		eli:repealed_by |
		eli:repeals |
		eli:responsibility_of_agents |
		eli:transposed_by |
		eli:transposes |
		eli:type_document |
		eli:version |
		eli:publisher_agent |
		eli:is_exemplified_by |
		eli:license |
		eli:published_in_format |
		eli:publishes |
		eli:rightsholder_agent
	">
		<xsl:call-template name="rdfResource">
			<xsl:with-param name="element" select="name(.)" />
			<xsl:with-param name="subject" select="../@eli:URI" />
		</xsl:call-template>
	</xsl:template>
	
	<xsl:template match="
		eli:date_document |
		eli:date_publication |
		eli:date_no_longer_in_force |
		eli:date_applicability |
		eli:first_date_entry_in_force |
		eli:version_date
	">
		<xsl:call-template name="textAsTypedLiteral">
			<xsl:with-param name="element" select="name(.)" />
			<xsl:with-param name="subject" select="../@eli:URI" />
			<xsl:with-param name="datatype">http://www.w3.org/2001/XMLSchema#date</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	
	<xsl:template match="
		eli:description |
		eli:id_local |
		eli:number |
		eli:responsibility_of |
		eli:publisher |
		eli:title |
		eli:title_alternative |
		eli:title_short |
		eli:published_in |
		eli:rights |
		eli:rightsholder
	">
		<xsl:call-template name="textAsTypedLiteral">
			<xsl:with-param name="element" select="name(.)" />
			<xsl:with-param name="subject" select="../@eli:URI" />
			<xsl:with-param name="datatype">http://www.w3.org/2001/XMLSchema#string</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	
	<xsl:template name="rdfResource">
		<xsl:param name="element" />
		<xsl:param name="subject" />	
		
		<xsl:choose>
			<xsl:when test="starts-with(@eli:URI,'http')">
				<xsl:choose>
					<xsl:when test="eli:display">
						<meta about="{$subject}" property="{$element}" resource="{@eli:URI}" />
						<meta about="{@eli:URI}" property="rdfs:label" content="{eli:display/text()}" />
					</xsl:when>
					<xsl:otherwise>
						<meta about="{$subject}" property="{$element}" resource="{@eli:URI}" />
					</xsl:otherwise>
				</xsl:choose>	
			</xsl:when>
			<xsl:otherwise>
				<xsl:message>Warning : in <xsl:value-of select="$element" />, expected a value starting with 'http', but found '<xsl:value-of select="@eli:URI" />'</xsl:message>
			</xsl:otherwise>
		</xsl:choose>
	
	</xsl:template>
	
	<xsl:template match="eli:display">
		<!--  Don't do anything -->
	</xsl:template>
	
	<xsl:template name="textAsLangLiteral">
		<xsl:param name="element" />
		<xsl:param name="subject" />	
		
		<xsl:choose>
			<xsl:when test="not(starts-with(text(),'http'))">
				<xsl:choose>
					<xsl:when test="@xml:lang">
						<meta about="{$subject}" property="{$element}" lang="{@xml:lang}" content="{text()}" />
					</xsl:when>
					<xsl:otherwise>
						<meta about="{$subject}" property="{$element}" content="{text()}" />
					</xsl:otherwise>
				</xsl:choose>			
			</xsl:when>
			<xsl:otherwise>
				<xsl:message>Warning : in <xsl:value-of select="$element" />, expected a value NOT starting with 'http', but found '<xsl:value-of select="text()" />'</xsl:message>
			</xsl:otherwise>
		</xsl:choose>
		
	</xsl:template>
	
	<xsl:template name="textAsTypedLiteral">
		<xsl:param name="element" />
		<xsl:param name="subject" />
		<xsl:param name="datatype" />		
		
		<xsl:choose>
			<xsl:when test="not(starts-with(text(),'http'))">
				<meta about="{$subject}" property="{$element}" datatype="{$datatype}" content="{text()}" />		
			</xsl:when>
			<xsl:otherwise>
				<xsl:message>Warning : in <xsl:value-of select="$element" />, expected a value NOT starting with 'http', but found '<xsl:value-of select="text()" />'</xsl:message>
			</xsl:otherwise>
		</xsl:choose>		
	</xsl:template>
	
	<!-- template to match every unmatched elements and not do anything with them -->
	<xsl:template match="*" />
	
	<!-- template to match all unmatched texts and attributes -->
	<xsl:template match="text()|@*"></xsl:template>
	
</xsl:stylesheet>