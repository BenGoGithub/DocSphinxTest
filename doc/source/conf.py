# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
print("Current sys.path:")
for p in sys.path:
    print(p)

project = 'DocSphinxTest'
copyright = '2025, BG'
author = 'BG'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['autoapi.extension',
              'sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinx.ext.viewcode',
              'sphinx_rtd_theme',
              'sphinx.ext.autosummary',
              ]


napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Configuration de l'autoapi apidoc
autoapi_generate_api_docs = True
# Active la génération automatique de la documentation de l'API

autoapi_dirs = ["../../vehicles"]
# Spécifie le répertoire où se trouvent les fichiers Python à documenter.
# Ici, on remonte de deux niveaux par rapport au dossier 'doc/source' (où se trouve conf.py)
# pour atteindre la racine du projet, puis on entre dans le dossier 'vehicles'.
# Assurez-vous que le chemin est correct par rapport à l'emplacement de ce fichier conf.py

autoapi_root = "api_reference"
# Définit le répertoire racine où seront générés les fichiers de documentation de l'API.
# Les fichiers seront placés dans 'doc/source/api_reference'.

autoapi_keep_files = True
# Indique si les fichiers générés doivent être conservés après la construction de la documentation.
# Utile pour le débogage et la personnalisation manuelle.

autoapi_options = [
    "members",
    "undoc-members",
    "private-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
]
# Définit les options pour la documentation de l'API.
# "members": inclut les membres (attributs et méthodes) des classes.
# "undoc-members": inclut les membres non documentés.
# "private-members": inclut les membres privés (commençant par un underscore).
# "show-inheritance": affiche l'héritage des classes.
# "show-module-summary": affiche un résumé du module.
# "special-members": inclut les méthodes spéciales (par exemple, __init__, __str__).
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

#  given, this must be the name of an image file (path relative to the
#  configuration directory) that is the favicon of the docs. Modern browsers
#  use this as the icon for tabs, windows and bookmarks. It should be a
#  Windows-style icon file (.ico), which is 16x16 or 32x32 pixels large.
html_favicon = "_static/favicon.png"