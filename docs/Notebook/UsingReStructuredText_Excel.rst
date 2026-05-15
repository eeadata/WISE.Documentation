
.. _rst-excel-table-ref:

Using reStructuredText - Excel tables
=======================================

.. note:: **NOT RECOMMENDED**
   
   Two extensions were explored but so far the results were deemed inadequate.  
   The extensions are not installed in this project.  
   This page will be kept in the documentation:  
   
   * in case this needs to be further explored,
   * to avoid looking into the same options again.

.. _rst-excel-table-directive-ref:

Excel tables using the excel-table extension
---------------------------------------------

Using Excel tables requires an additional module `sphinxcontrib-excel-table`.
See https://pypi.org/project/sphinxcontrib-excel-table/ for the instalation instructions,
which require copying some files to the Sphinx project `_templates` and `_static` folders.

.. note:: 
   This extension is not very flexible. If possible, avoid it using it.
   The reason this section is included is to document the perceived limitations, and not to encourage its use.

The syntax ``excel-table`` is simple::

   .. excel-table:: 
      :file: tables/EFTA.xlsx
      :selection: D4:E8

..
   Creates this table, using the first worksheet (even if there are several worksheets in the Excel):

   .. excel-table:: 
      :file: tables/EFTA.xlsx
      :selection: D4:E8
..

You can also embed worksheets with merged cells::

   .. excel-table:: 
      :file: tables/EFTA.xlsx
      :sheet: StrangeExample

..
   .. excel-table:: 
      :file: tables/EFTA.xlsx
      :sheet: StrangeExample
..

Apparently, only one option can be used at a time (e.g. if you select a worksheet, you can't simultaneously select a range of cells).
It is not possible to specify a caption, nor to use the generic `:name:` option.

.. _rst-xlsx-table-directive-ref:

Excel tables using the xlsx-table extension
---------------------------------------------
      
Using Excel tables requires an additional module `sphinxcontrib.xlsxtable`.

.. warning:: 
   
   When deplying to GitHub pages, there is a problem rendering tables 
   created with the `.. xlsx-table::` directive. 

   As of early 2026, the official sphinxcontrib-xlsxtable (version 1.1.1) 
   is not compatible with Docutils 0.21 or 0.22+.

   Therefore the examples in this section will be commented out, 
   until a solution can be found.

The syntax ``xlsx-table`` is simple::
   
      .. xlsx-table:: EFTA countries from an Excel file
         :file: tables/EFTA.xlsx
         :sheet: example
         :header-rows: 1
         :include-columns: D-E
         :include-rows: 4-8
         
..   
   This is the result that you can link to using the name you gave it (:ref:`the-EFTA-table-in-Excel-ref`):

   .. xlsx-table:: EFTA countries from an Excel file
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