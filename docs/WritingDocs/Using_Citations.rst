.. _rst-citations-ref:  

Using citations
---------------

Citations are similar footnotes,
but have a label that is not numeric or begins with ``#``.

When the documentation is built using the Sphinx  document generator,
the citations are "global",
meaning that every citation can be referenced from any .rst files.
In this case, a separate file may be created (e.g. a ``references.rst`` file).

.. tab-set::

   .. tab-item:: rst

      .. code-block:: rst
        
        You can find more information in the guidance [GuidanceDoc]_.

        .. [GuidanceDoc] EEA (2026). The ultimate Guidance Document. 100pp.

   .. tab-item:: md

      There is no equivalent in Markdown.
      See 

