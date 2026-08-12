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
		<rdf:RDF 
			xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
			xmlns:eli="http://data.europa.eu/eli/ontology#"
		>
			<xsl:apply-templates />
		</rdf:RDF>
	</xsl:template>
	
	<xsl:template match="eli:LegalResource">
		<eli:LegalResource rdf:about="{@eli:URI}">
			<!-- process the eli:in_force attribute -->
			<xsl:if test="@eli:in_force">
				<eli:in_force rdf:resource="http://data.europa.eu/eli/ontology#{@eli:in_force}" />
			</xsl:if>
			
			<!-- process the eli:uri_schema attribute -->
			<xsl:if test="@eli:uri_schema">
				<eli:uri_schema rdf:resource="{@eli:uri_schema}" />
			</xsl:if>
			
			<!-- process all property subelements -->
			<xsl:apply-templates select="*[not(local-name()='LegalExpression' or local-name()='LegalResource' or local-name()='LegalResourceSubdivision')]" />
			
			<!-- process all included LegalExpressions -->
			<xsl:for-each select="eli:LegalExpression">
				<eli:is_realized_by>
					<xsl:apply-templates select="eli:LegalExpression" />
				</eli:is_realized_by>
			</xsl:for-each>
			
			<!-- process all included LegalResource -->
			<xsl:for-each select="eli:LegalResource">
				<eli:has_member>
					<xsl:apply-templates select="eli:LegalResource" />
				</eli:has_member>
			</xsl:for-each>
			
			<!-- process all included LegalResourceSubdivision -->
			<xsl:for-each select="eli:LegalResourceSubdivision">
				<eli:has_part>
					<xsl:apply-templates select="eli:LegalResourceSubdivision" />
				</eli:has_part>
			</xsl:for-each>
		</eli:LegalResource>
	</xsl:template>

	<xsl:template match="eli:LegalResourceSubdivision">
		<eli:LegalResourceSubdivision rdf:about="{@eli:URI}">
			<!-- process the eli:in_force attribute -->
			<xsl:if test="@eli:in_force">
				<eli:in_force rdf:resource="http://data.europa.eu/eli/ontology#{@eli:in_force}" />
			</xsl:if>
			
			<!-- process the eli:uri_schema attribute -->
			<xsl:if test="@eli:uri_schema">
				<eli:uri_schema rdf:resource="{@eli:uri_schema}" />
			</xsl:if>
			
			<!-- process all property subelements -->
			<xsl:apply-templates select="*[not(local-name()='LegalExpression' or local-name()='LegalResource' or local-name()='LegalResourceSubdivision')]" />
			
			<!-- process all included LegalExpressions -->
			<xsl:apply-templates select="eli:LegalExpression" />
			
			<!-- process all included LegalResourceSubdivision -->
			<xsl:apply-templates select="eli:LegalResourceSubdivision" />
		</eli:LegalResourceSubdivision>
	</xsl:template>
	
	<xsl:template match="eli:LegalExpression">
		<eli:LegalExpression rdf:about="{@eli:URI}">				
			<!-- process the eli:in_force attribute -->
			<xsl:if test="@eli:in_force">
				<eli:in_force rdf:resource="http://data.europa.eu/eli/ontology#{@eli:in_force}" />
			</xsl:if>
			
			<!-- process the eli:language attribute -->
			<xsl:if test="@eli:language">
				<xsl:for-each select="tokenize(@eli:language,' ')">
					<eli:language rdf:resource="http://publications.europa.eu/resource/authority/language/{.}" />
				</xsl:for-each>
			</xsl:if>
			
			<!-- process the eli:uri_schema attribute -->
			<xsl:if test="@eli:uri_schema">
				<eli:uri_schema rdf:resource="{@eli:uri_schema}" />
			</xsl:if>
			
			<!-- process all property subelements -->
			<xsl:apply-templates select="*[not(local-name()='Format')]" />
			
			<!-- process all included Format -->
			<xsl:for-each select="eli:Format">
				<eli:is_embodied_by>
					<xsl:apply-templates select="eli:Format" />
				</eli:is_embodied_by>
			</xsl:for-each>
		</eli:LegalExpression>
	</xsl:template>
	
	<xsl:template match="eli:Format">
		<eli:Format rdf:about="{@eli:URI}">				
			<!-- process the eli:format attribute -->
			<xsl:if test="@eli:format">
				<eli:format rdf:resource="http://www.iana.org/assignments/media-types/{@eli:format}" />
			</xsl:if>
			
			<!-- process the eli:legal_value attribute -->
			<xsl:if test="@eli:legal_value">
				<eli:legal_value rdf:resource="http://data.europa.eu/eli/ontology#{@eli:legal_value}" />
			</xsl:if>
			
			<!-- process the eli:uri_schema attribute -->
			<xsl:if test="@eli:uri_schema">
				<eli:uri_schema rdf:resource="{@eli:uri_schema}" />
			</xsl:if>
			
			<!-- process all property subelements -->
			<xsl:apply-templates />
		</eli:Format>
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
		<xsl:call-template name="rdfResource"><xsl:with-param name="element" select="name(.)" /></xsl:call-template>
	</xsl:template>
	
	<xsl:template match="
		eli:date_document |
		eli:date_publication |
		eli:date_no_longer_in_force |
		eli:date_applicability |
		eli:first_date_entry_in_force |
		eli:version_date
	">
		<xsl:call-template name="textAsTypedLiteral"><xsl:with-param name="element" select="name(.)" /><xsl:with-param name="datatype">http://www.w3.org/2001/XMLSchema#date</xsl:with-param></xsl:call-template>
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
		<xsl:call-template name="textAsTypedLiteral"><xsl:with-param name="element" select="name(.)" /><xsl:with-param name="datatype">http://www.w3.org/2001/XMLSchema#string</xsl:with-param></xsl:call-template>
	</xsl:template>
	
	<xsl:template name="rdfResource">
		<xsl:param name="element" />		
		
		<xsl:element name="{$element}">
			<xsl:choose>
				<xsl:when test="starts-with(@eli:URI,'http')">
					<xsl:choose>
						<xsl:when test="eli:display">
							<rdf:Description>
								<xsl:attribute name="rdf:about"><xsl:value-of select="@eli:URI" /></xsl:attribute>
								<xsl:apply-templates select="eli:display" />
							</rdf:Description>
						</xsl:when>
						<xsl:otherwise>
							<xsl:attribute name="rdf:resource"><xsl:value-of select="@eli:URI" /></xsl:attribute>
						</xsl:otherwise>
					</xsl:choose>				
				</xsl:when>
				<xsl:otherwise>
					<xsl:message>Warning : in <xsl:value-of select="$element" />, expected a value starting with 'http', but found '<xsl:value-of select="@eli:URI" />'</xsl:message>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:element>		
	</xsl:template>
	
	<xsl:template match="eli:display">
		<rdfs:label>
			<xsl:if test="@xml:lang">
				<xsl:attribute name="xml:lang"><xsl:value-of select="@xml:lang" /></xsl:attribute>
			</xsl:if>
			<xsl:value-of select="text()" />
		</rdfs:label>
	</xsl:template>
	
	<xsl:template name="textAsLangLiteral">
		<xsl:param name="element" />		
		
		<xsl:element name="{$element}">
			<xsl:choose>
				<xsl:when test="not(starts-with(text(),'http'))">
					<xsl:if test="@xml:lang">
						<xsl:attribute name="xml:lang"><xsl:value-of select="@xml:lang" /></xsl:attribute>
						<xsl:value-of select="text()" />
					</xsl:if>
				</xsl:when>
				<xsl:otherwise>
					<xsl:message>Warning : in <xsl:value-of select="$element" />, expected a value NOT starting with 'http', but found '<xsl:value-of select="text()" />'</xsl:message>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:element>
		
	</xsl:template>
	
	<xsl:template name="textAsTypedLiteral">
		<xsl:param name="element" />
		<xsl:param name="datatype" />		
		
		<xsl:element name="{$element}">
			<xsl:choose>
				<xsl:when test="not(starts-with(text(),'http'))">
					<xsl:attribute name="rdf:datatype"><xsl:value-of select="$datatype" /></xsl:attribute>
					<xsl:value-of select="text()" />
				</xsl:when>
				<xsl:otherwise>
					<xsl:message>Warning : in <xsl:value-of select="$element" />, expected a value NOT starting with 'http', but found '<xsl:value-of select="text()" />'</xsl:message>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:element>
		
	</xsl:template>
	
	<!-- template to match every unmatched elements and not do anything with them -->
	<xsl:template match="*" />
	
	<!-- template to match all unmatched texts and attributes -->
	<xsl:template match="text()|@*"></xsl:template>
	
</xsl:stylesheet>