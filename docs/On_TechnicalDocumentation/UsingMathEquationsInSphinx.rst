:tocdepth: 2

.. highlight:: rst

.. metadata-placeholder

   :DC.Title:
      Mathematical equations
   :DC.Creator:
      Nery, Fernanda
   :DC.Date:
      2013-10-01
   :DC.Description:
      Overview of some available alternatives for
      producing and including equations in Sphinx.
      
      See http://sphinx-doc.org/ext/math.html
   :DC.Language:
      en
   :DC.Format:
      text/x-rst
   :DC.Rights:
      Public.

Mathematical equations
**********************

.. contents:: On this page...
   :depth: 3
   :local:

LaTeX
=====

The syntax for writing equations is LaTeX.
See some examples below.

LaTeX has a steep learning curve, so you may want to check online documentation,
for example https://www.overleaf.com/learn/latex/Mathematical_expressions. 

MathJax
=======

In Sphinx, the rendering (display) of the equations
can be done in different ways, that won't be discussed here.

The selected option is to use the ``sphinx.ext.mathjax`` extension.
This extension uses the JavaScript package MathJax_
to transform the LaTeX markup to readable math live in the browser.

The ``mathjax_path`` in the ``conf.py`` file
indicates where the MathJax library resides.

By default, this is the MathJax site,
but the path can be changed cross-site scripting is NOT allowed.

Equation editors
================

Given that LaTeX syntax may be daunting,
a WYSIWYG math editor can be useful, 
or at least an interactive previewer like https://www.latex4technics.com/.

Math examples
==============

Code:: 

      If :math:`\sigma_{1}` equals :math:`\sigma_{2}` then etc, etc. 
   
Output:

      If :math:`\sigma_{1}` equals :math:`\sigma_{2}` then etc, etc.

Code:: 

      :math:`\underline{x}=[  x_{1}, ...,  x_{n}]^{T}`
      
Output:

      :math:`\underline{x}=[  x_{1}, ...,  x_{n}]^{T}`

Code:

.. code-block:: latex
   
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

Output:

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


How to label and cross-reference equations in reStructuredText
==============================================================

*  To add a label to an equation in reST, use the `:label:` option inside the `.. math::` directive.

   Code::

      .. math::
         :label: euler-identity

         e^{i\pi} + 1 = 0


   Output:

      .. math::
         :label: euler-identity

         e^{i\pi} + 1 = 0

*  Once labeled, you can reference the equation anywhere in your documentation 
   using the Sphinx `:eq:` role.

   Code::

       As shown in equation :eq:`euler-identity`, 
       the relationship between the fundamental mathematical constants is elegant. 

   Output:

   As shown in equation :eq:`euler-identity`, 
   the relationship between the fundamental mathematical constants is elegant.

By default, Sphinx only numbers equations that have a label attached to them. 
If you want Sphinx to assign a number to every block equation in your documentation 
(even the ones you haven't labeled), you can add this line to your conf.py:

.. code-block:: python

   math_number_all = True
   
.. warning::

   Technically, the numbering of equations does not use the same numbering engine as the numbering of tables, figures, and code-blocks.

   For equations, one must use the `:label:` option and the `:eq:` role.
   
   For tables and figures, one must use the `:name:` option and the `:numref:` role.

   It is how it is...

.. links-placeholder

.. include:: ../_sharedFiles/Links.rst
