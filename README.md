# Source for the GMT website

[![TravisCI status](http://img.shields.io/travis/GenericMappingTools/website.svg?style=flat)](https://travis-ci.org/GenericMappingTools/website)

This repository contains the sphinx source files for building the GMT website.

## Compiling the site

Run:

    make

Pushing changes to
[GenericMappingTools/website](https://github.com/GenericMappingTools/website)
triggers a build on [TravisCI](https://travis-ci.org/GenericMappingTools/website).
When changes are pushed to the `master` branch (directly or by merging a Pull
Request), Travis will push the compiled site to the
[GenericMappingTools/genericmappingtools.github.io](https://github.com/GenericMappingTools/genericmappingtools.github.io)
repository.
Github serves this repository under
[http://genericmappingtools.github.io](http://genericmappingtools.github.io/).

Pushing the changes from Travis is handled by [doctr](https://github.com/drdoctr/doctr).
See `.travis.yml`.


## License

[![Creative Commons
License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
This work is licensed under a
[Creative Commons Attribution 4.0 International
License](http://creativecommons.org/licenses/by/4.0/).
