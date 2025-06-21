Quantum 1-Shot Signatures
=========================

|Python version| |PyPI version| |PyPI status| |Mypy checked| |Documentation status|

.. |Python version| image:: https://img.shields.io/badge/python-3.10+-green.svg
    :target: https://docs.python.org/3.10/
    :alt: Python versions

.. |PyPI version| image:: https://img.shields.io/pypi/v/q1ss.svg
    :target: https://pypi.python.org/pypi/q1ss/
    :alt: PyPI version

.. |PyPI status| image:: https://img.shields.io/pypi/status/q1ss.svg
    :target: https://pypi.python.org/pypi/q1ss/
    :alt: PyPI status

.. |Mypy checked| image:: http://www.mypy-lang.org/static/mypy_badge.svg
    :target: https://github.com/python/mypy
    :alt: Checked with Mypy

.. |Documentation status| image:: https://readthedocs.org/projects/q1ss/badge/?version=latest
    :target: https://q1ss.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


This library contains experimental implementations of quantum one-shot, with special focus on blockchain technology.
Currently, the main focus is on implementation, compilation and obfuscation of affine partition functions, originally introduced by `"One-shot Signatures and Applications to Hybrid Quantum/Classical Authentication" <https://eprint.iacr.org/2020/107>`_.



.. contents::

Install
-------

The library is currently in pre-alpha development, but you can install the latest release from `PyPI <https://pypi.org/project/q1ss/>`_ as follows:

.. code-block:: console

    $ pip install -U q1ss

Low-level operations are vectorised using `numpy <https://numpy.org/doc/stable/>`_, which is a required dependency of this library.

If `numba <https://numba.readthedocs.io/en/stable/>`_ is installed, it is automatically used to JIT-compile certain low-level operations for additional performance:

.. code-block:: console

    $ pip install -U numba

If `cupy <https://docs.cupy.dev/en/stable/>`_ is installed additionally to `numba <https://numba.readthedocs.io/en/stable/>`_, GPU acceleration can be used for certain operations:

.. code-block:: console

    $ pip install -U cupy

If `networkx <https://networkx.org/documentation/stable/>`_ and `matplotlib <https://matplotlib.org/>`_ are installed, affine subspaces and affine partition functions can be drawn for easier visualisation:

.. code-block:: console

    $ pip install -U networkx matplotlib


Usage
-----

Short usage examples for the README are coming soon.

The `notebooks <./notebooks>`_ folder contains the following Jupyter notebooks, exemplifying various features of the library:

1. The `AffinePartitions <./notebooks/AffinePartitions.ipynb>`_ notebook contains examples related to the construction of affine partition functions.

API
---

For the full API documentation, see https://q1ss.readthedocs.io/


License
-------

`LGPL © NeverLocal Ltd. <LICENSE>`_
