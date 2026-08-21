Setting up the wiseEnvironment
==============================

.. warning::
   
   This section has been simplified and only describes the procedure in Windows systems...

*  Make sure you have Anaconda_ available on your system.

   This project uses Conda_ to manage its dependencies and ensure a reproducible workflow.   

   All required packages for data analysis and documentation are specified in the `environment.yml` file 
   that you can download :download:`here <src/environment.yml>`.

*  Open the Anaconda Prompt or the Anaconda PowerShell

.. important::
   If you're using a remote desktop connection to the CWS,
   check if the `wiseEnvironment` already exists, using: 
   
   .. code-block:: bash

      conda env list

   As stated above, the `wiseEnvironment` includes Sphinx_ 
   and some extensions needed to add specific functionality to the WISE documentation.
   It also includes several other Python_ packages for data analysis 
   (which you don't actually need if you're just creating documentation).
   Anyway, if the environment already exists, use it.

*  Navigate to the root directory of the project where the `environment.yml` file was copied to:

   .. code-block:: bash

      cd /d path/to/your/project

*  Run the following command to build the environment if it doesn't already exist. 
   This will download and install all the packages required for the project:

   .. code-block:: bash

      conda env create -f environment.yml

*  This process may take a few minutes, depending on your internet connection and the number of packages being installed.  
   Conda will handle all dependencies and ensure that the environment is set up correctly.

   Once the installation finishes, you need to activate the environment before running any scripts:

   .. code-block:: bash

      conda activate wiseEnvironment

*  You should now see `(wiseEnvironment)` at the beginning of your terminal prompt.

Updating the environment
------------------------

If the project's dependencies change and the `environment.yml` file is updated, 
you can refresh your local setup without recreating it from scratch by running:

.. code-block:: bash

   conda env update -f environment.yml --prune

Where are environments created?
-----------------------------------

By default, Conda looks at your `envs_dirs` configuration to decide where to put new environments. 
If you want them strictly in `~/.conda/envs` (or whatever your prefered path is), 
you need to tell Conda that this path is your top priority.

.. code-block:: bash

   conda config --prepend envs_dirs ~/.conda/envs

To make sure Conda heard you loud and clear, check your configuration:

.. code-block:: bash

   conda config --show envs_dirs

The output should list `~/.conda/envs` (or the full path equivalent) at the very top.  

.. links-placeholder

.. include:: ../_sharedFiles/Links.rst
