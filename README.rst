========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/nfselib.barueri/badge/?style=flat
    :target: https://nfselibbarueri.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/erpbrasil/nfselib.barueri/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/erpbrasil/nfselib.barueri/actions

.. |version| image:: https://img.shields.io/pypi/v/nfselib.barueri.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/nfselib.barueri

.. |wheel| image:: https://img.shields.io/pypi/wheel/nfselib.barueri.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/nfselib.barueri

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/nfselib.barueri.svg
    :alt: Supported versions
    :target: https://pypi.org/project/nfselib.barueri

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/nfselib.barueri.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/nfselib.barueri

.. |commits-since| image:: https://img.shields.io/github/commits-since/erpbrasil/nfselib.barueri/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/erpbrasil/nfselib.barueri/compare/v0.0.1...main



.. end-badges

Python Library to genereate Barueri NFS-e

* Free software: MIT license

Installation
============

::

    pip install nfselib.barueri

You can also install the in-development version with::

    pip install https://github.com/erpbrasil/nfselib.barueri/archive/main.zip


Documentation
=============


https://nfselibbarueri.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
