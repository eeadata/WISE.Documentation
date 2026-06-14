(heading_using_sourcecode)=
# Using source code blocks

## Literal blocks

Literal code blocks are introduced by ending a paragraph with the special marker `::` in reStructuredText. In Markdown, we use standard backtick code fencing.

::::{tab-set}
:::{tab-item} md

```md
This is a normal text paragraph. The next paragraph is a code sample:

```md
It is not processed in any way, except
that the indentation is removed.

It can span multiple lines.
```

This is a normal text paragraph again.
:::
:::{tab-item} rst

```rst
This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.
```

:::
::::

The handling of the reStructuredText `::` marker is smart:

* If it occurs as a paragraph of its own, that paragraph is completely left out of the document.
* If it is preceded by whitespace, the marker is removed.
* If it is preceded by non-whitespace, the marker is replaced by a single colon.

That way, the second sentence in the above example's first paragraph would be rendered as "The next paragraph is a code sample:".

## Highlight directive

The default highlighting language in Sphinx is Python. In reStructuredText, it can be changed using the `highlight` directive within a document. In Markdown, there is no global equivalent of the `highlight` directive; you must specify the language explicitly on each code block.

::::{tab-set}
:::{tab-item} md

```md
There is no global highlight directive in Markdown. You specify the language on each individual code block:

```html
<html><head></head>
<body>This is a text.</body>
</html>
```

:::
:::{tab-item} rst

```rst
.. highlight:: html

The literal blocks are now highlighted as HTML, until a new directive is found.

::

   <html><head></head>
   <body>This is a text.</body>
   </html>
```

:::
::::

## Code-block directive

The `code-block` directive can be used to declare the specific language to be used in a block, regardless of the default highlighting language.

::::{tab-set}
:::{tab-item} md

```md
```{code-block} sql
:linenos:

SELECT * FROM mytable
```

:::
:::{tab-item} rst

```rst
.. code-block:: sql
   :linenos:

   SELECT * FROM mytable
```

:::
::::

**Output:**

```{code-block} sql
:linenos:

SELECT * FROM mytable
```

Line numbers are useful for long blocks such as this one:

```{code-block} postgresql
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
```

## Literalinclude directive

Another option is to include part of a given source code file, using the `literalinclude` directive.

::::{tab-set}
:::{tab-item} md

```md
```{literalinclude} filename
:linenos:
:language: 
:lines:
:start-after:
:end-before:
:emphasize-lines:
```

:::
:::{tab-item} rst

```rst
.. literalinclude:: filename
   :linenos:
   :language: 
   :lines:
   :start-after:
   :end-before:
   :emphasize-lines:
```

:::
::::

Just below is an example of the use of the `lines` option, which includes only the specified lines of the file.

::::{tab-set}
:::{tab-item} md

```md
```{literalinclude} Using_SourceCode.md
:language: markdown
:lines: 111-114
```

:::
:::{tab-item} rst

```rst
.. literalinclude:: UsingReStructuredText_SourceCode.rst
   :language: rst
   :lines: 111-114
```

:::
::::

**Output:**

```{literalinclude} Using_SourceCode.md
:language: markdown
:lines: 111-114
```

Instead of using line numbers (which can change), it is possible to use the options `start-after` and `end-before` that search the included file for lines containing the specified text.

::::{tab-set}
:::{tab-item} md

```md
```{literalinclude} Using_SourceCode.md
:language: markdown
:start-after: Instead of using line numbers
:end-before: produces this result
```

:::
:::{tab-item} rst

```rst
.. literalinclude:: UsingReStructuredText_SourceCode.rst
   :language: rst
   :start-after: Instead of using line numbers
   :end-before: produces this result
```

:::
::::

**Output:**

```{literalinclude} Using_SourceCode.md
:language: markdown
:start-after: Instead of using line numbers
:end-before: produces this result
```

## Pygments lexers

Syntax highlighting is done by [Pygments](https://pygments.org/), a syntax highlighting package written in Python. Any of the [Pygments language lexers](https://pygments.org/docs/lexers/) can be used.

The following table lists some useful lexers (in no particular order).

(pygments-lexers-ref)=

| Lexer | Shortname |
| :--- | :--- |
| Structured Query Language | sql |
| PostgreSQL dialect of SQL | postgresql |
| PostgreSQL procedural language | plpgsql |
| PostgreSQL console sessions | psql |
| ReStructured Text | rst |
| TeX and LaTeX | latex |
| DOS/Windows batch file | bat |
| Windows PowerShell | powershell |
| Bash shell scripts | bash |
| Bash shell sessions | console |
| Cascading Style Sheets | css |
| HTML | html |
| XML | xml |
| XSLT | xslt |
| XQuery | xquery |
| JavaScript | javascript |
| JSON data structures | json |
| PHP source code | php |
| PHP embedded in HTML | html+php |
| Python | python |
| Python console | pycon |
| Java | java |
| R source code (or S, or S-plus) | r |
| Matlab | matlab |
| NumPy | numpy |
