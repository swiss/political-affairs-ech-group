.. -*- coding: utf-8 -*-

Expected usage
==============

Each organization can, of course, use the ELI annotation tool in any
way that best fits its needs. Nevertheless, the tool has been designed
with a specific usage in mind. This section describes the expected
business use case around the ELI annotation tool.

The ELI annotation tool has been built for writing ELI notices
describing legal resources. The notices can be written for three
differents types of resources: *acts*, *official journals* and
*consolidations*. The tool is not fitted for publishing such notices
on the Web or for managing published notices.

Firstly, a user with administrative rights must configure the tool by:

1. uploading the controlled vocabularies that will be used in the ELI
   properties,
2. configuring the form used to created the notices for each type of
   legal resource:

   - how the URIs of the ELI entities will be built,
   - for which languages and formats the ELI entities will be created,
   - which ELI properties will be active,
   - which controlled vocabulary will be used in each of the ELI properties
     (that require a vocabulary).

Then the tool can be used to create legal notices:

1. A regular user creates a new notice for an act, an official journal or
   a consolidation. The user can visualize the notice in various formats,
   including an HTML rendering.
2. A designated user proofreads the notice, corrects it and downloads it in
   an archive file (zip format) containing the HTML rendering of all the
   *legal expressions* and all the *formats* contained in the notice
3. This HTML files inside the archive file have now to be deployed on
   an external Web server (this operation is outside the scope of the ELI
   annotation tool).

It is strongly adviced to delete the notices when they have been deployed on
the external Web server. The ELI annotation tool has not been designed to
manage the notices but only to write them. Having too much notices inside
the tool will result in bad performances. If necessary, it is always possible
to import a notice in the tool from any generated HTML rendering.
