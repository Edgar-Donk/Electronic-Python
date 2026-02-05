# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
#import os
#import sys
#sys.path.append(os.path.abspath('../')) # sys.path.insert(0, os.path.abspath('.'))
#import pydata_sphinx_theme

# -- Project information -----------------------------------------------------

project = 'Arduino and Python'
copyright = '2020, Edga Donk'
author = 'Edga Donk'

# The full version, including alpha/beta/rc tags
release = '0.0'

# stops looking for non-existant contents.rst
master_doc = 'index'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [#'sphinx.ext.todo',
              'sphinx.ext.autodoc',
              #'hidden_code_block'
              "sphinx.ext.autosummary",
              #"numpydoc",
              'sphinx.ext.mathjax',
			  'sphinx.ext.autosectionlabel',
			  'sphinx_copybutton'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme_path = ['..']
html_theme = "pydata_sphinx_theme" # "sphinx_rtd_theme" # "sphinxdoc" # 'alabaster'
#html_theme_path = pydata_sphinx_theme.get_html_theme_path()

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme_options = {

  #"github_url": "https://github.com/pandas-dev/pydata-sphinx-theme",
  "show_prev_next": True,
  # search bar options are ‘navbar’ and ‘sidebar’.
  "search_bar_position": "sidebar",
  #  "use_edit_page_button": True,
  #'display_version': True,
    #'prev_next_buttons_location': 'both',
    #'logo_only': False,
    #'style_nav_header_background': '#98dbcc',
    #'style_external_links': True,
    # Toc options
    #'collapse_navigation': False,
    #'sticky_navigation': True,
    #'navigation_depth': 3,
    #'includehidden': True,
    #'titles_only': False
}

html_sidebars = {
'''    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html'

    ]
}
'''
"contributing": ["sidebar-search-bs.html", "custom-template.html"],
    "changelog": [],
}

# option for show/hide code
def setup(app):
    app.add_css_file('custom.css')

html_context = {
    "github_user": "pandas-dev",
    "github_repo": "pydata-sphinx-theme",
    "github_version": "master",
    "doc_path": "docs",
}

# html_logo = '_static/ben2.png' #ben1.png

html_theme_options = {
   "logo": {
      "text": "electronic python",
      "image_light": 'bigbenc.avif',
      "image_dark": "bigbencneon.avif",
   }
}

html_favicon = '_static/ben1.ico'

smartquotes = False

rst_prolog = f"""
.. role:: AL
    :class: keys
"""
