.. highlight:: rst
    
.. _rst-tables-ref:

Using reStructuredText - Tables
===============================

Grid tables
--------------------------------------------

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
--------------------------------------------

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
--------------------------------------------

The ``table`` directive associates a title with the following table::

   .. table:: User list with two persons
      :name: table-user-list-with-two-persons-ref

      ==========  =========
      First name  Last name
      ==========  =========
      John        Doe
      Jane        Dove
      ==========  =========

This is the result:

.. table:: User list with two persons
   :name: table-user-list-with-two-persons-ref

   ==========  =========
   First name  Last name
   ==========  =========
   John        Doe
   Jane        Dove
   ==========  =========

And you can cross-reference to the :numref:`table-user-list-with-two-persons-ref` in the text, using::

   :numref:`table-user-list-with-two-persons-ref`


.. _rst-list-table-directive-ref:

List-table directive
--------------------------------------------

.. note::

   This is the recommended option for simple tables.

A ``list-table`` is created from a uniform two-level bullet list::

   .. list-table:: Another user list
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

.. list-table:: Another user list
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

Same as before, you can also use just a numbered reference :numref:`a-name-you-can-use-to-link-to-this-table`::

   you can also use just a numbered reference :numref:`a-name-you-can-use-to-link-to-this-table`

   
.. _rst-csv-table-directive-ref:

CSV-table directive
--------------------------------------------

.. note::

   This is the recommended option for long tables, 
   specially using a separate CSV file.

A ``csv-table`` is created from comma-separated values
(either in the document or in an external file)::

   .. csv-table:: User list
      :name: this-one-is-a-csv-table-with-a-user-list
      :header: "First name","Last name"
      
      "John","Doe"
      "Jane","Dove"

This is the :ref:`result <this-one-is-a-csv-table-with-a-user-list>`:

.. csv-table:: User list
   :name: this-one-is-a-csv-table-with-a-user-list
   :header: "First name","Last name"
   
   "John","Doe"
   "Jane","Dove"

Another example of ``csv-table``, using and external file::

   .. csv-table:: EFTA countries.
      :name: the-EFTA-table
      :file: tables/EFTA.csv
      :header-rows: 1
      :stub-columns: 1
      
This is the result that you can link to using the name you gave it (:ref:`the-EFTA-table`):

.. csv-table:: EFTA countries.
   :name: the-EFTA-table
   :file: tables/EFTA.csv
   :header-rows: 1
   :stub-columns: 1


.. links-placeholder

.. include:: ../_sharedFiles/Links.rst