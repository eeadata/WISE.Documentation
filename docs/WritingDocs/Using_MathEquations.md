---
title: Mathematical equations
author: Nery, Fernanda
date: 2013-10-01
description: Overview of some available alternatives for producing and including equations in Sphinx.
---

(heading_using_mathequations)=
# Using mathematical equations

## LaTeX

The syntax for writing equations is LaTeX. See some examples below.

LaTeX has a steep learning curve, so you may want to check online documentation, for example [Overleaf's LaTeX mathematical expressions guide](https://www.overleaf.com/learn/latex/Mathematical_expressions).

Given that LaTeX syntax may be daunting, a WYSIWYG math editor can be useful, or at least an interactive previewer like [latex4technics](https://www.latex4technics.com/).

## MathJax

In Sphinx, the rendering (display) of the equations can be done in different ways, which won't be discussed here.

The selected option is to use the `sphinx.ext.mathjax` extension. This extension uses the JavaScript package [MathJax](https://www.mathjax.org/) to transform the LaTeX markup to readable math live in the browser.

The `mathjax_path` in the `conf.py` file indicates where the MathJax library resides. By default, this is the MathJax site, but the path can be changed if cross-site scripting is NOT allowed.


## Math examples

### Inline equation

::::{tab-set}
:::{tab-item} output

If $\sigma_{1}$ equals $\sigma_{2}$ then etc, etc.

:::
:::{tab-item} md

```md
If $\sigma_{1}$ equals $\sigma_{2}$ then etc, etc.
```

:::
:::{tab-item} rst

```rst
If :math:`\sigma_{1}` equals :math:`\sigma_{2}` then etc, etc.
```

:::
::::

### Inline equation with subscript and superscript

::::{tab-set}
:::{tab-item} output

$\underline{x}=[  x_{1}, ...,  x_{n}]^{T}$

:::
:::{tab-item} md

```md
$\underline{x}=[  x_{1}, ...,  x_{n}]^{T}$
```

:::
:::{tab-item} rst

```rst
:math:`\underline{x}=[  x_{1}, ...,  x_{n}]^{T}`
```

:::
::::

### Block equation

::::{tab-set}
:::{tab-item} output

$$
\langle \alpha, \beta  \rangle 
\in 
\Biggl \lbrace 
{ 
M,\text{ if } 
   {
    l(\underline{x}) = 
      \frac { p(\underline{x}|M ) } { p(\underline{x}|U) } 
      \geq
       \frac { p(U) }{ p(M) } }
   \atop 
   U, \text{ otherwise } 
   }
$$

:::
:::{tab-item} md

```md
$$
\langle \alpha, \beta  \rangle 
\in 
\Biggl \lbrace 
{ 
M,\text{ if } 
   {
    l(\underline{x}) = 
      \frac { p(\underline{x}|M ) } { p(\underline{x}|U) } 
      \geq
       \frac { p(U) }{ p(M) } }
\atop 
U, \text{ otherwise } 
}
$$
```

:::
:::{tab-item} rst

```rst
.. math::

   \langle \alpha, \beta  \rangle 
   \in 
   \Biggl \lbrace 
   { 
   M,\text{ if } 
      {
       l(\underline{x}) = 
         \frac { p(\underline{x}|M ) } { p(\underline{x}|U) } 
         \geq
          \frac { p(U) }{ p(M) } }
   \atop 
   U, \text{ otherwise } 
   }
```

:::
::::

## How to label and cross-reference equations

* To add a label to an equation:

::::{tab-set}
:::{tab-item} output

$$
e^{i\pi} + 1 = 0
$$ (euler-identity)

:::
:::{tab-item} md

```md
$$
e^{i\pi} + 1 = 0
$$ (euler-identity)
```

:::
:::{tab-item} rst

```rst
.. math::
   :label: euler-identity

   e^{i\pi} + 1 = 0
```

:::
::::

* Once labeled, you can reference the equation anywhere in your documentation using the Sphinx `eq` role.

::::{tab-set}
:::{tab-item} output

As shown in equation {eq}`euler-identity`, the relationship between the fundamental mathematical constants is elegant.

:::
:::{tab-item} md

```md
As shown in equation {eq}`euler-identity`, 
the relationship between the fundamental mathematical constants is elegant.
```

:::
:::{tab-item} rst

```rst
As shown in equation :eq:`euler-identity`, 
the relationship between the fundamental mathematical constants is elegant.
```

:::
::::

By default, Sphinx only numbers equations that have a label attached to them. If you want Sphinx to assign a number to every block equation in your documentation (even the ones you haven't labeled), you can add this line to your `conf.py`:

```python
math_number_all = True
```

```{warning}
Technically, the numbering of equations does not use the same numbering engine as the numbering of tables, figures, and code-blocks.

* For equations, one must use the `:label:` option / `(label-name)` and the `{eq}` role.
* For tables and figures, one must use the `:name:` option and the `{numref}` role.

It is how it is...
```
