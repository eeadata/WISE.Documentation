.. _heading-copy-button:

Using a copy button
======================

The sphinx-copybutton_ extension 
just adds a small copy-to-clipboard button
in the code blocks.

If the project uses both the sphinx-copybutton_ extension
and the nbsphinx_ extension,
then the `conf.py` file should have the following lines.

..  code-block:: python

    # -- Sphinx-copybutton options ---------------------------------------------
    # Exclude copy button from appearing over notebook cell numbers by using :not()
    # The default copybutton selector is `div.highlight pre`
    # https://github.com/executablebooks/sphinx-copybutton/blob/master/sphinx_copybutton/__init__.py#L82
    copybutton_exclude = ".linenos, .gp"
    copybutton_selector = ":not(.prompt) > div.highlight pre"
   
The extension just modifies the normal blocks, 
there is no change to the directives.

.. links-placeholder

.. include:: ../_sharedFiles/Links.rst
            