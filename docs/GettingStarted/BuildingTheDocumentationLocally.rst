Building the documentation locally
================================== 

Sphinx
-------------------

`Sphinx`_ is a Python documentation generator.

If your using the `wiseEnvironment` Conda environment, Sphinx_ should already be installed.
The `wiseEnvironment` includes the `sphinx-autobuild` package, 
which allows you to automatically rebuild and preview your documentation in a web browser as you edit it (see next section).

..
   The Sphinx builder can produce a number of output formats (e.g. HTML, PDF).
   PDF files can be produced using the LaTeX builder (more complicated)
   or using the direct PDF builder called rst2pdf (see below).
..

Before building the documentation, ensure your Conda environment is activated:

.. code-block:: bash

   conda activate wiseEnvironment

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

*  If port `8000` is already in use by another application: 

   .. code-block:: bash

      sphinx-autobuild docs docs/_build/html --port 9000


Standard HTML Build
-----------------------------

If you just want to generate the static HTML files once without starting a persistent server, you can use the standard build command.

*  **Build the HTML files:**  

   Navigate to your documentation directory (usually `docs/`) and run:

   .. code-block:: bash

      make html

   *(On Windows, use `.\make.bat html` instead).*

*  **View the docs**  

   Open the generated `index.html` file in your browser. You can typically find it at:

   .. code-block:: 
      
      docs/_build/html/index.html

.. links-placeholder

.. include:: ../_sharedFiles/Links.rst      