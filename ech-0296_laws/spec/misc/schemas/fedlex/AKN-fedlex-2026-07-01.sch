<?xml version="1.0" encoding="UTF-8"?>
<schema 
    xmlns:sch="http://purl.oclc.org/dsdl/schematron" 
    xmlns="http://purl.oclc.org/dsdl/schematron" 
    queryBinding="xslt2"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema">
    
    <!--xmlns:fun="urn:com:c-moria:fedlex:schematron:functions"
    xmlns:fedlex="http://fedlex.admin.ch/"-->
    
    
    <ns uri="http://docs.oasis-open.org/legaldocml/ns/akn/3.0" prefix="akn"/>
    <ns uri="http://fedlex.admin.ch/" prefix="fedlex"/>
    <ns uri="urn:com:c-moria:fedlex:schematron:functions" prefix="fun"/>
    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->    
    <!--  Audit Trail -->    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->    
    
    <!-- 2023-12-08: Geert Bormans - initial version -->
    <!-- 2023-12-20: Geert Bormans - rules identifiers added -->
    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->    
    <!--  Document Root Restrictions -->    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->    
    
    <!-- the document root should be "act" -->
    <pattern>
        <rule context="akn:akomaNtoso">
            <assert 
                id="FLX-RT-001"
                test="empty(* except akn:act)"
                >The document root should only contain an act </assert>
        </rule>
    </pattern>

    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->    
    <!--  Preface Restrictions -->    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->    
    
    <!-- the preface should have a docNumber -->
    <pattern>
        <rule context="akn:act/akn:preface">
            <assert
                id="FLX-PF-001"
                test="akn:p/akn:docNumber"
                >Missing docNumber in preface</assert>
        </rule>
    </pattern>
    
    <!-- the preface should have a docTitle -->
    <pattern>
        <rule context="akn:act/akn:preface">
            <assert 
                id="FLX-PF-002"
                test="akn:p/akn:docTitle"
                >Missing docTitle in preface</assert>
        </rule>
    </pattern>
    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->    
    <!--  Body Restrictions -->    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->    
    
    <!-- lists all elements allowed as a top level in an act -->
    <pattern>
        <rule 
            context="akn:act/akn:body/*[not(
            self::akn:book | self::akn:title | self::akn:part |  
            self::akn:chapter | self::akn:subchapter | self::akn:section | self::akn:subsection | 
            self::akn:level | self::akn:article |
            self::akn:transitional | self::akn:proviso 
            )]">
            <report 
                id="FLX-BD-001"
                test="self::*"
                >Illegal element <value-of select="local-name()"/> in body</report>
        </rule>
    </pattern>
    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->    
    <!--  Hierarchical Component Restrictions -->    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->    
     
    <!-- 
     function that actually checks against the allowed hierarchy table in the Fedlex XML specification document 
    -->
    <xsl:function name="fun:is-legal-hier-child" as="xs:boolean">
        <xsl:param name="e"/>
        <xsl:param name="ln"/>
        <xsl:choose>
            <!-- article => always OK -->
            <xsl:when test="$e/self::akn:article"><xsl:sequence select="true()"/></xsl:when>
            <!-- lname = 'body' as first non transparent node in level ancestors => always OK -->
            <xsl:when test="$ln = 'body'"><xsl:sequence select="true()"/></xsl:when>
            <!-- book children -->
            <xsl:when test="$ln = 'book' and $e/self::akn:title"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'book' and $e/self::akn:part"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'book' and $e/self::akn:chapter"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'book' and $e/self::akn:subchapter"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'book' and $e/self::akn:section"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'book' and $e/self::akn:subsection"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'book' and $e/self::akn:level"><xsl:sequence select="true()"/></xsl:when>
            <!-- title children -->
            <xsl:when test="$ln = 'title' and $e/self::akn:book"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'title' and $e/self::akn:part"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'title' and $e/self::akn:chapter"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'title' and $e/self::akn:subchapter"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'title' and $e/self::akn:section"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'title' and $e/self::akn:subsection"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'title' and $e/self::akn:level"><xsl:sequence select="true()"/></xsl:when>
            <!-- part children -->
            <xsl:when test="$ln = 'part' and $e/self::akn:chapter"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'part' and $e/self::akn:subchapter"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'part' and $e/self::akn:section"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'part' and $e/self::akn:subsection"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'part' and $e/self::akn:level"><xsl:sequence select="true()"/></xsl:when>
            <!-- chapter children -->
            <xsl:when test="$ln = 'chapter' and $e/self::akn:subchapter"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'chapter' and $e/self::akn:section"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'chapter' and $e/self::akn:subsection"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'chapter' and $e/self::akn:level"><xsl:sequence select="true()"/></xsl:when>
            <!-- subchapter children -->
            <xsl:when test="$ln = 'subchapter' and $e/self::akn:section"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'subchapter' and $e/self::akn:subsection"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'subchapter' and $e/self::akn:level"><xsl:sequence select="true()"/></xsl:when>
            <!-- section children -->
            <xsl:when test="$ln = 'section' and $e/self::akn:subsection"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$ln = 'section' and $e/self::akn:level"><xsl:sequence select="true()"/></xsl:when>
            <!-- subsection children -->
            <xsl:when test="$ln = 'subsection' and $e/self::akn:level"><xsl:sequence select="true()"/></xsl:when>
            <xsl:otherwise><xsl:sequence select="false()"/></xsl:otherwise>
        </xsl:choose>
        
    </xsl:function>
    
    <!-- 
     function that verifies the element is a valid heading element 
    -->
    <xsl:function name="fun:is-heading-element" as="xs:boolean">
        <xsl:param name="e"/>
        <xsl:choose>
            <xsl:when test="$e/self::akn:num"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$e/self::akn:heading"><xsl:sequence select="true()"/></xsl:when>
            <xsl:when test="$e/self::akn:subheading"><xsl:sequence select="true()"/></xsl:when>
            <xsl:otherwise><xsl:sequence select="false()"/></xsl:otherwise>
        </xsl:choose>
    </xsl:function>
    
    <!-- title has strict rules on what content it can have -->
    <!-- title requires an eId -->
    <pattern>
        <rule context="akn:act/akn:body//akn:title" >
            <let name="lname" value="local-name()"/>
            <assert
                id="FLX-HR-001-ti"
                test="empty( * except (*[(fun:is-heading-element(.))] | *[fun:is-legal-hier-child(., $lname)]) )"
                >Hierarchy mismatch on <value-of select="local-name()"/></assert>

            <report 
                id="FLX-HR-002-ti"
                test="not(@eId)"
                ><value-of select="local-name()"/> needs a unique identifier eId</report>
        </rule>
    </pattern>
    
    <!-- book has strict rules on what content it can have -->
    <!-- book requires an eId -->
    <pattern>
        <rule context="akn:act/akn:body//akn:book" >
            <let name="lname" value="local-name()"/>
            <assert 
                id="FLX-HR-001-bk"
                test="empty( * except (*[(fun:is-heading-element(.))] | *[fun:is-legal-hier-child(., $lname)]) )"
                >Hierarchy mismatch on <value-of select="local-name()"/></assert>

            <report 
                id="FLX-HR-002-bk"
                test="not(@eId)"
                ><value-of select="local-name()"/> needs a unique identifier eId</report>
        </rule>
    </pattern>
    
    <!-- part has strict rules on what content it can have -->
    <!-- part requires an eId -->
    <pattern>
        <rule context="akn:act/akn:body//akn:part" >
            <let name="lname" value="local-name()"/>
            <assert 
                id="FLX-HR-001-pt"
                test="empty( * except (*[(fun:is-heading-element(.))]| *[fun:is-legal-hier-child(., $lname)] ) )"
                >Hierarchy mismatch on <value-of select="local-name()"/></assert>
            
            <report 
                id="FLX-HR-002-pt"
                test="not(@eId)"
                ><value-of select="local-name()"/> needs a unique identifier eId</report>
        </rule>
    </pattern>
    
    <!-- chapter has strict rules on what content it can have -->
    <!-- chapter requires an eId -->
    <pattern>
        <rule context="akn:act/akn:body//akn:chapter" >
            <let name="lname" value="local-name()"/>
            <assert 
                id="FLX-HR-001-ch"
                test="empty( * except (*[(fun:is-heading-element(.))] | *[fun:is-legal-hier-child(., $lname)]) )"
                >Hierarchy mismatch on <value-of select="local-name()"/></assert>
            
            <report 
                id="FLX-HR-002-ch"
                test="not(@eId)"
                ><value-of select="local-name()"/> needs a unique identifier eId</report>
        </rule>
    </pattern>
    
    <!-- subchapter has strict rules on what content it can have -->
    <!-- subchapter requires an eId -->
    <pattern>
        <rule context="akn:act/akn:body//akn:subchapter" >
            <let name="lname" value="local-name()"/>
            <assert 
                id="FLX-HR-001-sh"
                test="empty( * except (*[(fun:is-heading-element(.))] | *[fun:is-legal-hier-child(., $lname)]) )"
                >Hierarchy mismatch on <value-of select="local-name()"/></assert>
            
            <report 
                id="FLX-HR-002-sh"
                test="not(@eId)"
                ><value-of select="local-name()"/> needs a unique identifier eId</report>
        </rule>
    </pattern>
    
    <!-- section has strict rules on what content it can have -->
    <!-- section requires an eId -->
    <pattern>
        <rule context="akn:act/akn:body//akn:section" >
            <let name="lname" value="local-name()"/>
            <assert 
                id="FLX-HR-001-sc"
                test="empty( * except (*[(fun:is-heading-element(.))] | *[fun:is-legal-hier-child(., $lname)]) )"
                >Hierarchy mismatch on <value-of select="local-name()"/></assert>
            
            <report 
                id="FLX-HR-002-sc"
                test="not(@eId)"
                ><value-of select="local-name()"/> needs a unique identifier eId</report>
        </rule>
    </pattern>
    
    <!-- subsection has strict rules on what content it can have -->
    <!-- subsection requires an eId -->
    <pattern>
        <rule context="akn:act/akn:body//akn:subsection" >
            <let name="lname" value="local-name()"/>
            <assert 
                id="FLX-HR-001-ss"
                test="empty( * except (*[(fun:is-heading-element(.))] | *[fun:is-legal-hier-child(., $lname)]) )"
                >Hierarchy mismatch on <value-of select="local-name()"/></assert>
            
            <report 
                id="FLX-HR-002-ss"
                test="not(@eId)"
                ><value-of select="local-name()"/> needs a unique identifier eId</report>
        </rule>
    </pattern>
    
    <!-- level has strict rules on what content it can have -->
    <!-- level requires an eId -->
    <!-- a level is 'transparent' so the local name is the first non-transparent node on the ancestor axis  -->
    <pattern>
        <rule context="akn:act/akn:body//akn:level[not(akn:content)]" >
            <let name="lname" value="ancestor::*[not(local-name() = 'level')][1]/local-name()"/>
            <assert 
                id="FLX-HR-001-lv"
                test="empty( * except (*[(fun:is-heading-element(.))] | *[fun:is-legal-hier-child(., $lname)]) )"
                >Hierarchy mismatch on <value-of select="local-name()"/></assert>
            
            <report 
                id="FLX-HR-002-lv"
                test="not(@eId)"
                ><value-of select="local-name()"/> needs a unique identifier eId</report>
        </rule>
    </pattern>
    
    <!-- level in body can only have content if the content caters for modifications -->
    <!-- level requires an eId -->
    <pattern>
        <rule context="akn:act/akn:body//akn:level[akn:content]" >
            <assert 
                id="FLX-HR-003"
                test="akn:content//akn:mod"
                >content in <value-of select="local-name()"/> only allowed for modifications</assert>
            
            <report 
                id="FLX-HR-004"
                test="not(@eId)"
                ><value-of select="local-name()"/> needs a unique identifier eId</report>
        </rule>
    </pattern>
    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->    
    <!--  Heading Section Restriction -->    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->    
    
    <!-- restrictions on num (num?, heading?, subheading?) -->
    <pattern>
        <rule context="akn:num">
            <report 
                id="FLX-HD-001" 
                test="preceding-sibling::akn:num"
                >A hierarchical component should have a maximum of one <value-of select="local-name()"/></report>
            
            <report 
                id="FLX-HD-002" 
                test="preceding-sibling::akn:heading"
                >If a hierarchical component has both a <value-of select="local-name()"/> and a heading, the num should come first</report>

            <report 
                id="FLX-HD-003" 
                test="preceding-sibling::akn:subheading"
                >If a hierarchical component has both a <value-of select="local-name()"/> and a subheading, the num should come first</report>
        </rule>
    </pattern>
    
    <!-- restrictions on heading (num?, heading?, subheading?) -->
    <pattern>
        <rule context="akn:heading">
            <report 
                id="FLX-HD-004" 
                test="preceding-sibling::akn:heading"
                >A hierarchical component should have a maximum of one <value-of select="local-name()"/></report>
            
            <report 
                id="FLX-HD-005" 
                test="preceding-sibling::akn:subheading"
                >If a hierarchical component has both a <value-of select="local-name()"/> and a subheading, the heading should come first</report>
        </rule>
    </pattern>
    
    <!-- restrictions on subheading (num?, heading?, subheading?) -->
    <pattern>
        <rule context="akn:subheading" >
            <report 
                id="FLX-HD-006"
                test="preceding-sibling::akn:subheading"
                >A hierarchical component should have a maximum of one <value-of select="local-name()"/></report>
        </rule>
    </pattern>
    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->    
    <!--  Article Restriction -->    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->

    <pattern>
        <rule context="akn:article" >
            <!-- in an article num is mandatory -->
            <assert 
                id="FLX-ART-001" 
                test="akn:num"
                >num is mandatory in a <value-of select="local-name()"/></assert>
            
            <!-- in an article only heading elements, paragraphs or subdivisions are allowed -->
            <assert 
                id="FLX-ART-002" 
                test="empty( * except (*[(fun:is-heading-element(.))] | akn:paragraph | akn:subdivision) )"
                >Content not allowed in <value-of select="local-name()"/></assert>
            
            <!-- article requires an eId -->
            <report
                id="FLX-ART-003" 
                test="not(@eId)"
                ><value-of select="local-name()"/> needs a unique identifier eId</report>
        </rule>
    </pattern>
    
    <pattern>
        <rule context="akn:subdivision" >
           
            <!-- in a subdivision only heading elements and paragraphs are allowed -->
            <assert
                id="FLX-SD-001" 
                test="empty( * except (*[(fun:is-heading-element(.))] | akn:paragraph) )"
                >Content not allowed in <value-of select="local-name()"/></assert>
            
            <!-- a subdivision is only allowed in the context of an article -->
            <assert 
                id="FLX-SD-002" 
                test="parent::akn:article"
                ><value-of select="local-name()"/> only allowed in the context of an article</assert>

            <!-- subdivision requires an eId -->
            <report 
                id="FLX-SD-003" 
                test="not(@eId)"
                ><value-of select="local-name()"/> needs a unique identifier eId</report>
        </rule>
    </pattern>

    <pattern>
        <rule context="akn:article//akn:paragraph" >
            
            <!-- in a paragraph only heading elements and content are allowed -->
            <assert
                id="FLX-PR-001"
                test="empty( * except (*[(fun:is-heading-element(.))] | akn:content) )"
                >Content not allowed in <value-of select="local-name()"/></assert>
            
            <!-- a paragraph is only allowed in the context of an article or a subdivision -->
            <assert 
                id="FLX-PR-002"
                test="parent::*[self::akn:article | self::akn:subdivision]"
                ><value-of select="local-name()"/> only allowed in the context of an article or subdivision</assert>

            <!-- paragraph requires an eId -->
            <report 
                id="FLX-PR-003"
                test="not(@eId)"
                ><value-of select="local-name()"/> needs a unique identifier eId</report>
        </rule>
    </pattern>
    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->    
    <!--  Text Content Restriction -->    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ --> 
    
    <!--<pattern>
        <rule context="akn:br">
            <assert 
                id="FLX-TXT-001" 
                test="ancestor::*[self::akn:docTitle | self::akn:heading | self::akn:subheading]"
                ><value-of select="local-name()"/> restricted to heading type elements only</assert>
        </rule>
    </pattern>-->
    
    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->    
    <!--  Extension Attributes Restrictions -->    
    <!-- ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ + ++++++++++ -->  
    
    <!-- the schema currently is only restrictive on extension attributes in the fedlex namespace -->
    <!-- in case other namespaced attributes are added, they would be ignored in the fedlex processing tools -->
    
    <pattern>
        <rule context="@fedlex:*">
            <!-- only defined fedlex extension attributes are allowed throughout the document -->
            <assert 
                id="FLX-XF-001" 
                test="local-name() = ('role', 'generator')"
                >[{$id}] Fedlex extension attribute not supported: <value-of select="local-name()"/></assert>

            <!-- fedlex:generator only allowed on FRBR format -->
            <report 
                id="FLX-XF-002" 
                test="local-name() = 'generator' and not(parent::akn:FRBRformat[@value='xml'])"
                >Fedlex extension attribute 'generator' not allowed on <value-of select="parent::*/local-name()"/></report>

            <!-- fedlex:role values are either 'reference' or 'marginal' -->
            <report 
                id="FLX-XF-003" 
                test="local-name() = 'role' and not(. = ('reference', 'marginal'))"
                >Fedlex extension attribute 'role', value not allowed: <value-of select="."/></report>

            <!-- fedlex:role value 'marginal' only allowed on level elements -->
            <report 
                id="FLX-XF-004" 
                test="local-name() = 'role' and (. = 'marginal') and not(parent::akn:level)"
                >Fedlex extension attribute 'role', with value 'marginal' not allowed on <value-of select="parent::*/local-name()"/></report>

            <!-- fedlex:role value 'reference' only allowed on subheading elements -->
            <report 
                id="FLX-XF-005" 
                test="local-name() = 'role' and (. = 'reference') and not(parent::akn:subheading)"
                >Fedlex extension attribute 'role', with value 'marginal' not allowed on <value-of select="parent::*/local-name()"/></report>
            
        </rule>
    </pattern>
    
    
</schema>

