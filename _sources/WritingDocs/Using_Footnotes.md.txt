(footnotes-ref)=
# Using footnotes

First of all, **do not number your footnotes**.

Sphinx will create the numbers for you. 
Give each footnote a unique and descriptive name. 
You can reference a footnote several times in the text, using the descriptive name.

::::{tab-set}
:::{tab-item} rst

```{code-block} rst
You can use footnotes [#what-is-a-footnote]_ 
that always appear at the end of the page.
I don't think you can place them all together
in a separate page, like a global place with endnotes [#what-is-an-endnote]_

You can put the footnotes' text at the end of the file,
or simply write them in the middle of the text.

.. rubric:: Footnotes

.. [#what-is-a-footnote] A footnote appears at the bottom of a page.
.. [#what-is-an-endnote] An endnote appear at the end of a document.
```

:::
:::{tab-item} md

```{code-block} md
You can use footnotes [^what-is-a-footnote] 
that always appear at the end of the page.
I don't think you can place them all together
in a separate page, like a global place with endnotes [^what-is-an-endnote]

You can put the footnotes' text at the end of the file,
or simply write them in the middle of the text.

[^what-is-a-footnote]: A footnote appears at the bottom of a page.
[^what-is-an-endnote]: An endnote appear at the end of a document.
```

:::
::::
