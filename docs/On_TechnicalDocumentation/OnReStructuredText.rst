:tocdepth: 2

.. highlight:: rst

.. metadata-placeholder

   :DC.title:
   	What is reStructuredText?
   :DC.creator:
   	Fernanda Nery
   :DC.date:
   	2013-05-01
   :DC.description:
      Brief introduction to reStructuredText (reST) concepts and syntax.
      This is a modified version of Sphinx's reStructuredText Primer
      (http://sphinx-doc.org/).
   :DC.language:
   	eng
   :DC.format:
   	text/x-rst
   :DC.license:
         https://creativecommons.org/licenses/by/4.0/      
   :DC.rights:
   	Public.
   :DC.rightsHolder:
      Copyright (c) 2007-2011 by Georg Brandl
      Copyright (c) 2007-2013 by the Sphinx team

.. _rst-primer-ref:
  
What is reStructuredText?
=========================

.. note::

   This document is an abridged and modified version of `Sphinx's reStructuredText Primer`_.

reStructuredText_ (reST) is a simple, easy-to-read markup language used by Sphinx_.

A reStructuredText document is a text file
with some markup to specify the format or the semantics of the text.

Most of the markup used by Sphinx is standard reST markup
Exceptions (i.e. markup specific to Sphinx) are signalled in the text.

There are two types of markup:

*  **inline markup**: 
   for example, ``*the surrounding asterisks would mark this text as italics*``, like *this*.

*  **explicit markup**: 
   is used for blocks of text that need special handling,
   such as footnotes, tables, or generic directives.
   Explicit markup always starts with ``..`` followed by whitespace.


.. _rst-paragraphs-ref:

Paragraphs
==========

Paragraphs are simply chunks of text separated by one or more blank lines.
All lines of the same paragraph
must be left-aligned to the same level of indentation.

**Quoted paragraphs** are created by
just indenting them more than the surrounding paragraphs::

   Normal paragraph.
      
      Indented paragraph.

.. tip:: 

   Each indentation level is created with 3 whitespaces.
   Do not use tabs.

Line blocks are a way of preserving **line breaks**::

   | the sweet & aged people
   | who rule this world(and me and
   | you if we’re not very
   | careful)

Here is the result of the above markup:

   | the sweet & aged people
   | who rule this world(and me and
   | you if we’re not very
   | careful)
   
.. _rst-sections-ref: 
  
Sections
========

Section are created by underlining the title with a punctuation character::

   This is a heading
   =================

The underlining must be at least as long as the text itself.
Sections must be properly nested.

   .. admonition:: This is a style convention.
      
      Use the following punctuation characters in the section titles:

      *  ``#`` for Parts
      *  ``*`` for Chapters
      *  ``=`` for sections ("Heading 1")
      *  ``-`` for subsections ("Heading 2")
      *  ``^`` for subsubsections ("Heading 3")
      *  ``"`` for paragraphs ("Heading 4")

      When converting to HTML format, 
      sections are converted to an appropriate heading tag 
      (for example: ``<h2>Heading text</h2>``).
      
      When converting to ODT or DOCX, 
      an appropriate Heading style is applied.

.. _rst-inlinemarkup-ref:

Bold, italics, and other inline markup
==================================================

The markup is quite simple:

*  use one asterisk for *italics*: ``*text*``
*  use two asterisks for **bold**: ``**text**``
*  use backquotes for text ``literals``: ````text````
* Subscript is marked with ``:sub:`subscript text```.
* Superscript is marked with ``:sup:`superscript text```.

There are some restrictions:

*  The markup may not be nested.
   For example, this is wrong: ``*italics with **bold** inside*``
*  The text content within the markup may not start or end with whitespace.
   For example, this is wrong: ``* text*``
*  The markup must be separated from surrounding text by whitespace or punctuation.
   Use a backslash-escaped-space to work around that.
   For example: ``thisis\ *one*\ word`` is rendered like thisis\ *one*\ word.

   .. tip:: 

      Whitespace or punctuation is required around interpreted text, 
      but often not desired with subscripts & superscripts. 
      Backslash-escaped whitespace can be used; 
      the whitespace will be removed from the processed document::
      
         The chemical formula for molecular oxygen is O\ :sub:`2`. 
      
      To improve the readability of the text, the use backslash-escapes is discouraged.
      If possible, use :ref:`rst-substitutions-ref` instead::
      
         The chemical formula for pure water is |H2O|.
         
         .. |H2O| replace:: H\ :sub:`2`\ O
      
      Keep all substitutions together (e.g. at the end of the file or in a separate file).
      
.. _rst-lists-ref:

Lists
=====

Bulleted lists
--------------

List markup is natural:
just place an asterisk at the start of a paragraph and indent properly::

   *  This is a bulleted list.
   *  It has two items, the second
      item uses two lines.

Nested lists are possible,
but be aware that they must be separated
from the parent list items by blank lines::

   * this is
   * a list

     * with a nested list
     * and some sub-items

   * and here the parent list continues

Numbered lists
--------------

The same goes for numbered lists;
they can also be auto-numbered using a ``#`` sign::


   1. This is a numbered list.
   2. It has two items too.

   #. This is a numbered list.
   #. It has two items too.

.. _rst-definitionlists-ref: 

Definition lists
----------------

Definition lists are created as follows::

   term (up to a line of text)
      Definition of the term, which must be indented

      and can even consist of multiple paragraphs

   next term
      Description.

The Sphinx_ documentation generator
provides a more flexible alternative to definition lists
(see :ref:`rst-glossaries-ref`).

.. _rst-glossaries-ref: 

Glossaries
----------

The Sphinx ``..glossary::`` directive
contains a reST definition-list-like markup
with terms and definitions.

See the following example::

   .. glossary::

      environment
         A structure where information about all documents under the root is
         saved, and used for cross-referencing.  The environment is pickled
         after the parsing stage, so that successive runs only need to read
         and parse new and changed documents.

      source directory
         The directory which, including its subdirectories, contains all
         source files for one Sphinx project.

The definitions will then be used in cross-references with the ``:term:`` role.
For example:: 

   The :term:`source directory` for this project is ...
         
In contrast to regular definition lists,
a glossary supports *multiple* terms per entry
and inline markup is allowed in terms.
You can link to all of the terms.  For example::

   .. glossary::

      term 1
      term 2
         Definition of both terms.

When the glossary is sorted, the first term determines the sort order.

To automatically sort a glossary, include the following flag::

   .. glossary::
      :sorted:

.. _rst-fieldlists-ref:

Field lists
-----------

Field lists are two-column table-like structures
resembling database records (label & data pairs).
For example::

   :Date: 2001-08-16
   :Version: 1
   :Authors: - Me
             - Myself
             - I
   :Indentation: Since the field marker may be quite long, the second
      and subsequent lines of the field body do not have to line up
      with the first line, but they must be indented relative to the
      field name marker, and they must line up with each other.
   :Parameter i: integer

In this project, field lists are used to include metadata in each document.

   .. admonition:: This is a style convention.
           
      The basic `Dublin Core`_ metadata fields
      should be included in the very beginning of each document
      (like a header to the text file),
      like this::
      
         .. metadata-placeholder
      
         :DC.title: 
            Document title
         :DC.creator:
            Author(s) and/or organisation(s) responsible for the content of the document.
         :DC.date:
            Creation date or last update date of the document.
            Use the YYYY-MM-DD format.
         :DC.description:
            Abstract
         :DC.language:
            eng
         :DC.format:
            text/x-rst
         :DC.license:
            https://creativecommons.org/licenses/by/4.0/
         :DC.rights:
            Access rights
         :DC.rightsHolder:
            E.g. European Environment Agency, European Commission, etc.

      Note that these metadata field names 
      are not automatically recognised by the Sphinx parser, 
      so the text itself will not be visible in the HTML pages (for example). 
      The metadata fields are the equivalent 
      to the *Document properties* fields in a ``DOCX`` file or an ``ODT`` file.
   
docutils_ recognises a number of Bibliographic Fields 
(such as ``docinfo``, ``author``, ``authors``, 
``organization``, ``contact``, ``version``, ``status``, 
``date``, ``copyright``, ``field``, ``topic``).

.. _rst-hyperlinks-ref:

Hyperlinks
==========

External links
--------------

Use ```link text <http://example.com/>`_`` for inline web links.
If the link text should be the web address,
you don't need special markup at all,
the parser finds links and mail addresses in ordinary text (with no markup).

You can also separate the link and the target definition, like this::

   This is a paragraph that contains `a link`_.

   .. _a link: http://example.com/

   .. tip:: This is a tip.

      The use of inline web links is discouraged, 
      to improve the readability of the reST text.
      
      Simple links (e.g. to institutional sites, software sites, and so on)
      should be kept together at the end of the text file 
      (this is merely a way to simplify the editing procedure, 
      and the update and verification of the links).

.. _rst-internallinks-ref:
   
Internal links
--------------

To support cross-referencing to arbitrary locations in any document,
the standard reST labels are used.
For this to work,
the label names must be unique throughout the entire documentation.
There are two ways in which you can refer to labels:

*  If you place a label directly before a section title,
   you can reference to it with ``:ref:`label-name```.
   Example::

      .. _my-label-ref:

      Section to cross-reference
      --------------------------

      This is the text of the section.

      In the end of this phrase is a reference to the section title, see :ref:`my-label-ref`.

   The ``:ref:`` role would then generate a link to the section, 
   with the link  title being "Section to cross-reference".  
   This works just as well 
   when section and reference are in different source files.

   Automatic labels also work with :ref:`figures <rst-figures-ref>`::

      .. _my-figure-ref:

      .. figure:: my-image.png

         My figure caption

   A reference like ``:ref:`my-figure-ref``` 
   would insert a reference to the figure
   with link text "My figure caption".

*  Labels that aren't placed before a section title can still be referenced
   to, but you must provide the text for the link, using this syntax:
   ``:ref:`Link text <label-name>```.

Using ``:ref:`` is advised over standard reStructuredText links to sections
(like ```Section title`_``) because it works across files, when section
headings are changed, and for all builders that support cross-references.

.. _rst-explicitmarkup-ref:
      
Explicit Markup
===============

Explicit markup is used in reStructuredText
for most constructs that need special handling,
such as footnotes,
specially-highlighted paragraphs,
comments,
and generic directives.

An explicit markup block begins with a line starting with ``..``
followed by whitespace
and is terminated by the next paragraph
at the same level of indentation.
(There needs to be a blank line
between explicit markup and normal paragraphs.
This may all sound a bit complicated,
but it is intuitive enough when you write it.)

.. _rst-directives-ref:

Directives
==========

A directive is a generic block of explicit markup.

The directive content follows after a blank line
and is indented relative to the directive start.

Basically, a directive consists of a name, arguments, options and content.

Look at this example::

   .. contents:: This is my Table of Contents
      :depth: 2
      
The directive starts with ``..`` followed by one whitespace.
The name of the directive is ``contents`` (it creates a table of contents).
This directive takes one argument:
the table of contents' title ("This is my Table of Contents").
The option ``depth`` specifies
the number of section levels that are collected in the table of contents.

Options are given in the lines immediately following the arguments
and are indicated by the colons.
Options must be indented to the same level as the directive content.

Docutils_ supports the many directives (not all are listed below!):

*  Admonitions: ``attention``, ``caution``, ``danger``,
   ``error``, ``hint``, ``important``, ``note``,
   ``tip``, ``warning`` and the generic ``admonition``.
   (Most themes style only ``note`` and ``warning`` specially.)

*  Images:

   *  ``image`` - see the images_ section;
   *  ``figure`` - an image with caption and optional legend.

*  Additional body elements:

   *  ``contents <table-of-contents>`` -
      a local table of contents for the sections in the current file only;
   *  ``rubric`` -
      a heading without relation to the document's sections
      that won't be included in any table of contents;
   *  ``topic`` and ``sidebar`` - special highlighted body elements;
   *  ``epigraph`` - a block quote with optional attribution line;
   *  ``container`` -   a container with a custom class,
      useful to generate an outer ````<div>```` in HTML output.

*  Special directives:

   *  ``include`` - include reStructuredText from another file;
   *  ``raw`` -  include raw target-format markup, such as LaTeX;
   *  ``class`` - assign a class attribute to the next element.

.. _rst-contents-ref:

Table of contents
====================

To include a table of contents within a given document,
use the directive ``contents``.
The following example creates a local table of contents
with a maximum of two levels (below the level where it is located)::

   
   Part II
   #######
   
   Chapter 1
   *********
      
   .. contents::
      :depth: 2
      :local: 

   Heading 1
   =========
   
The ``toctree`` directive creates a table of contents
that collets information from several files.
The following example creates a table of contents
from the sections of various documents (up to a depth of 3 levels).
The ``:glob:`` option allows all documents in the 'chapter2' folder
to be included (sorted according to their name)::
   
   .. toctree::
      :glob:
      :maxdepth: 3
      
      preamble
      chapter1/part1
      chapter1/conclusion
      chapter2/*
      references 
    
   
.. _rst-images-ref:

Images
------

reST supports an image directive, used like so::

   .. image:: myImage.png
      :width: 100%
      :align: middle

The filename must either be relative to the source file,
or absolute (which means that they are relative to the top source directory).


.. _rst-figures-ref:

Figures
-------

A ``figure`` consists of image data (including image options),
an optional caption (a single paragraph),
and an optional legend (arbitrary body elements)::

   .. figure:: picture.png
      :scale: 50 %
      :alt: map to buried treasure

      This is the caption of the figure (a simple paragraph).

      The legend consists of all elements after the caption.  In this
      case, the legend consists of this paragraph and the following
      table:

      +-----------------------+-----------------------+
      | Symbol                | Meaning               |
      +=======================+=======================+
      | .. image:: tent.png   | Campground            |
      +-----------------------+-----------------------+
      | .. image:: waves.png  | Lake                  |
      +-----------------------+-----------------------+
      | .. image:: peak.png   | Mountain              |
      +-----------------------+-----------------------+

There must be blank lines before the caption paragraph and before the legend.
To specify a legend without a caption,
use an empty comment (``..``) in place of the caption.

.. _rst-footnotes-ref:

Footnotes
---------

For footnotes, use ``[#name]_`` to mark the footnote
location, and add the footnote body at the bottom of the document after a
"Footnotes" rubric heading, like so::

   Lorem ipsum [#first-footnote-name]_ dolor sit amet [#second-footnote-name]_

   .. rubric:: Footnotes

   .. [#first-footnote-name] Text of the first footnote.
   .. [#fsecond-footnote-name] Text of the second footnote.

You can also explicitly number the footnotes (``[1]_``) or use auto-numbered
footnotes without names (``[#]_``).

   .. tip:: 

      To facilitate editing, auto-numbered footnotes should **not** be used. 
      Instead, use short descriptive names (that simplify cross-referencing).    
   
.. _rst-citations-ref:  
   
Citations
---------

Standard reST citations are supported::

   Lorem ipsum [Ref]_ dolor sit amet.

   .. [Ref] Book or article reference, URL or whatever.

Citation usage is similar to footnote usage,
but with a label that is not numeric or begins with ``#``.

When the documentation is built using the Sphinx_  document generator,
the citations are "global",
meaning that every citation can be referenced from any .rst files.
In this case, a separate file may be created (e.g. a ``references.rst`` file).

   .. tip:: 

      See :ref:`rst-biblio-ref` for further information.
   
.. _rst-substitutions-ref:
   
Substitutions
-------------

reST supports "substitutions",
which are pieces of text and/or markup referred to in the text by ``|name|``.
They are defined like footnotes with explicit markup blocks, like this::

   .. |name| replace:: replacement *text*

or this::

   .. |caution| image:: warning.png
                :alt: Warning!


If you want to use some substitutions for all documents,
put them into a separate file
(e.g. ``substitutions.txt``)
and include it into all documents you want to use them in,
using the ``include`` directive.

Be sure to use a file name extension
which different from that of other source files,
to avoid Sphinx finding it as a standalone document.
For example, use the ``.rst`` file extension for the source files,
and the ``.txt`` file extension for the files which are to be included.

   .. tip:: 

      This is useful in technical documentation such as User's Manuals, 
      where a substitution file can be built for each localised version 
      of the interface elements (menus, messages, etc), 
      guaranteeing the consistency of the document translation 
      with the software's human user interface.

   .. warning::

      Substitutions do NOT work inside directives (or inside the options of a directive).
      
      Do not try to google for a solution (...been there). 
      It is a design limitation: RST markup can not be nested. Period.

   .. warning::

      Substitutions can be used with the ``image`` directive, 
      which is an inline element.
      Substitutions can **not** be used with the ``figure`` directive, 
      which creates a block-level element.

.. _rst-comments-ref:

Comments
--------

Every explicit markup block
which isn't a valid markup construct is regarded as a comment.
For example::

   .. This is a comment.

You can indent text after a comment start to form multiline comments::

   ..
      This whole indented block
      is a comment.

      Still in the comment.
   ..

.. admonition:: This is a style convention.
      
   Comments can also be used as placeholders 
   to mark places within the document. 
   For example:

   *  the ``.. links-placeholder`` can mark the place 
      where hyperlinks are kept together at the end of the document;
      
   *  the ``.. metadata-placeholder`` can mark the place 
      where document metadata (author, date, etc) 
      is kept together at the beginning of the document.
   
.. links-placeholder

.. include:: ../_sharedFiles/Links.rst