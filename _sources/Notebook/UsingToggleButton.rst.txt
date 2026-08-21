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


Hidding a long table
--------------------

Long tables make the documents akward to read.

Let's test with a short table:

..  csv-table:: User list
    :name: hidden-table-example
    :header: "First name","Last name"

    "John","Doe"
    "Jane","Dove"

Let's check if they can be hidden using `toggle`:

..  toggle:: 

    ..  csv-table:: User list
        :name: hidden-table-example-1
        :header: "First name","Last name"
    
        "John","Doe"
        "Jane","Dove"


To show a different text, we need to use an `admonition` with a caption:

..  admonition:: The table with the user list
    :class: dropdown

    ..  csv-table:: User list
        :name: hidden-table-example-2
        :header: "First name","Last name"
    
        "John","Doe"
        "Jane","Dove"


The admonition caption can even reference something 
in the hidden content, using `numref` and `ref` 
in the caption of the `admonition` 
but it becomes too convoluted... 

..  admonition::  :numref:`hidden-table-example-3` - :ref:`hidden-table-example-3` (this looks weird)
    :class: dropdown

    ..  csv-table:: User list
        :name: hidden-table-example-3
        :header: "First name","Last name"
    
        "John","Doe"
        "Jane","Dove"


..  caution::
    Search for collapsible tables?

    Can `:class: dropdown` be applied to normal tables?

    No. Not directly. To be continued when time allows.

..  csv-table:: User list
    :class: dropdown
    :name: hidden-table-example-4
    :header: "First name","Last name"

    "John","Doe"
    "Jane","Dove"




.. links-placeholder

.. include:: ../_sharedFiles/Links.rst
            