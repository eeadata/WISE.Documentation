:tocdepth: 3

.. highlight:: rst

.. metadata-placeholder

   :DC.title:
   	Separate document just about tables
   :DC.creator:
   	Fernanda Nery
   :DC.date:
   	2026-02-27
   :DC.description:
      Putting everything related to tables into a separate document
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

   
.. _rst-tables-ref:

Tables
======

.. contents:: On this page...
   :depth: 3
   :local:

Grid tables
-----------

The reStructuredText markup supports two basic types of tables.
For *grid tables*,
you have to "paint" the cell grid yourself.
They look like this::

   +------------------------+------------+----------+----------+
   | Header row, column 1   | Header 2   | Header 3 | Header 4 |
   | (header rows optional) |            |          |          |
   +========================+============+==========+==========+
   | body row 1, column 1   | column 2   | column 3 | column 4 |
   +------------------------+------------+----------+----------+
   | body row 2             | ...        | ...      |          |
   +------------------------+------------+----------+----------+

This is the result:

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

Simple tables
-------------

*Simple tables* are easier to write, but limited:
they must contain more than one row,
and the first column cannot contain multiple lines.
They look like this::

   =====  =====  =======
   A      B      A and B
   =====  =====  =======
   False  False  False
   True   False  False
   False  True   False
   True   True   True
   =====  =====  =======

This is the result:

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

.. _rst-table-directive-ref:

Table directive
---------------

The ``table`` directive associates a title with the following table::

   .. table:: Table 1 - User list with two persons

      ==========  =========
      First name  Last name
      ==========  =========
      John        Doe
      Jane        Dove
      ==========  =========

This is the result:

.. table:: Table 1 - User list with two persons

   ==========  =========
   First name  Last name
   ==========  =========
   John        Doe
   Jane        Dove
   ==========  =========

.. _rst-list-table-directive-ref:

List-table directive - **recommended**
--------------------------------------

A ``list-table`` is created from a uniform two-level bullet list::

   .. list-table:: User list
      :header-rows: 1
      :name: a-name-you-can-use-to-link-to-this-table
      :widths: 10 20 10
      :width: 50%
      :align: center

      *  - First name
         - Last name
         - Photo
      *  - John
         - Doe
         - .. image:: img/john.png
      *  - Jane
         - Dove
         - .. image:: img/jane.png

This is the result:

.. list-table:: User list
   :header-rows: 1
   :name: a-name-you-can-use-to-link-to-this-table
   :widths: 10 20 10
   :width: 50%
   :align: center

   *  - First name
      - Last name
      - Photo
   *  - John
      - Doe
      - .. image:: img/john.png
   *  - Jane
      - Dove
      - .. image:: img/jane.png

And this is how you reference the table in your text::

   As you can see in the :ref:`a-name-you-can-use-to-link-to-this-table` table, we only have two users.

Which generates the following paragraph:

   As you can see in the :ref:`a-name-you-can-use-to-link-to-this-table` table, we only have two users.
   
.. _rst-csv-table-directive-ref:

CSV-table directive - **recommended**
-------------------------------------

A ``csv-table`` is created from comma-separated values
(either in the document or in an external file)::

   .. csv-table:: User list
      :header: "First name","Last name"
      
      "John","Doe"
      "Jane","Dove"

This is the result:

.. csv-table:: User list
   :header: "First name","Last name"
   
   "John","Doe"
   "Jane","Dove"

Another example of ``csv-table``, using and external file::

   .. csv-table:: Table 1 - EFTA countries.
      :name: the-EFTA-table
      :file: tables/EFTA.csv
      :header-rows: 1
      :stub-columns: 1
      
This is the result that you can link to using the name you gave it (:ref:`the-EFTA-table`):

.. csv-table:: Table 1 - EFTA countries.
   :name: the-EFTA-table
   :file: tables/EFTA.csv
   :header-rows: 1
   :stub-columns: 1

.. _rst-excel-table-directive-ref:

Excel tables using the excel-table extension
---------------------------------------------

Using Excel tables requires an additional module `sphinxcontrib-excel-table`.
See https://pypi.org/project/sphinxcontrib-excel-table/ for the instalation instructions,
which require copying some files to the Sphinx project `_templates` and `_static` folders.

.. warning:: 
   
   This extension is not very flexible. If possible, avoid it using it.
   The reason this section is included is to document the perceived limitations, and not to encourage its use.

The syntax ``excel-table`` is simple::

   .. excel-table:: 
      :file: tables/EFTA.xlsx
      :selection: D4:E8

Creates this table, using the first worksheet (even if there are several worksheets in the Excel):

.. excel-table:: 
   :file: tables/EFTA.xlsx
   :selection: D4:E8

You can also embed worksheets with merged cells::

   .. excel-table:: 
      :file: tables/EFTA.xlsx
      :sheet: StrangeExample

.. excel-table:: 
   :file: tables/EFTA.xlsx
   :sheet: StrangeExample


Apparently, only one option can be used at a time (e.g. if you select a worksheet, you can't simultaneously select a range of cells).
It is not possible to specify a caption, nor to use the generic `:name:` option.

 
.. _rst-xlsx-table-directive-ref:

Excel tables using the xlsx-table extension
-------------------------------------------
      
Using Excel tables requires an additional module `sphinxcontrib.xlsxtable`.

.. warning:: 
   
   When deplying to GitHub pages, there is a problem rendering tables 
   created with the `.. xlsx-table::` directive. 

   As of early 2026, the official sphinxcontrib-xlsxtable (version 1.1.1) 
   is not compatible with Docutils 0.21 or 0.22+.

   Therefore the examples in this section will be commented out, 
   until a solution can be found.

The syntax ``xlsx-table`` is simple::
   
      .. xlsx-table:: Table 1 - EFTA countries from an Excel file
         :file: tables/EFTA.xlsx
         :sheet: example
         :header-rows: 1
         :include-columns: D-E
         :include-rows: 4-8
         
..   
   This is the result that you can link to using the name you gave it (:ref:`the-EFTA-table-in-Excel-ref`):

   .. xlsx-table:: Table 1 - EFTA countries from an Excel file
      :file: tables/EFTA.xlsx
      :sheet: Example
      :header-rows: 1
      :include-columns: D-E
      :include-rows: 4-8
..

You can also embed worksheets with merged cells.
The original formatting of the is **not** kept.

..
   .. xlsx-table:: A table with lots of strange cells
      :file: tables/EFTA.xlsx
      :sheet: StrangeExample
      :header-rows: 1
..

It is possible to specify a caption, but it is NOT possible to use the generic `:name:` option.

.. links-placeholder
.. include:: ../_sharedFiles/Links.rst
