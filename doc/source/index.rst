
#######

.. |title| replace:: scikit-package documentation

| Software version |release|.
| Last updated |today|.

Welcome to Billinge Group's Python scikit-package documentation!

How `scikit-package` benefits scientists
----------------------------------------

A challenge for scientists is to share software with the community. As a scientist, if you **have useful code you want to share and further develop**, how do you go about doing that? Sharing code can be challenging due to complications inherent in the process. Here we provide a roadmap and helpful templates for scientists who wish to share their code with others.

The goal of ``scikit-package`` is to offer students and scientists an easy path to share code at various levels of complexity. At the lowest level it has pedagogical examples for simple sharing such as reusing functions across files, building up in complexity all the way to sharing with the wider scientific community as a fully open-source, maintained and tested package.

When your software is ready for public distribution, ``scikit-package`` provides pre-configured documents and a straightforward release process that, once it is set up, significantly reduces the time required to release and share code. It also standardizes procedures across projects.

Getting started
---------------

To get started, please visit the :ref:`Getting started <getting-started>` page to learn how to navigate the documentation!


Who are using ``scikit-package``?
----------------------------------

The full list of packages is as follows:

- `diffpy.pdffit2 <https://github.com/diffpy/diffpy.pdffit2>`_
- `diffpy.fourigui <https://github.com/diffpy/diffpy.fourigui>`_
- `diffpy.pdfgui <https://github.com/diffpy/diffpy.pdfgui>`_
- `diffpy.utils <https://github.com/diffpy/diffpy.utils>`_
- `diffpy.structure <https://github.com/diffpy/diffpy.structure>`_
- `diffpy.labpdfproc <https://github.com/diffpy/diffpy.labpdfproc>`_
- `diffpy.pdfmorph <https://github.com/diffpy/diffpy.pdfmorph>`_
- `diffpy.snmf <https://github.com/diffpy/diffpy.snmf>`_
- `diffpy.srmise <https://github.com/diffpy/diffpy.srmise>`_
- `regolith <https://github.com/regro/regolith>`_
- `bg-mpl-stylesheets <https://github.com/Billingegroup/bg-mpl-stylesheets>`_

What are the useful features?
-----------------------------

To help increase your research impact, ``scikit-package`` offers the following features:

- Automated `PEP8 <https://peps.python.org/pep-0008/>`_ and `PEP256 <https://peps.python.org/pep-0256/>`_ standard checks.
- Automated PyPI/GitHub release, testing, documentation, and CHANGELOG updates.
- Streamlined package release workflow with a checklist.
- Latest Python version support compatible with `SPEC0 <https://scientific-python.org/specs/spec-0000/>`_.
- Rich README template containing badges, installation, support, and contribution guide.
- Automatic spelling check, linting for .json, .yml, and .md files.

For more technical details, it includes:

- Pull requests with coverage reports using ``Codecov`` and checks with ``pre-commit CI``.
- Namespace package support, e.g., ``import diffpy.utils``.
- conda-package ``meta.yaml`` generation with a template.
- Support for non-pure Python package releases with ``cibuildwheel``.
- Support for headless GitHub CI testing for GUI applications.
- Reusable GitHub Actions workflows located in `Billingegroup/release-scripts <https://github.com/Billingegroup/release-scripts/tree/main/.github/workflows>`_.

How do I get started?
---------------------

Please visit the :ref:`Getting started <getting-started>` page to learn how to navigate the documentation!

How do I receive support?
-------------------------

If you have any questions or have trouble, please read the :ref:`Frequently asked questions (FAQ) <frequently-asked-questions>` section to see if your questions have already been answered. If there aren't answers available, please create an issue. The team will reach out.

How can I contribute?
---------------------

Do you have any new features? Please make an issue via the GitHub issue tracker for further discussions. For a minor typo or grammatically incorrect sentence, please make a pull request. Before making a PR, please run ``pre-commit run --all-files`` to ensure the code is formatted.

=======
Authors
=======

- Sangjoon Lee (sl5400@columbia.edu)
- Andrew Yang (ay2546@columbia.edu)
- Simon Billinge (sb2896@columbia.edu)

scikit-package is developed by Billinge Group and its community contributors.

For a detailed list of contributors, see
https://github.com/Billingegroup/scikit-package/graphs/contributors.

================
Acknowledgements
================

The Billinge Group's scikit-package has been modified from the NSLS-II scientific cookiecutter: https://github.com/nsls-ii/scientific-python-cookiecutter

=================
Table of contents
=================
.. toctree::
   :maxdepth: 2

   getting-started
   start-new-project-no-package
   start-new-project-package-lightweight
   start-new-project-package-full
   pypi-release-guide
   conda-forge-release-guide
   migration-guide
   frequently-asked-questions
   license
   release

=======
Indices
=======

* :ref:`genindex`
* :ref:`search`
