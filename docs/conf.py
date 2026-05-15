# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys, os

# Check if this is on ReadTheDocs, which sets a specific environment variable
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

extensions = ['sphinx.ext.autodoc',
                'myst_parser',
                'sphinx.ext.todo', 
                #'sphinx.ext.imgmath', 
                'sphinx.ext.mathjax', 
                'sphinx.ext.graphviz', 
                'sphinxcontrib.bibtex', 
                'sphinxcontrib.mermaid', 
                'sphinxcontrib.sqltable',
                'nbsphinx',
                'sphinx_design']

bibtex_bibfiles = ['./_sharedFiles/Bibliography.bib']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','*.txt']

# NUMBERING - begin config

numfig = True

numfig_format = {
    'figure': 'Figure %s',       # Changes "Fig. 1" to "Figure 1"
    'table': 'Table %s',    
    'code-block': 'Example %s',  # Changes "Listing 1" to "Example 1"
    'section': 'Section %s',     
}

    # The separator must defined in a custom.css

# NUMBERING - end config

# MERMAID DIAGRAMS - begin config

mermaid_init_js = """
mermaid.initialize({theme:"neutral"});
"""

# MERMAID DIAGRAMS - end config

# SYNTAX HIGHLIGHTING - The name of the Pygments style to use.
pygments_style = 'sphinx'

# Support for todo items: If this is True, todo and todolist produce output, else they produce nothing. The default is False.
todo_include_todos = True

# MATH - Tell MyST to allow dollar signs and advanced math blocks
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "colon_fence"
]

# SQLTABLE - configure the default connection if there is one

#sqltable_connection_string = ''

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'pydata_sphinx_theme'
#html_theme = 'sphinx_rtd_theme'
html_show_copyright = False
# The _static folder is where you place files that should be copied as-is to your final build output (_build/html/_static). It is commonly used for:
# Custom.css: To override the default theme colors or fonts.
# Logos/Favicons: Images referenced directly in your theme configuration.
# JavaScript: Scripts for custom interactivity not provided by extensions.
html_static_path = ['_static']
html_css_files = [
   'customTable.css'
]


html_theme_options = {
    "logo": {
        "alt_text": "WISE Documentation",
        "text": "Docs-as-Code",
    }
}

html_logo = "_static/wise.svg"

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'WISE'
copyright = '2013-2026. These pages aggregate content from multiple sources (refer to the metadata).'
author = 'Fernanda Nery'
version = '0.1'
