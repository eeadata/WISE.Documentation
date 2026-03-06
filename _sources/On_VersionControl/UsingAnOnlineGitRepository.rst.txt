.. metadata-placeholder

:DC.Title:
   Background information on the use of online repositories
:DC.Creator:
   Nery, Fernanda
:DC.Date:
   2014-09-01
:DC.Description:
   Brief introduction to online git repositories.
   Based on:
   http://intermediaware.com/blog/how-to-use-dropbox-as-a-git-repository
   https://freshmob.com.au/using-dropbox-as-a-git-repository/
   http://viralpatel.net/blogs/dropbox-svn-subversion-repository/
:DC.Language:
   en
:DC.Format:
   text/x-rst
:DC.Rights:
   Public.

Setting up an online Git Repository using Github
*************************************************


1. Create a GitHub account and a new repository "projectXPTO"

2. Install Git in your computer
   and set the global configuration (usig Git Bash)::

   $ git config --global user.name "johndoe"
   $ git config --global user.email johndoe@example.com

3. Create a local git repository::

   $ mkdir /path/to/your/project
   $ cd /path/to/your/project
   $ git init

4. Link the remote git repository to your local repository::

   $  git remote add origin https://github.com/johndoe/projectXPTO.git

5. Add a ReadMe file::

   $ echo "# This is my README" >> README.md
   $ git add README.md
    
6. Commit and push the first change::

   $ git commit -m "First commit. Adding a README."
   $ git push -u origin master


.. links-placeholder

.. include:: ../_sharedFiles/Links.rst
