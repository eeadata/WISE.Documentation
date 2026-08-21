
Publishing to GitHub Pages
==========================

Use `GitHub Desktop` to create a git repository in your local project folder, and push it to GitHub.

Once your documentation is ready to be shared, you can automatically publish it using GitHub Pages. 
You can only use GitHub Pages over **public** repositories (unless you have an entreprise account).

The best way to do this is by setting up a GitHub Actions workflow 
that automatically builds and deploys your HTML files whenever you push changes to your main branch.

*  **Create a GitHub Actions workflow**  

   Create a new configuration file in your repository at `.github/workflows/documentation.yml`.  
   Use the configuration in the `documentation.yml` file 
   that you can download :download:`here <src/documentation.yml>`.

   The `documentation.yml` points to a  `docs/requirements.txt` file 
   that you can download :download:`here <../requirements.txt>`.
   (If you put the requirements.txt file in another folder, you'll need to modify the documentation.yml file...)

*  **Configure your repository settings**  

   Once the action runs for the first time, it will create a new branch called `gh-pages`.

   *  Go to your repository on GitHub.
   *  Navigate to **Settings** > **Pages**.
   *  Under **Build and deployment**, set the **Source** to "Deploy from a branch".
   *  Select the `gh-pages` branch and the `/ (root)` folder, then click **Save**.

Your documentation will now be publicly accessible at `https://<your-username>.github.io/<your-repository-name>/`.

.. warning::

   Before publishing your documentation, make sure to review it locally and ensure that it is accurate and up-to-date. 
   Once published, the documentation will be publicly accessible, so it's important to verify its quality beforehand.

   Make sure that your WISE project manager is aware of the publication and has approved the content,
   specially is it is being published in an organisational repository.

.. links-placeholder

.. include:: ../_sharedFiles/Links.rst
            