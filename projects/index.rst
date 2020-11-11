.. title:: Projects

The GMT ecosystem
=================

A bit about main GMT, the external interfaces, and derived projects (GMTSAR, MB-System).


Core GMT
--------

The core GMT API library lies at the center of GMT. It powers the command-line modules
typically scripted in shell languages (bash, csh, etc).  It can also be linked with
a user's custom C or C++ program to extend GMT into discipline-specific processing or
plotting for applications not currently supported by the core GMT package.

.. raw:: html

   <ul class="fa-ul">
      <li><i class="fa-li fa fa-book fa-fw"></i>
         <a href="https://docs.generic-mapping-tools.org">Documentation</a>
      </li>
      <li><i class="fa-li fab fa-github fa-fw"></i>
         <a href="https://github.com/GenericMappingTools/gmt">GenericMappingTools/gmt</a>
      </li>
   </ul>

GMT interfaces
--------------

GMTMex
++++++

The GMT/MATLAB toolbox allows users of MATLAB and Octave to write scripts in those
environments that calls the GMT modules directly.  Users can pass and retrieve data
from and to their environment and benefit from the best of both worlds.

.. raw:: html

   <ul class="fa-ul">
      <li><i class="fa-li fa fa-book fa-fw"></i>
         <a href="https://github.com/GenericMappingTools/gmtmex/wiki">Documentation</a>
      </li>
      <li><i class="fa-li fab fa-github fa-fw"></i>
         <a href="https://github.com/GenericMappingTools/gmtmex">GenericMappingTools/gmtmex</a>
      </li>
   </ul>


GMT.jl
++++++

The GMT.jl wrapper is intended not only to access GMT from within the Julia language
but also to provide a more modern interface to the GMT modules by fully expanding the compact
syntax into long options names.

.. raw:: html

   <ul class="fa-ul">
      <li><i class="fa-li fa fa-book fa-fw"></i>
         <a href="https://www.generic-mapping-tools.org/GMT.jl/">Documentation</a>
      </li>
      <li><i class="fa-li fab fa-github fa-fw"></i>
         <a href="https://github.com/GenericMappingTools/GMT.jl">GenericMappingTools/GMT.jl</a>
      </li>
   </ul>

PyGMT
+++++

A Python library for accessing GMT's plotting and data processing capabilities from a
simplified, object-oriented interface that is compatible with the
`Jupyter notebook <https://jupyter.org/>`__.

.. raw:: html

   <ul class="fa-ul">
      <li><i class="fa-li fa fa-book fa-fw"></i>
         <a href="https://www.pygmt.org">Documentation</a>
      </li>
      <li><i class="fa-li fab fa-github fa-fw"></i>
         <a href="https://github.com/GenericMappingTools/pygmt">GenericMappingTools/pygmt</a>
      </li>
   </ul>


Software relying on GMT
-----------------------

GMTSAR
++++++

An open source (GNU General Public License) InSAR processing system based on GMT and
designed for users familiar with Generic Mapping Tools (GMT). The code is written in C
and will compile on any computer where GMT and NetCDF are installed.

.. raw:: html

   <ul class="fa-ul">
      <li><i class="fa-li fa fa-book fa-fw"></i>
         <a href="https://topex.ucsd.edu/gmtsar/">Documentation</a>
      </li>
      <li><i class="fa-li fab fa-github fa-fw"></i>
         <a href="https://github.com/gmtsar/gmtsar">gmtsar/gmtsar</a>
      </li>
   </ul>

MB-System
+++++++++

An open source software package for the processing and display of bathymetry and
backscatter imagery data derived from multibeam, interferometry, and sidescan sonars.

.. raw:: html

   <ul class="fa-ul">
      <li><i class="fa-li fa fa-book fa-fw"></i>
         <a href="https://www.mbari.org/products/research-software/mb-system/">Documentation</a>
      </li>
      <li><i class="fa-li fab fa-github fa-fw"></i>
         <a href="https://github.com/dwcaress/MB-System">dwcaress/MB-System</a>
      </li>
   </ul>
