Building the documentation locally
================================== 

Quickstart
-------------------

`Sphinx`_ is a Python documentation generator.

If you are using the `wiseEnvironment` Conda environment, Sphinx should already be installed.
Just open the Anaconda Prompt, activate the wiseEnvironment, and navigate to the repository and folder where you have your docs.

If you want to start from scratch with an empty project,
Sphinx comes with a script called `sphinx-quickstart` that sets up a source directory 
and creates a default `conf.py` with the most useful configuration values from a few questions it asks you: 

.. code-block:: bash

   sphinx-quickstart

The script creates an `index.rst` file. You can open it and add some text there...

Otherwise, the fastest way is to simply make a copy of this documentation and modify it as you want.

.. warning::
   Some of the functionality described in these pages 
   depends on the use of the `PyData theme`_ 
   and of a set of Sphinx extensions that are already defined in the project's `conf.py`.
   The instalation and configuration of those extensions are not described here.  

   The look-and-feel of the WISE dataflows documentation should be identical, 
   so there is no strong reason to modify the theme or the configuration.


"Live build" 
----------------------------------------------------

.. note::

   This is the recommended option during development.

If you are actively writing or editing documentation, the best way to preview your changes is using `sphinx-autobuild`. 
This will start a local web server and automatically refresh your browser whenever you save a file.

*  **Start the autobuild server.**  

   Navigate to the root of your project and run:

   .. code-block:: bash

      sphinx-autobuild docs docs/_build/html

   *(Note: If your Sphinx source files are in a different directory than `**docs**`, adjust the paths accordingly).*

*  **View the docs:**  

   Open your web browser and navigate to the local URL provided in the terminal (usually `http://127.0.0.1:8000`).

*  Use `CTRL+C` to stop the autobuild.

*  If port 8000 is already in use by another application, use another...: 

   .. code-block:: bash

      sphinx-autobuild docs docs/_build/html --port 9000

Standard HTML Build
-----------------------------

If you just want to generate the static HTML files once without starting a persistent server, you can use the standard build command.

*  **Build the HTML files:**  

   Navigate to your documentation directory (usually `docs/`) and run:

   .. code-block:: bash

      .\make.bat html

*  **View the docs**  

   Open the generated `index.html` file in your browser. You can typically find it at:

   .. code-block:: 
      
      docs/_build/html/index.html

.. links-placeholder

.. include:: ../_sharedFiles/Links.rst      
