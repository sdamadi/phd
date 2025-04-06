import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

extensions = [
 'sphinx.ext.autodoc',
 'sphinx.ext.viewcode',  # For viewing source code
 'myst_parser',
 'sphinx.ext.mathjax'  # or 'sphinx.ext.imgmath' for PNG rendering
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = []  # Remove static path warning