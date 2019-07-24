# -*- coding: utf-8 -*-
import datetime
import sphinx_bootstrap_theme

extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
]

pygments_style = 'default'

# Sphinx project configuration
templates_path = ['_templates']
exclude_patterns = ['_build']
source_suffix = '.rst'
source_encoding = 'utf-8'
master_doc = 'index'

# General information about the project
year = datetime.date.today().year
project = ""
copyright = "{:d}, The GMT Developers".format(year)
version = ""

html_last_updated_fmt = '%b %d, %Y'
html_title = "Generic Mapping Tools"
html_short_title = "GMT"
html_logo = '_static/logo.png'
html_favicon = '_static/favicon.png'
html_static_path = ['_static']
html_extra_path = ['.nojekyll', 'team.html']
html_use_smartypants = True
html_sidebars = {}
# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True
# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True
# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# Theme config
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_theme_options = {
    'bootswatch_theme': "yeti",
    'navbar_title': '',
    'navbar_site_name': "Site",
    'navbar_links': [
        ('About', "about/", False),
        ('<i class="fa fa-github fa-lg" title="Github Organization"></i>',
         "https://github.com/GenericMappingTools", True),
    ],
    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': False,
    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': False,
    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "This page",
    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 1,
    # Include hidden TOCs in Site navbar?
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "false",
    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar navbar-default",
    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "false",
    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "footer",
    'bootstrap_version': "3",
}
# Extra variables that are passed to the template
html_context = {
    "banner_logo": "_static/logo.png",
    "banner_background": "_static/banner.jpg",
}


# Load the custom CSS files (needs sphinx >= 1.6 for this to work)
def setup(app):
    app.add_stylesheet("style.css")
    app.add_stylesheet("font-awesome/css/font-awesome.css")
