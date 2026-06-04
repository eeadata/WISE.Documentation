:html_theme.sidebar_secondary.remove:

WISE Docs-as-Code
*********************************

.. toctree:: 
   :maxdepth: 1
   :hidden: 
   
   GettingStarted/index
   WritingDocs/index
   On_VersionControl/index
   Notebook/index

Here you will find information about how to create and maintain the documentation for WISE dataflows and projects. 

We want to move away from the traditional "Guidance Documents" in PDF format.
Instead, we want to create living documentation that is easily accessible and can be updated regularly.
Also, we would rather never see a Word document with track changes again in our lives...

Follow the link to learn more about the `Docs as Code <https://www.writethedocs.org/guide/docs-as-code/>`_ approach.

The WISE Documentation is organized into three main sections:

* **Getting Started**: 

  *You only need to read this once, if you are setting up your work environment for the first time.* 

  This section provides instructions on how to set up the WISE environment and get started with the documentation.

* **Writing documentation**: 

  This section provides guidelines and best practices 
  for creating and maintaining technical documentation for WISE dataflows and projects. 
  It covers topics such as writing style, formatting, and tools for generating documentation.

* **Version control**: 

  This section provides information about using the GIT version control system
  for managing and publishing the documentation. 
  It includes guidelines for organizing documentation files, committing changes, and collaborating with other contributors.

WISE documentation using Sphinx
=======================================

The following projects have WISE **public** documentation 
using Sphinx.

.. list-table:: 
   :name: wise-projects-using-Sphinx
   :header-rows: 1
   :stub-columns: 1
   :width: 80
   :align: center

   *  - Project
      - Link
   *  - Water Framework Directive
      - https://eeadata.github.io/WISE.WFD.Documentation/


Projects using Sphinx and the PyData theme
==========================================

The following projects use the PyData Sphinx theme, 
and are a good source of inspiration and examples.

.. csv-table:: 
   :name: projects-using-the-PyData-Sphinx-theme
   :file: GettingStarted/tables/ProjectsUsingThePyDataTheme.csv
   :header-rows: 1
   :stub-columns: 1
   :width: 80
   :align: center
   
Good documentation about good documentation
==============================================================

When (if...) this project grows and matures, it would be nice to have something like:

* the Canonical `Sphinx Stack documentation <https://documentation.ubuntu.com/sphinx-stack/latest/#>`_ 
  describes the Sphinx stack used by Canonical in the Ubuntu documentation 
  (and in the documentation of all their other products) 

* the Canonical `Documentation Style Guide <https://documentation.ubuntu.com/style-guide>`_ 
  contains basic style guidelines. 
  When in doubt, and until there's a strong case for having different guidelines, it's OK to follow theirs.

Once time allows, some simple guidelines have to be made based on:

* the SEMIC style guidelines for data specifications, specifically the part about 
  `conceptual model conventions (UML) <https://semiceu.github.io/style-guide/1.0.0/gc-conceptual-model-conventions.html>`_
* the EC Library Guides on `how to cite documents and data <https://ec-europa-eu.libguides.com/EU_sources/citing>`_

TL;DR yet
=========

Technical documentation is frequently organised into four blocks 
(see for example the `Ubuntu documentation <https://documentation.ubuntu.com/core/>`_):

* Tutorials - learning-oriented experiences
* How-to guides - goal-oriented directions
* Reference - information-oriented technical description
* Explanation - understanding-oriented discussion

Aparently there's a methodology behind it: 
see `diátaxis <https://diataxis.fr/application/>`_ for a complete guide.