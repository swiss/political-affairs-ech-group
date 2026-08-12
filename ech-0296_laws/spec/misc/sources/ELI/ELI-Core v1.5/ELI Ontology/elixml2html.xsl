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
		<html prefix="eli: http://data.europa.eu/eli/ontology#, rdfs: http://www.w3.org/2000/01/rdf-schema#">
			<head>
				<style>
					.LegalResource {
					
					}
					
					.LegalExpression {
						margin-left:1.5em;
						margin-top:1em;
					}
					
					.Format {
						margin-left:3em;
						margin-top:0.5em;
					}
				</style>
			</head>
			<body>
				<xsl:apply-templates />
			</body>			
		</html>
	</xsl:template>
	
	<xsl:template match="eli:LegalResource">
		<div typeof="eli:LegalResource" class="LegalResource" resource="{@eli:URI}">
			<!-- process the eli:in_force attribute -->
			<xsl:if test="@eli:in_force">
				<div>eli:in_force : <span property="eli:in_force" resource="http://data.europa.eu/eli/ontology#{@eli:in_force}"><xsl:value-of select="@eli:in_force" /></span></div>
			</xsl:if>
			
			<!-- process the eli:uri_schema attribute -->
			<xsl:if test="@eli:uri_schema">
				<div>eli:uri_schema : <span property="eli:uri_schema" resource="{@eli:uri_schema}"><xsl:value-of select="@eli:uri_schema" /></span></div>
			</xsl:if>
			
			<!-- process all property subelements -->
			<xsl:apply-templates select="*[not(local-name()='LegalExpression' or local-name()='LegalResource' or local-name()='LegalResourceSubdivision')]" />
			
			<!-- process all included LegalExpressions -->
			<xsl:for-each select="eli:LegalExpression">
				<div property="eli:is_realized_by">
					<xsl:apply-templates select="." />
				</div>
			</xsl:for-each>
			
			<!-- process all included LegalResource -->
			<xsl:for-each select="eli:LegalResource">
				<div property="eli:has_member">
					<xsl:apply-templates select="." />
				</div>
			</xsl:for-each>
			
			<!-- process all included LegalResourceSubdivision -->
			<xsl:for-each select="eli:LegalResourceSubdivision">
				<div property="eli:has_part">
					<xsl:apply-templates select="." />
				</div>
			</xsl:for-each>
		</div>
		<xsl:comment>End eli:LegalResource <xsl:value-of select="@eli:URI" /></xsl:comment>
	</xsl:template>

	<xsl:template match="eli:LegalResourceSubdivision">
		<div typeof="eli:LegalResourceSubdivision" class="LegalResourceSubdivision" resource="{@eli:URI}">
			<!-- process the eli:in_force attribute -->
			<xsl:if test="@eli:in_force">
				<div>eli:in_force : <span property="eli:in_force" resource="http://data.europa.eu/eli/ontology#{@eli:in_force}"><xsl:value-of select="@eli:in_force" /></span></div>
			</xsl:if>
			
			<!-- process the eli:uri_schema attribute -->
			<xsl:if test="@eli:uri_schema">
				<div>eli:uri_schema : <span property="eli:uri_schema" resource="{@eli:uri_schema}"><xsl:value-of select="@eli:uri_schema" /></span></div>
			</xsl:if>
			
			<!-- process all property subelements -->
			<xsl:apply-templates select="*[not(local-name()='LegalExpression' or local-name()='LegalResource' or local-name()='LegalResourceSubdivision')]" />
			
			<!-- process all included LegalExpressions -->
			<xsl:for-each select="eli:LegalExpression">
				<div property="eli:is_realized_by">
					<xsl:apply-templates select="." />
				</div>
			</xsl:for-each>
			
			<!-- process all included LegalResourceSubdivision -->
			<xsl:for-each select="eli:LegalResourceSubdivision">
				<div property="eli:has_part">
					<xsl:apply-templates select="." />
				</div>
			</xsl:for-each>
		</div>
		<xsl:comment>End eli:LegalResourceSubdivision <xsl:value-of select="@eli:URI" /></xsl:comment>
	</xsl:template>
	
	<xsl:template match="eli:LegalExpression">
		<div typeof="eli:LegalExpression" class="LegalExpression" resource="{@eli:URI}">
		
			<!-- keep current URI in a variable for future reference -->
			<xsl:variable name="legalExpression-URI" select="@eli:URI" />
			
			<!-- process the eli:language attribute -->
			<xsl:if test="@eli:language">
				<xsl:for-each select="tokenize(@eli:language,' ')">
					<div>Expression in language <span property="eli:language" resource="http://publications.europa.eu/resource/authority/language/{.}"><xsl:value-of select="." /></span></div>
				</xsl:for-each>
			</xsl:if>
			
			<!-- process the eli:in_force attribute -->
			<xsl:if test="@eli:in_force">
				<div>eli:in_force : <span property="eli:in_force" resource="http://data.europa.eu/eli/ontology#{@eli:in_force}"><xsl:value-of select="@eli:in_force" /></span></div>
			</xsl:if>
			
			<!-- process the eli:uri_schema attribute -->
			<xsl:if test="@eli:uri_schema">
				<div>eli:uri_schema : <span property="eli:uri_schema" resource="{@eli:uri_schema}"><xsl:value-of select="@eli:uri_schema" /></span></div>
			</xsl:if>
			
			<!-- process all property subelements -->
			<xsl:apply-templates select="*[not(local-name()='Format')]" />
			
			<!-- process all included Format -->
			<xsl:for-each select="eli:Format">
				<div property="eli:is_embodied_by">
					<xsl:apply-templates select="." />
				</div>
			</xsl:for-each>
		</div>
		<xsl:comment>End eli:LegalExpression <xsl:value-of select="@eli:URI" /></xsl:comment>
	</xsl:template>
	
	<xsl:template match="eli:Format">
		<div typeof="eli:Format" class="Format" resource="{@eli:URI}">			
			<!-- process the eli:format attribute -->
			<xsl:if test="@eli:format">
				<div>Format in <span property="eli:format" resource="http://www.iana.org/assignments/media-types/{@eli:format}"><xsl:value-of select="@eli:format" /></span></div>
			</xsl:if>
			
			<!-- process the eli:legal_value attribute -->
			<xsl:if test="@eli:legal_value">
				<div>eli:legal_value : <span property="eli:legal_value" resource="http://data.europa.eu/eli/ontology#{@eli:legal_value}"><xsl:value-of select="@eli:legal_value" /></span></div>
			</xsl:if>
			
			<!-- process the eli:uri_schema attribute -->
			<xsl:if test="@eli:uri_schema">
				<div>eli:uri_schema : <span property="eli:uri_schema" resource="{@eli:uri_schema}"><xsl:value-of select="@eli:uri_schema" /></span></div>
			</xsl:if>
			
			<!-- process all property subelements -->
			<xsl:apply-templates />
		</div>
		<xsl:comment>End eli:Format <xsl:value-of select="@eli:URI" /></xsl:comment>
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
			<xsl:with-param name="datatype">http://www.w3.org/2001/XMLSchema#string</xsl:with-param>
		</xsl:call-template>
	</xsl:template>
	
	<xsl:template name="rdfResource">
		<xsl:param name="element" />		
		
		<div class="property-{$element}"><xsl:value-of select="$element" /> :
		
		<span property="{$element}">
			<xsl:choose>
				<xsl:when test="starts-with(@eli:URI,'http')">
					<xsl:choose>
						<xsl:when test="eli:display">
							<xsl:attribute name="resource"><xsl:value-of select="@eli:URI" /></xsl:attribute>
							<xsl:apply-templates select="eli:display" />
						</xsl:when>
						<xsl:otherwise>
							<xsl:attribute name="resource"><xsl:value-of select="@eli:URI" /></xsl:attribute>
							<!-- use URI as default text -->
							<span><xsl:value-of select="@eli:URI" /></span>
						</xsl:otherwise>
					</xsl:choose>				
				</xsl:when>
				<xsl:otherwise>
					<xsl:message>Warning : in <xsl:value-of select="$element" />, expected a value starting with 'http', but found '<xsl:value-of select="@eli:URI" />'</xsl:message>
				</xsl:otherwise>
			</xsl:choose>
		</span>
		
		</div>
	</xsl:template>
	
	<xsl:template match="eli:display">
		<span property="rdfs:label">
			<xsl:if test="@xml:lang">
				<xsl:attribute name="lang"><xsl:value-of select="@xml:lang" /></xsl:attribute>
			</xsl:if>
			<xsl:value-of select="text()" />
		</span>
	</xsl:template>
	
	<xsl:template name="textAsLangLiteral">
		<xsl:param name="element" />		
		
		<xsl:choose>
			<xsl:when test="not(starts-with(text(),'http'))">
				<xsl:choose>
					<xsl:when test="@xml:lang">
						<div><xsl:value-of select="$element" /> : <span property="{$element}" content="{@eli:uri_schema}" lang="{@xml:lang}"><xsl:value-of select="text()" /></span></div>
					</xsl:when>
					<xsl:otherwise>
						<div><xsl:value-of select="$element" /> : <span property="{$element}" content="{@eli:uri_schema}"><xsl:value-of select="text()" /></span></div>
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
		<xsl:param name="datatype" />		
		
		<xsl:choose>
			<xsl:when test="not(starts-with(text(),'http'))">
				<div><xsl:value-of select="$element" /> : <span property="{$element}" content="{@eli:uri_schema}" datatype="{$datatype}"><xsl:value-of select="text()" /></span></div>
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