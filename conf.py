# -- fix for sphinxcontrib-googleanalytics------------------------------------

import sphinx.application
import sphinx.errors

sphinx.application.ExtensionError = sphinx.errors.ExtensionError

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'A.T.O.M\'s Wiki'
copyright = '2022, A.T.O.M'
author = 'A.T.O.M'
release = '0.0.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.githubpages', 'myst_parser', 'sphinxcontrib.googleanalytics']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Aditional configuration -------------------------------------------------

version = u'0.0.3'
master_doc = 'index'
pygments_style = 'sphinx'

html_favicon = "https://github.com/atom-robotics-lab/assets/blob/main/logo_with_background.jpg?raw=true"

googleanalytics_id = 'G-79B58JVRHB'
googleanalytics_enabled = True