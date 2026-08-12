.. -*- coding: utf-8 -*-

Install
=======

The ELI Annotation tool is expected to be installed onto a Debian Stretch
(Debian 9) system thanks to a ``deb`` package.

Hardware prerequisites
----------------------

The ELI Annotation tool is a Web application and should be installed on
a computer that meets the state-of-the-art requirements of a standard
little Web server. Currently (as of end 2017), this would be:

* RAM: 4 Go
* Disk: 32 Go
* CPU: Intel i7 or equivalent

The CPU could be a less powerful one but then, when uploading big
vocabularies, the processing might take too long.

Setup
-----

Add the stretch-backports repository to the package sources, by adding to the
``/etc/apt/source.list.d`` directory a file named ``stretch-backports.list``
that contains the line::

  deb http://httpredir.debian.org/debian stretch-backports main

This will allow the retrieval of the needed dependencies (listed in the
sources in the ``debian/control`` file).

Install
-------

Install the ELI Annotation Tool package using the ``dpkg`` tool::

   dpkg -i eli-annotation-tool.deb

Then make sure all the dependency packages are installed with::

   apt-get -f install

Web server configuration
------------------------

The ELI annotation tool is a Web application that listens on a network port (see
:ref:`serve` section). If needed, make sure your firewall is not blocking the
HTTP trafic to this port on your server.

Please note that the ELI annotation tool is a Web application that expects its
URLs to be absolute (main page at ``/``\ ). If you use a proxy server, make sure
it is correctly configured for the URL routing process to work.

Configuration
-------------

Please note that **it is necessary to configure the tool before
doing any other operation.**

