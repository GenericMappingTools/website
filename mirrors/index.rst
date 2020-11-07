.. title:: Mirrors

Mirrors
=======

FTP Mirrors
-----------

The GMT FTP site hosts tarballs of GMT releases and its support data.
Here is a list of the known active mirrors of the GMT FTP site.
Try the site that is closest to you to minimize transmission times.

.. cssclass:: table-bordered

=============================================================== =============================================================
Site                                                            Address
=============================================================== =============================================================
SOEST, U. of Hawaii, US                                         ftp://ftp.soest.hawaii.edu/gmt
Lab for Satellite Altimetry, NOAA, US                           ftp://ftp.star.nesdis.noaa.gov/pub/sod/lsa/gmt
IRIS, Washington, US                                            ftp://ftp.iris.washington.edu/pub/gmt
IAG-USP, U. of Sao Paulo, BRAZIL                                ftp://ftp.iag.usp.br/pub/gmt
TENET, Tertiary Education & Research Networks, SOUTH AFRICA     ftp://gmt.mirror.ac.za/gmt
Univ. of Sci. & Tech. of China, Hefei, CHINA                    http://mirrors.ustc.edu.cn/gmt
Tokai U, Shizuoka, JAPAN                                        http://www.scc.u-tokai.ac.jp/gmt
=============================================================== =============================================================

Many thanks to these institutions for serving as GMT FTP mirrors for such a long time!

Data Server Mirrors
-------------------

The GMT data server stores frequently used data sets (e.g., Earth Relief Data).
Here is a list of the known active mirrors of the GMT remote data server.
Change the GMT setting `GMT_DATA_SERVER <https://docs.generic-mapping-tools.org/latest/gmt.conf.html#term-GMT_DATA_SERVER>`_
to the mirror that is closest to you to minimize transmission times.
We thank the hosting institutions for mirroring the GMT data distribution so that users can have a faster download wherever they are located.

.. cssclass:: table-bordered

================= ============================================================= ========================
Name              Address                                                       Mirror Status
================= ============================================================= ========================
**Oceania**       https://oceania.generic-mapping-tools.org                     |Oceania_mirror_status|
**Europe**        http://europe.generic-mapping-tools.org                       |Europe_mirror_status|
**China**         http://china.generic-mapping-tools.org                        |China_mirror_status|
================= ============================================================= ========================

.. |Oceania_mirror_status| image:: https://img.shields.io/website?down_message=offline&label=%20&style=plastic&up_message=OK&url=https%3A%2F%2Foceania.generic-mapping-tools.org
                           :alt: Oceania Mirror Status

.. |Europe_mirror_status| image:: https://img.shields.io/website?down_message=offline&label=%20&style=plastic&up_message=OK&url=http%3A%2F%2Feurope.generic-mapping-tools.org
                          :alt: Europe Mirror Status

.. |China_mirror_status| image:: https://img.shields.io/website?down_message=offline&label=%20&style=plastic&up_message=OK&url=http%3A%2F%2Fchina.generic-mapping-tools.org
                          :alt: China Mirror Status

Becoming a GMT mirror
---------------------

You can help out the GMT community by running a mirror of
the GMT FTP site (~20 GB) and/or the GMT data server (~60 GB).

To mirror the GMT FTP site, you can use `lftp <https://lftp.yar.ru/>`_::

    lftp -e "mirror --delete --parallel=8 gmt gmt; bye" ftp.soest.hawaii.edu

To mirror the GMT data server, you can use the **rsync** command::

    rsync -av --delete rsync://oceania.generic-mapping-tools.org/gmtdata /your/local/gmtdata

You must run the above command periodically (e.g., daily) to keep files in the
mirror up to date. This can be done via `cron jobs <https://en.wikipedia.org/wiki/Cron>`_.

We're glad to offer help if you enconter problems when setting up the mirror.
Once you have gotten the mirror running, please `let us know <https://forum.generic-mapping-tools.org/>`_
so that we can add your mirror to the list.
