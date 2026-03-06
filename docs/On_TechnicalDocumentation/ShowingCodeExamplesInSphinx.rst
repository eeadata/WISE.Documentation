:tocdepth: 2

.. highlight:: rst

.. metadata-placeholder

   :DC.Title:
      Showing source code examples in Sphinx
   :DC.Creator:
      Fernanda Nery
   :DC.Date:
      2013-05-25
   :DC.Description:
      Overview on the available alternatives for showing source code examples
      in Sphinx.
   :DC.Language:
      en
   :DC.Format:
      text/x-rst
   :DC.Rights:
      Public 

.. _rst-sourcecode-ref:

Source code
====================

.. contents:: On this page...
   :depth: 3
   :local:

Literal blocks
-----------------

Literal code blocks are introduced by ending a
paragraph with the special marker ``::``.
The literal block must be indented
(and, like all paragraphs, separated from the surrounding ones by blank lines)::

   This is a normal text paragraph. The next paragraph is a code sample::

      It is not processed in any way, except
      that the indentation is removed.

      It can span multiple lines.

   This is a normal text paragraph again.

The handling of the ``::`` marker is smart:

*  If it occurs as a paragraph of its own, that paragraph is completely left
   out of the document.
*  If it is preceded by whitespace, the marker is removed.
*  If it is preceded by non-whitespace, the marker is replaced by a single
   colon.

That way, the second sentence in the above example's first paragraph would be
rendered as "The next paragraph is a code sample:".

Highlight directive
---------------------

The default highlighting language is Python:
it can be be changed using the ``highlight`` directive
within a document::

   .. highlight:: html

.. highlight:: html

The literal blocks are now highlighted as HTML, until a new directive is found. 

:: 

   <html><head></head>
   <body>This is a text.</body>
   </html>

The following directive changes the hightlight language to SQL.::
      
   .. highlight:: sql

.. highlight:: sql

Therefore, the following block is highlighted as SQL.

:: 

   SELECT * FROM mytable
   
If we want to stop highlighting, we can use the ``none`` language, which is a special lexer that does not do any highlighting.::

   .. highlight:: none

.. highlight:: none
   
From here on no highlighting will be done. 
   
   :: 

      SELECT * FROM mytable
    

Code-block directive
--------------------

The ``code-block`` directive can be used to declare the specific language
to be used in a block, regardless of the highlighting language.
Use the following directive::
   
   .. code-block:: sql
      :linenos:

      SELECT * FROM mytable

... to create the following result:

.. code-block:: sql
   :linenos:

   SELECT * FROM mytable


Line numbers are useful for long blocks such as this one:

.. code-block:: postgresql
   :linenos:
   
   -- http://www.postgresonline.com/journal/index.php?/archives/97-SQL-Coding-Standards-To-Each-His-Own-Part-II.html
   SELECT persons.id, persons.first_name, persons.last_name, forums.category,
      COUNT(DISTINCT posts.id) as num_posts,
      COALESCE(MAX(comments.rating), 0) AS highest_rating,
      COALESCE(MIN(comments.rating), 0) AS lowest_rating
   FROM persons JOIN posts ON persons.id = posts.author
      JOIN forums on posts.forum = forums.id
      LEFT OUTER JOIN comments ON posts.id = comments.post
   WHERE persons.status > 0
      AND forums.ratings = TRUE
      AND comments.post_date > ( now() - INTERVAL '1 year')
   GROUP BY persons.id, persons.first_name, persons.last_name, forums.category
   HAVING count(DISTINCT posts.id) > 0
   ORDER BY persons.last_name, persons.first_name; 
      
Literalinclude directive
------------------------

Another option is to include part of a given source code file, using the ``literalinclude`` directive::

      .. literalinclude:: filename
         :linenos:
         :language: 
         :lines:
         :start-after:
         :end-before:
         :emphasize-lines:

Just below is a example of the use of the ``lines`` option, which includes only the specified lines of the file.:

.. literalinclude:: ShowingCodeExamplesInSphinx.rst
   :language: rst
   :lines: 111-114

Instead of using line numbers (which can change), it is possible to
use the options ``:start-after`` and ``:end-before:``
that search the included file for lines containing the specified text.
For example::

   .. literalinclude:: ShowingCodeExamplesInSphinx.rst
      :language: rst
      :start-after: Instead of using
      :end-before: For example

produces this result:

.. literalinclude:: ShowingCodeExamplesInSphinx.rst
      :language: rst
      :start-after: Instead of using
      :end-before: For example

Pygments lexers
-----------------

Syntax highlighting is done by Pygments_, a syntax highlighting package written in Python.
Any of the `Pygments language lexers`_ can be used.

The following table lists some useful lexers (in no particular order).

.. _pygments-lexers-ref:

.. list-table::
   :header-rows: 1
   
   *  -  Lexer
      -  Shortname
      
   *  -  Structured Query Language
      -  sql
      
   *  -  PostgreSQL dialect of SQL
      -  postgresql
      
   *  -  PostgreSQL procedural language
      -  plpgsql
      
   *  -  PostgreSQL console sessions
      -  psql
      
   *  -  ReStructured Text
      -  rst
   
   *  -  TeX and LaTeX
      -  latex
      
   *  -  DOS/Windows batch file
      -  bat
   
   *  -  Windows PowerShell
      -  powershell
      
   *  -  Bash shell scripts
      -  bash
      
   *  -  Bash shell sessions
      -  console
      
   *  -  Cascading Style Sheets
      -  css
      
   *  -  HTML
      -  html
   
   *  -  XML
      -  xml
   
   *  -  XSLT
      -  xslt
   
   *  -  XQuery
      -  xquery
      
   *  -  JavaScript
      -  javascript
   
   *  -  JSON data structures
      -  json
   
   *  -  PHP source code
      -  php
      
   *  -  PHP embedded in HTML
      -  html+php
      
   *  -  Python 
      -  python
   
   *  -  Python console
      -  pycon
   
   *  -  Java 
      -  java
        
   *  -  R source code (or S, or S-plus)
      -  r
      
   *  -  Matlab
      -  matlab
      
   *  -  NumPy
      -  numpy



.. links-placeholder

.. include:: ../_sharedFiles/Links.rst
      