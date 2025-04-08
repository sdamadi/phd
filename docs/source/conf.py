import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'Saeed Damadi PhD'
copyright = '2025, Saeed Damadi'
author = 'Saeed Damadi'


templates_path = ['_templates']
exclude_patterns = []

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',  # For viewing source code
    'myst_parser',
    'sphinx.ext.mathjax'  # or 'sphinx.ext.imgmath' for PNG rendering
]


html_theme = 'sphinx_rtd_theme'
html_static_path = []

myst_enable_extensions = [
    "dollarmath",    # Allow $...$ for math
    "amsmath",       # Allow align environments
]

mathjax3_config = {
    'tex2jax': {
        'inlineMath': [['$', '$'], ['\\(', '\\)']],
        'displayMath': [['$$', '$$'], ['\\[', '\\]']]
    }
}
