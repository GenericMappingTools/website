import datetime
import sphinx_bootstrap_theme

# Sphinx project configuration
templates_path = ["_templates"]
exclude_patterns = ["_build"]
source_suffix = ".rst"
master_doc = "index"

# General information about the project
year = datetime.date.today().year
project = "Generic Mapping Tools"
copyright = "{:d}, The GMT Developers".format(year)
version = ""

html_title = project
html_short_title = ""
html_logo = "_static/gmt-logo.png"
html_favicon = "_static/favicon.png"
html_static_path = ["_static"]
html_extra_path = [".nojekyll"]
html_use_smartypants = True
pygments_style = "default"
add_function_parentheses = False
html_add_permalinks = ""
# Custom sidebar templates, maps document names to template names.
html_sidebars = {}
# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}
# If false, no module index is generated.
# html_domain_indices = True
# If false, no index is generated.
# html_use_index = True
# If true, the index is split into individual pages for each letter.
# html_split_index = False
# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True
# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True
# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True
# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''
# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None
# Output file base name for HTML help builder.
# htmlhelp_basename = ""

# Theme config
html_theme = "bootstrap"
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_theme_options = {
    "bootswatch_theme": "flatly",
    "navbar_title": "",
    "navbar_site_name": "Site",
    "navbar_links": [
        ("Home", "/", True),
        ("About", "about/", True),
        ("Download", "download/", True),
        ("Workshops", "workshops/", True),
        ("Documentation", "https://docs.generic-mapping-tools.org", True),
    ],
    # Render the next and previous page links in navbar. (Default: true)
    "navbar_sidebarrel": False,
    # Render the current pages TOC in the navbar. (Default: true)
    "navbar_pagenav": False,
    # Tab name for the current pages TOC. (Default: "Page")
    "navbar_pagenav_name": "This page",
    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    "globaltoc_depth": 1,
    # Include hidden TOCs in Site navbar?
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    # Values: "true" (default) or "false"
    "globaltoc_includehidden": "false",
    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    "navbar_class": "navbar navbar-default",
    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    "navbar_fixed_top": "false",
    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    "source_link_position": "footer",
    "bootstrap_version": "3",
}
html_context = {
    "social_links": [
        (
            '<i class="fab fa-github fa-lg"></i>',
            "GitHub",
            "https://github.com/GenericMappingTools",
        ),
        (
            '<i class="fab fa-gitter fa-lg"></i>',
            "Gitter chat",
            "https://gitter.im/GenericMappingTools/Lobby",
        ),
    ],
    "url": "https://www.generic-mapping-tools.org/website",
}


# Load the custom CSS files (needs sphinx >= 1.6 for this to work)
def setup(app):
    app.add_stylesheet("style.css")
    app.add_stylesheet("fontawesome/css/all.css")
