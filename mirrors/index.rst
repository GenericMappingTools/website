.. title:: Mirrors

Mirrors
=======

**We thank the hosting institutions for mirroring the GMT FTP and data server
so that users can have a faster download wherever they are located.**

FTP Mirrors
-----------

The GMT FTP site hosts tarballs of GMT releases and its support data.
Here is a list of the known active mirrors of the GMT FTP site.
Try the site that is closest to you to minimize transmission times.

.. cssclass:: table-bordered table-mirrors

=============================================================== =============================================================
Site                                                            Address
=============================================================== =============================================================
SOEST, U. of Hawaii, USA                                        ftp://ftp.soest.hawaii.edu/gmt
EarthByte Group, Sydney U, Australia                            https://www.earthbyte.org/webdav/gmt_mirror/gmt
Lab for Satellite Altimetry, NOAA, USA                          ftp://ftp.star.nesdis.noaa.gov/pub/sod/lsa/gmt
IRIS, Washington, USA                                           ftp://ftp.iris.washington.edu/pub/gmt
IAG-USP, U. of Sao Paulo, Brazil                                https://generic-mapping-tools.iag.usp.br/gmt
TENET, Tertiary Education & Research Networks, South Africa     ftp://gmt.mirror.ac.za
Univ. of Sci. & Tech. of China, Hefei, China                    http://mirrors.ustc.edu.cn/gmt
Tokai U, Shizuoka, Japan                                        http://www.scc.u-tokai.ac.jp/gmt
=============================================================== =============================================================


Data Server Mirrors
-------------------

The GMT data server stores frequently used data sets (e.g., Earth Relief Data).
Here is a list of the known active mirrors of the GMT remote data server.
Change the GMT setting `GMT_DATA_SERVER <https://docs.generic-mapping-tools.org/latest/gmt.conf.html#term-GMT_DATA_SERVER>`_
to the mirror that is closest to you to minimize transmission times.
(Please `report to us <https://github.com/GenericMappingTools/gmtserver-admin/issues>`_ if any mirrors are offline.)

.. cssclass:: table-bordered table-mirrors

.. list-table::
   :widths: 20 50 25 5
   :header-rows: 1

   * - Name
     - Address
     - Host
     - Status
   * - **Oceania** [Master]
     - https://oceania.generic-mapping-tools.org
     - SOEST, U of Hawaii, USA
     - .. image:: https://img.shields.io/website?down_message=offline&label=%20&style=plastic&up_message=OK&url=https%3A%2F%2Foceania.generic-mapping-tools.org/gmt_data_server.txt
   * - **Brasil**
     - http://brasil.generic-mapping-tools.org
     - IAG-USP, U of Sao Paulo, Brazil
     - .. image:: https://img.shields.io/website?down_message=offline&label=%20&style=plastic&up_message=OK&url=http%3A%2F%2Fbrasil.generic-mapping-tools.org/gmt_data_server.txt
   * - **Australia**
     - http://australia.generic-mapping-tools.org
     - EarthByte Group, Sydney U, Australia
     - .. image:: https://img.shields.io/website?down_message=offline&label=%20&style=plastic&up_message=OK&url=http%3A%2F%2Faustralia.generic-mapping-tools.org/gmt_data_server.txt
   * - **China**
     - http://china.generic-mapping-tools.org
     - U of Sci. & Tech. of China, China
     - .. image:: https://img.shields.io/website?down_message=offline&label=%20&style=plastic&up_message=OK&url=http%3A%2F%2Fchina.generic-mapping-tools.org/gmt_data_server.txt
   * - **sdsc-opentopography** [US West Coast]
     - http://sdsc-opentopography.generic-mapping-tools.org
     - OpenTopography at San Diego Supercomputing Center
     - .. image:: https://img.shields.io/website?down_message=offline&label=%20&style=plastic&up_message=OK&url=http%3A%2F%2Fsdsc-opentopography.generic-mapping-tools.org/gmt_data_server.txt
   * - **NOAA** [US East Coast]
     - http://noaa.generic-mapping-tools.org
     - Lab for Satellite Altimetry, NOAA, USA
     - .. image:: https://img.shields.io/website?down_message=offline&label=%20&style=plastic&up_message=OK&url=https%3A%2F%2Fwww.star.nesdis.noaa.gov/data/socd3/lsa/gmtdata/gmt_data_server.txt
   * - **Portugal**
     - http://portugal.generic-mapping-tools.org
     - U of Algarve, Portugal
     - .. image:: https://img.shields.io/website?down_message=offline&label=%20&style=plastic&up_message=OK&url=http%3A%2F%2Fportugal.generic-mapping-tools.org/gmt_data_server.txt
   * - **Singapore**
     - http://singapore.generic-mapping-tools.org
     - National U of Singapore, Singapore
     - .. image:: https://img.shields.io/website?down_message=offline&label=%20&style=plastic&up_message=OK&url=http%3A%2F%2Fsingapore.generic-mapping-tools.org/gmt_data_server.txt
   * - **South Africa**
     - http://south-africa.generic-mapping-tools.org
     - TENET, Tertiary Education & Research Networks, South Africa
     - .. image:: https://img.shields.io/website?down_message=offline&label=%20&style=plastic&up_message=OK&url=http%3A%2F%2Fsouth-africa.generic-mapping-tools.org/gmt_data_server.txt

Becoming a GMT mirror
---------------------

You can help out the GMT community by running a mirror of
the GMT FTP site (~25 GB) and/or the GMT data server (~120 GB).

To mirror the GMT FTP site, you can use `lftp <https://lftp.yar.ru/>`_::

    lftp -e "mirror --delete --parallel=8 gmt gmt; bye" ftp.soest.hawaii.edu

To mirror the GMT data server, you can use the **rsync** command::

    rsync -av --delete rsync://oceania.generic-mapping-tools.org/gmtdata /your/local/gmtdata

You must run the above commands periodically (e.g., daily) to keep files in the
mirrors up to date. This can be done via `cron jobs <https://en.wikipedia.org/wiki/Cron>`_.

We are glad to offer help if you encounter problems when setting up the mirror.
Once you have gotten the mirror running, please `let us know <https://forum.generic-mapping-tools.org/>`_
so that we can add your mirror to the list. **Note**: We reserve the right to decide which mirrors
will receive a forward from the generic-mapping-tools domain.
