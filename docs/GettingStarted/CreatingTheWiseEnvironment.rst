Setting up the wiseEnvironment
==============================

*  Make sure you have Anaconda_ available on your system (or **Miniconda** or **Mamba**).  

   This project uses Conda_ to manage its dependencies and ensure a reproducible workflow.   

   All required packages for data analysis and documentation are specified in the `environment.yml` file 
   that you can download :download:`here <src/environment.yml>`.

*  Open the Anaconda PowerShell (Windows) or your terminal of choice (Linux/Mac).  

   .. important::
      If you're using a remote desktop connection to the CWS,
      check if the `wiseEnvironment` already exists, using: 
      
      .. code-block:: bash

         conda env list


*  Navigate to the root directory of the project where the `environment.yml` file was copied to:

   .. code-block:: bash

      cd path/to/your/project

*  Run the following command to build the environment. This will download and install all the exact package versions required for the project:

   .. code-block:: bash

      conda env create -f environment.yml

   Or, if you're pointing directly to the `environment.yml` file in this repository, use:

   .. code-block:: bash

      conda env create -f https://raw.githubusercontent.com/eeadata/WISE.Documentation/refs/heads/main/docs/GettingStarted/src/environment.yml

   
   *(Note: If you use `mamba`, replace `conda` with `mamba` for a significantly faster installation).*      

*  This process may take a few minutes, depending on your internet connection and the number of packages being installed.  
   Conda will handle all dependencies and ensure that the environment is set up correctly.

   Once the installation finishes, you need to activate the environment before running any scripts:

   .. code-block:: bash

      source activate wiseEnvironment


*  You should now see `(wiseEnvironment)` at the beginning of your terminal prompt.

Updating the environment
------------------------

*  If the project's dependencies change and the `environment.yml` file is updated, 
   you can refresh your local setup without recreating it from scratch by running:

   .. code-block:: bash

      conda env update -f environment.yml --prune

*  Same as above, you can point directly to the `environment.yml` file in this repository:
  
   .. code-block:: bash

      conda env update -f https://raw.githubusercontent.com/eeadata/WISE.Documentation/refs/heads/main/docs/GettingStarted/src/environment.yml --prune

Where are environments created?
-----------------------------------

By default, Conda looks at your `envs_dirs`` configuration to decide where to put new environments. 
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
