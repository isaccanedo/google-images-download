# Arquivo de configuração para o construtor de documentação Sphinx.
#
# Este arquivo contém apenas uma seleção das opções mais comuns. Por um completo
# lista veja a documentação:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
version = '1.0.1'

source_suffix = '.rst'
master_doc = 'index'

html_static_path = ['_static']

def setup(app):
    app.add_stylesheet('overrides.css')  # may also be an URL

html_context = {
	"display_github": False, # Add 'Edit on Github' link instead of 'View page source'
	"last_updated": True,
	"commit": False,
     }

# -- Project information -----------------------------------------------------

project = 'Google Images Download'
copyright = '2019, Hardik Vasa'
author = 'Hardik Vasa'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bizstyle'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'searchbox.html'] }

