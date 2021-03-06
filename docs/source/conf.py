# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'Hamsa Survey'
copyright = '2020, Bruno Ferraz'
author = 'Bruno Ferraz'

# The full version, including alpha/beta/rc tags
release = 'v 0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc','sphinx.ext.inheritance_diagram','sphinx.ext.autosummary','sphinx.ext.todo','sphinx.ext.viewcode', 'rst2pdf.pdfbuilder']
todo_include_todos=True
pdf_documents = [('index', u'hamsaSurvey', u"Hamsa Survey's doc", u'Bruno Ferraz'),]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
import sphinx_theme
html_theme = "stanford_theme"
html_theme_path = [sphinx_theme.get_html_theme_path('stanford-theme')]
# All available themes:
print(sphinx_theme.THEME_LIST)
# >> ['stanford_theme', 'neo_rtd_theme']

# import sphinx_pdj_theme
# html_theme = 'sphinx_pdj_theme'
# htm_theme_path = [sphinx_pdj_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
autodoc_member_order = 'bysource'