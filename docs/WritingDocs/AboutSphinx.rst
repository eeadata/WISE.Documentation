About Sphinx
*************************

Sphinx_ is a document generator based on docutils_
(an open-source text processing system, 
for processing plain text documentation into useful formats, 
such as HTML, LaTeX, ODT or XML).

In Sphinx, content (the text) is separated from presentation (formatting):

*  Content is stored in plain text files using a simple markup language 
   (reStructuredText or Markdown). 
   
*  Presentation is defined using themes and templates 
   for each type of output (HTML, LaTeX, PDF).
   
This separation allows the authors to focus on the content 
and not on the presentation or the output format(s).

Also, if the documentation needs to be localised to another language,
the text can be translated (using translation tools, if required),
and all the formatting is applied later 
(without requiring further changes to the localised documents).

Using reStructuredText or using Markdown?
=========================================

reStructuredText_ and Markdown_ are two popular lightweight markup languages.
They are both plain text formats, and can be edited with any text editor.

reStructuredText_ is the markup language used in this project,
and is the default markup language supported by Sphinx_.

Markdown_ is also supported by Sphinx_, but only the CommonMark_ flavour
(supported by GitHub_ and other platforms) is supported.::

      # This is a section in Markdown   This is a section in RST
                                       ========================

      ## This is a subsection           This is a subsection
                                       --------------------

      Nothing special needed for        Nothing special needed for
      a normal paragraph.               a normal paragraph.

                                       ::

         This is a code block          This is a code block

      **Bold** and *emphasized*.        **Bold** and *emphasized*.

      A list:                           A list:
      - this is an item                 - this is an item
      - another item                    - another item

      There is more: images,            There is more: images,
      tables, links, ...                tables, links, ...


.. links-placeholder

.. include:: ../_sharedFiles/Links.rst      