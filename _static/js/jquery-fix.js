// Override of sphinx_bootstrap_theme's bundled jquery-fix.js.
//
// The theme loads scripts in this order: jquery, jquery-fix.js,
// bootstrap.min.js, bootstrap-sphinx.js. The upstream jquery-fix.js calls
// jQuery.noConflict(true), which removes *both* window.jQuery and window.$
// before bootstrap.min.js runs. bootstrap.min.js grabs the global `jQuery`
// symbol to attach its plugins (carousel, dropdown, collapse, ...), so it
// crashes immediately and none of them get attached - breaking, among other
// things, the front-page carousel (GenericMappingTools/website#146).
//
// Calling noConflict() without `true` only releases the `$` alias and keeps
// window.jQuery defined, so bootstrap.min.js still works. bootstrap-sphinx.js
// already prefers window.$jqTheme, so behavior for the theme's own script is
// unchanged.
window.$jqTheme = jQuery.noConflict();
