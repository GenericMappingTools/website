import datetime
import sphinx_bootstrap_theme

# Sphinx project configuration
templates_path = ["_templates"]
exclude_patterns = ["_build"]
source_suffix = ".rst"
master_doc = "index"

# General information about the project
year = datetime.date.today().year
project = "The Generic Mapping Tools"
copyright = "2019 - {:d}, The GMT Developers".format(year)
version = ""

html_title = project
html_short_title = ""
html_logo = "_static/gmt-logo.png"
html_favicon = "_static/favicon.png"
html_static_path = ["_static"]
html_extra_path = [".nojekyll", "CNAME", "team.html"]
html_use_smartypants = True
pygments_style = "default"
html_add_permalinks = ""

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
            '<i class="fab fa-twitter fa-lg"></i>',
            "Twitter",
            "https://twitter.com/gmt_dev",
        ),
        (
            '<i class="fab fa-youtube fa-lg"></i>',
            "YouTube",
            "https://www.youtube.com/channel/UCo1drOh0OZPcB7S8TmIyf8Q",
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


# Load the custom CSS files (needs sphinx >= 1.6 for this to work)
def setup(app):
    app.add_css_file("style.css")
    app.add_css_file("fontawesome/css/all.css")
