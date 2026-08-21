(heading_using_bibtex_citations)=
# Using BibTeX citations

https://ec-europa-eu.libguides.com/EU_sources/citing

https://style-guide.europa.eu/en/content/-/isg/topic?identifier=5.9.4-bibliographic-references

https://www.zotero.org/styles?q=id%3Aeu-interinstitutional-style

## Inline citations

The base format for inline citations (e.g., whether your whole project uses author-year `[Smith, 2020]` or numeric `[1]`)
is set **globally** in your `conf.py` and cannot be easily mixed.
However, you *can* dynamically change how individual citations are presented in the text using different **roles**.

For example, you can mix parenthetical citations, textual citations, and footnote citations in the exact same paragraph:

::::{tab-set}
:::{tab-item} md

* **Parenthetical:** `{cite:p}` renders as `[Smith 2023]` or `[1]`
* **Textual:** `{cite:t}` renders as `Smith [2023]` or `Smith [1]`
* **Footnote:** `{footcite}` renders as a footnote marker `[1]`
:::

:::{tab-item} rst

* **Parenthetical:** `:cite:p:` renders as `[Smith 2023]` or `[1]`
* **Textual:** `:cite:t:` renders as `Smith [2023]` or `Smith [1]`
* **Footnote:** `:footcite:` renders as a footnote marker `[1]`
:::
::::

Here is an example:

::::{tab-set}

:::{tab-item} md

```md
According to {cite:t}`smith2023`, the algorithm is highly efficient. 
Other researchers have found similar results {cite:p}`doe2021, johnson2022`. 
We also want to note this secondary finding {footcite:p}`adams2019`.

```{footbibliography}
```

:::

:::{tab-item} rst

```rst
According to :cite:t:`smith2023`, the algorithm is highly efficient. 
Other researchers have found similar results :cite:p:`doe2021, johnson2022`. 
We also want to note this secondary finding :footcite:p:`adams2019`.

.. footbibliography::
```

:::

::::

## Bibliography lists

You can have multiple bibliography lists in your project (or even on the same page),
each using a completely different styling format (e.g., one list sorted alphabetically, another numbered in order of appearance).
You do this by passing a `:style:` flag to the `.. bibliography::` directive.

### Global options in `conf.py`

These options available in `sphinxcontrib-bibtex`
control the default behaviour for your entire Sphinx project:

* **`bibtex_bibfiles`**: A list of your `.bib` files (e.g., `['refs.bib']`).
* **`bibtex_default_style`**: The global default bibliography style (`alpha`, `plain`, `unsrt`, `unsrtalpha`).
* **`bibtex_reference_style`**: The global inline citation style (`label`, `author_year`, `super`).
* **`bibtex_foot_reference_style`**: The inline style for footnotes (defaults to `foot`).
* **`bibtex_encoding`**: Encoding of your bib files (defaults to `utf-8-sig`).

Here is how you set the global defaults in your `conf.py` file:

```python
extensions = ['sphinxcontrib.bibtex']

# Point to your bib files
bibtex_bibfiles = ['books.bib', 'articles.bib']

# Set global bibliography list style (e.g., unsorted/numeric)
bibtex_default_style = 'unsrt'

# Set global inline citation style (e.g., author-year)
bibtex_reference_style = 'author_year'

```

### Directive options

When generating a reference list using `.. bibliography::`, you can pass these options:

* **`:style:`**: Overrides the global style for this specific list (`alpha`, `plain`, `unsrt`, `unsrtalpha`).
* **`:filter:`**: A Python boolean expression to filter which citations appear in this list (e.g., `docname in docnames` to only show citations referenced on the current page, or `type == 'article'`).
* **`:labelprefix:`**: Prepends a string to the citation labels (useful if you have multiple bibliographies and want to avoid label collisions, e.g., `[A1]`, `[A2]`).
* **`:keyprefix:`**: Prepends a string to the citation keys to prevent duplicate key errors across different scopes.
* **`:list:`**: Changes the HTML list formatting (`bullet` or `enumerated`).

## BibTeX files

The BibTeX files can be managed with Zotero_.
Zotero is available on Windows, Linux, Mac and Android

## Example with different styles

If you want to split your references into two distinct lists on the same page—say,
one for books formatted alphabetically,
and one for articles formatted numerically—you can use the `:style:` and `:filter:` options:

::::{tab-set}

:::{tab-item} md

```md
## References: Books (Alphabetical)
```{bibliography} books.bib
:style: alpha
:filter: type == 'book'
:labelprefix: B-

## References: Articles (Numbered by appearance)
```{bibliography} articles.bib
:style: unsrt
:filter: type == 'article'
:list: enumerated
```

:::
:::{tab-item} rst

```rst
## References: Books (Alphabetical)
.. bibliography:: books.bib
   :style: alpha
   :filter: type == 'book'
   :labelprefix: B-

## References: Articles (Numbered by appearance)
.. bibliography:: articles.bib
   :style: unsrt
   :filter: type == 'article'
   :list: enumerated
```

:::
::::

In this example, any book cited will appear with a prefix like **[B-Smi23]**, while articles will appear in a standard numbered list like **1, 2, 3**, completely independent of each other.

## Using citations as footnotes

The `references.bib` file should contain a BibTex bibliography.  
If your bibliography contains the following entries:

```{code-block} latex
   @Book{Strunk1979,
     title = {The Elements of Style},
     publisher = {Macmillan},
     year = {1979},
     author = {Strunk, Jr., William and E. B. White},
     edition = {Third}
     }
   @Book{1987:nelson,
      author = {Edward Nelson},
      title = {Radically Elementary Probability Theory},
      publisher = {Princeton University Press},
      year = {1987}
      }
```

This is how you can use it in the text.

::::{tab-set}

:::{tab-item} md

```{code-block} md

    If you are using Markdown do the citations like this:
    see {cite}`Strunk1979` for an introduction to stylish blah, blah...

    There are also the variations. 
    For example, this one shows the authors names before the citation, which appears as a footnote {footcite:t}`1987:nelson`. 

    And place the bibliography directive at the end of the document,
    where the bibliography should appear. (It can also go to a separate document.)

    ---

    ```{footbibliography}
```

:::
:::{tab-item} rst

```{code-block} rst

    If you are using Markdown do the citations like this:
    see :cite:`Strunk1979` for an introduction to stylish blah, blah...

    There are also the variations. 
    For example, this one shows the authors names before the citation, which appears as a footnote :footcite:t:`1987:nelson`. 

    And place the bibliography directive at the end of the document,
    where the bibliography should appear. (It can also go to a separate document.)

    .. footbibliography:: 
```

:::

::::

*And here is the result:*

If you are using Markdown do the citations like this:
see {cite}`Strunk1979` for an introduction to stylish blah, blah...

There are also the variations.
For example, this one shows the authors names before the citation, which appears as a footnote {footcite:t}`1987:nelson`.

And place the bibliography directive at the end of the document,
where the bibliography should appear. (It can also go to a separate document.)

---

```{footbibliography}
```
