ELI Annotation Tool
===================


The ELI annotation tool is a tool for building notices describing legal
resources using the `European Legislation Identifier <http://www.eli.fr/>`_
(ELI) standard.

The notices describe several standard legal entities (*legal resources*, *legal
expressions* and *formats*) using standard properties.
The values of some of these properties are constrained using controlled
vocabularies described with the `SKOS standard
<https://www.w3.org/2004/02/skos/>`_).

The notices can be created for three different types of resources: *acts*,
*official journals* and *consolidations*. For each of these types, the ELI
annotation tool allows to configure the notices form by choosing which
properties will be active for the legal entities and by choosing the
controlled vocabularies of these properties (when applicable).

The ELI annotation tool is a Web application that must be installed on a Web
server. Command-line operations executed on the server allow to configure the
ELI annotation tool, localize it and manage its users. Once this server is
configured, the ELI annotation tool is accessible simply with a recent (as of
end of 2017) Web browser.

The ELI annotation tool is not meant to publish, manage or archive notices and
vocabularies. It is meant to be simple to set up (no database, no connection to
a user directory, no connection to external data sources, etc.) and to allow
users to efficiently produce the notices that will be published on the Web
using other tools and other servers.


License
-------

The ELI annotation tool is published under the EUPL license.

See https://joinup.ec.europa.eu/community/eupl/og_page/eupl
