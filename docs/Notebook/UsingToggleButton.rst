.. _heading-toggle-button:

Using a toggle button
======================

The sphinx-togglebutton_ extension allows text to be hidden.

Colapse warnings, admonitions,...
----------------------------------

This code...

..  code-block:: rst

    .. admonition:: Click the title to toggle
       :class: dropdown

    This title was made into a dropdown admonition by adding `:class: dropdown` to it.

... creates this result:

..  admonition:: Click the title to toggle
    :class: dropdown

    This title was made into a dropdown admonition by adding `:class: dropdown` to it.

Toggle text
-------------

..  toggle::

    This is a toggled content block!

This is the code (also hidden in a toggle...):

..  toggle::
    
    ..  code-block:: rst

        ..  toggle::

            This is a toggled content block!

.. links-placeholder

.. include:: ../_sharedFiles/Links.rst
            