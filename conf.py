import datetime

import sphinx_bootstrap_theme
from docutils import nodes

# Sphinx project configuration
templates_path = ["_templates"]
exclude_patterns = ["_build"]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
master_doc = "index"

# General information about the project
year = datetime.date.today().year
project = "The Generic Mapping Tools"
copyright = "2019 - {:d}, The GMT Developers".format(year)
version = ""

# Sphinx extensions
extensions = [
    "sphinx.ext.githubpages",
    "myst_parser",
]

myst_enable_extensions = ["colon_fence"]

html_title = project
html_short_title = ""
html_logo = "_static/gmt-logo.png"
html_favicon = "_static/favicon.png"
html_static_path = ["_static"]
html_extra_path = ["CNAME", "team.html"]
html_use_smartypants = True
pygments_style = "default"

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
        ("Mirrors", "mirrors/", True),
        ("Citing", "cite/", True),
        ("Documentation", "documentation/", True),
        ("Ecosystem", "projects/", True),
        ("Workshops", "workshops/", True),
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
            "<strong>Try Online!</strong>",
            "Try Online",
            "https://github.com/GenericMappingTools/try-gmt",
        ),
        (
            "<strong>Forum</strong>",
            "Forum",
            "https://forum.generic-mapping-tools.org/",
        ),
        (
            '<i class="fab fa-github fa-lg"></i>',
            "GitHub",
            "https://github.com/GenericMappingTools",
        ),
        (
            '<i class="fab fa-youtube fa-lg"></i>',
            "YouTube",
            "https://www.youtube.com/c/TheGenericMappingTools",
        ),
        (
            '<i class="fab fa-instagram fa-lg"></i>',
            "Instagram",
            "https://www.instagram.com/genericmappingtools/",
        ),
    ],
    "url": "https://www.generic-mapping-tools.org",
    "last_updated": str(datetime.date.today()),
    "repository": "GenericMappingTools/website",
}


def use_front_matter_title(app, doctree):
    """Use the front matter ``title`` as the title of pages without a heading.

    Sphinx takes the page title from the first section heading and falls back
    to "<no title>" when a page has none, like the landing page. MyST only
    uses the front matter ``title`` if ``myst_title_to_header`` is enabled,
    which would insert a visible heading, so set the title ourselves.
    """
    if doctree.next_node(nodes.section) is not None:
        return  # Sphinx uses the first heading as the title
    docinfo = doctree.next_node(nodes.docinfo)
    if docinfo is None:
        return
    for field in docinfo.findall(nodes.field):
        field_name, field_body = field.children
        if field_name.astext() == "title":
            doctree["title"] = field_body.astext()
            return


# Load the custom CSS files (needs sphinx >= 1.6 for this to work)
def setup(app):
    app.add_css_file("style.css")
    app.add_css_file("fontawesome/css/all.css")
    # Priority < 500 so that it runs before Sphinx collects the page titles
    app.connect("doctree-read", use_front_matter_title, priority=400)
