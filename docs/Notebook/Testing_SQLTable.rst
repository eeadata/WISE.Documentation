Testing the sqltable extension
******************************

The ``sphinxcontrb-sqltable`` is an extension to Sphinx_ to allow authors 
to embed SQL statements in source documents and produce tabular output
in rendered documents.

It supports all databases accessible via SQLAlchemy.

Using ..sqltable in the WISE documentation
==========================================

For the WISE documentation, the most likely use-case 
is to create the reporting guidance documents for dataflows.

Let's start at the end...

* The EEA tabular data published in discodata_. 
* All the published data should have metadata.  
  For each table and column that is published, at least a **[description]** value should exist.
* After the publication, the descriptions are available in the **[metadata].[v2].[metadata]** table.
* The column datatypes, etc. are available in the **[metadata].[v2].[columns]** table.
* The tables can be joined using the **[identifier]** value.

Why is this relevant? 

* To be able to push data into discodata_, 
  a **[metadata]** table with the same structure 
  already exists in the WISE databases (prior to publication).

* The standard **[INFORMATION_SCHEMA].[COLUMNS]** view 
  contains the same information 
  that exists in discodata_ **[columns]** table.

Therefore, it is possible to use that "standard" struture 
to create more user-friendly documentation about tables, columns, etc.

Example: All the published tables related to groundwater bodies and their description
-----------------------------------------------------------------------------------------

See the code example below.

* The **:connection_string:** points to the **wise_wfd_metadata.db** file.
  The path is relative to the location of the **conf.py** file.

* The **:name:** is a unique name within the documentation (that can be used to reference the table).

See the other options in the `sqltable documentation <https://sphinxcontrib-sqltable.readthedocs.io/en/latest/customize.html>`_.

.. code-block:: rst
   :linenos:

   .. sqltable:: Tables in the GWB schema
      :connection_string: sqlite:///docs/Notebook/tables/wise_wfd_metadata.db
      :name: sqltable-example-using-wise_wfd_metadata-gwb-tables

      select title AS Tablename, description AS Description
      from metadata
      where objectType = 'table'
      and title like 'GWB%'
      order by title


The table resulting from the **..sqltable** directive is the one below:

.. sqltable:: Tables in the GWB schema
   :connection_string: sqlite:///docs/Notebook/tables/wise_wfd_metadata.db
   :name: sqltable-example-using-wise_wfd_metadata-gwb-tables

   select title AS Tablename, description AS Description
   from metadata
   where objectType = 'table'
   and title like 'GWB%'
   order by title

Example: The struture of the GWB_GroundWaterBody table
------------------------------------------------------

The example below shows how to document the content of the [GWB_GroundWaterBody] table.

.. code-block:: rst
   :linenos:

   .. sqltable:: Columns in the [GWB_GroundWaterBody] table
      :connection_string: sqlite:///docs/Notebook/tables/wise_wfd_metadata.db
      :name: sqltable-example-using-wise_wfd_metadata-GWB_GroundWaterBody

      select title AS Columnname, DATA_TYPE AS Datatype, description AS Description
      from metadata
      where objectType = 'column'
      and parentIdentifier = '[WISE_WFD].[v2r1].[GWB_GroundWaterBody]'
      order by [ORDINAL_POSITION],title

This is the resulting table:

.. sqltable:: Columns in the [GWB_GroundWaterBody] table
   :connection_string: sqlite:///docs/Notebook/tables/wise_wfd_metadata.db
   :name: sqltable-example-using-wise_wfd_metadata-GWB_GroundWaterBody

   select title AS Columnname, DATA_TYPE AS Datatype, description AS Description
   from metadata
   where objectType = 'column'
   and parentIdentifier = '[WISE_WFD].[v2r1].[GWB_GroundWaterBody]'
   order by [ORDINAL_POSITION],title


About the example database wise_wfd_metadata.db 
-----------------------------------------------

The wise_wfd_metadata.db sqLite database 
contains data extracted form discodata_ 
with the query below, and put into a sqLite database.

(The ipynb notebook will be added soon to the documentation.)

.. code-block:: sql
   :linenos:

   SELECT a.[identifier]
         ,[parentIdentifier]
         ,[title]
         ,[description]
         ,[objectType]
         -- only for columns
         ,[IS_NULLABLE]
         ,[DATA_TYPE]
         ,[CHARACTER_MAXIMUM_LENGTH]
         ,[NUMERIC_PRECISION]
         ,[NUMERIC_SCALE]
         ,[ORDINAL_POSITION]
   FROM [metadata].[v2].[metadata] a
   LEFT JOIN [metadata].[v2].[columns] b
   ON a.[identifier] = b.[identifier]
   
   WHERE a.[identifier] like '%WISE_WFD%v2r1%'
         AND [objectType] IN ('table','column')
   ORDER BY [objectType] desc,[parentIdentifier],[ORDINAL_POSITION],[title]



.. links-placeholder

.. include:: ../_sharedFiles/Links.rst      