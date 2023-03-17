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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Papermerge DMS'
copyright = '2020-2023, Papermerge DMS'
author = 'Eugen Ciur'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_multiversion",
]

# Match as remote branch any git ref of following format.
# Some examples:
#  origin/2.0.x   # 2.0.x branch
#  origin/2.1.x   # 2.1.x branch
#  origin/master  # master branch
smv_remote_whitelist = r'^(origin)$'  # remote ref format
smv_branch_whitelist = r'^(\d+\.\d+\.[\d+x]|master)$'  # branch format

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
html_theme = "sphinx_rtd_theme"

rst_prolog = """
.. |project| replace:: Papermerge DMS
.. |backend_version| replace:: 2.1.8
"""

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_style = 'custom.css'
