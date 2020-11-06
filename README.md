# Source for the GMT website

[![build-html](https://github.com/GenericMappingTools/website/workflows/build-html/badge.svg?event=push)](https://github.com/GenericMappingTools/website/actions?query=workflow%3Abuild-html)

This repository contains the sphinx source files for building the GMT website.

## Compiling the site

Run:

    make

Pushing changes to
[GenericMappingTools/website](https://github.com/GenericMappingTools/website)
triggers a [GitHub Actions workflow](.github/workflows/build.yml).
When changes are pushed to the `master` branch (directly or by merging a Pull
Request), Github Actions will push the compiled site to the
[GenericMappingTools/genericmappingtools.github.io](https://github.com/GenericMappingTools/genericmappingtools.github.io)
repository.
Github serves this repository under
[http://genericmappingtools.github.io](http://genericmappingtools.github.io/).

## License

[![Creative Commons
License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
This work is licensed under a
[Creative Commons Attribution 4.0 International
License](http://creativecommons.org/licenses/by/4.0/).
