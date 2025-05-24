.. _level-5-tutorial:

(Level 5) Share your code as a publicly installable package
===========================================================

Overview
--------

Welcome! By the end of the tutorial, you will be able to share your code as a publicly installable package that can be installed using ``pip install <package-name>`` and ``conda install <package-name>``.

Prerequisites
^^^^^^^^^^^^^

We assume that you have a basic understanding of starting a new project and have hosted at least one project on GitHub. If you are new to GitHub, we recommend you start from :ref:`level-4-tutorial` where you will learn how to create a new project and host it on GitHub while using GitHub Actions to automatically format your code and run unit tests.

Make sure you have the latest version of ``scikit-package`` installed:

.. include:: ../snippets/scikit-installation.rst

Step 1. Create a new project with ``scikit-package``
----------------------------------------------------

Create a new GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-create-new-repo.rst


Create a new project with ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Run the following command to create a new project folder with ``scikit-package`` using the Level 5 ``public`` template:

    .. code-block:: bash

        $ package create public

#. Answer the following questions:

    .. include:: ../snippets/user-input-level-5.rst

    .. note::

        You may press the "Enter" key to accept the default values for the questions.

#. Now type ``ls`` to check a new folder has been created.

Install your package locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/package-install-test-local.rst

Build documentation locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^

``/doc`` is the the Sphinx documentation folder. The documentation will be built locally first and then automatically built and hosted on GitHub Pages when a new release is created.

.. include:: ../snippets/doc-local-build.rst

Upload ``README.md`` to your GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-upload-readme-pre-commit.rst

Step 2. Automate code linting and testing with GitHub Actions
-------------------------------------------------------------

We will do 3 things in order to automate testing, linting, infrastructure in your GitHub repository.

- :ref:`pre-commit-ci`
- :ref:`github-codecov-setup`
- :ref:`github-ci-permission`

The above steps will take 5 to 10 minutes in total but save hours and days of time in the long run.

.. _pre-commit-ci:

1. Setup ``pre-commit CI`` in the remote repository in each pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-pre-commit-setup.rst

.. _github-codecov-setup:

2. Setup Codecov token for GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-codecov-setup.rst

.. _github-ci-permission:

3. Allow GitHub Actions to write comments in PRs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-ci-permission.rst

.. _github-news-item-PR:

Step 3. Upload rest of files to GitHub repository with pull request
-------------------------------------------------------------------

While we previously uploaded the ``README`` file to the remote GitHub ``main`` repository, this is not a recommended workflow. We want to ensure that before any code is pushed to the ``main`` branch, the incoming code **formatted**, **tested**, and **reviewed**. We will try to automate these tasks as much as we can while creating a pull request (PR) to the ``main`` branch.

#. Just in case, pull the latest code from the remote ``main`` branch to your local ``main`` branch:

    .. code-block:: bash

        $ git checkout main
        $ git pull origin main

#. Setup pre-commit locally so that code is linted before a commit is made:

    .. code-block:: bash

        $ pre-commit install

#. Checkout a new branch called ``skpkg-public`` from the ``main`` branch:

    .. code-block:: bash

        $ git checkout -b skpkg-public
        $ git add .
        $ git commit -m "skpkg: start a new level 5 project with skpkg"
        $ git push -u origin skpkg-public

    .. note::

        Did you see any failed ``pre-commit`` hooks? If so, no commit will be made. Simply re-run ``git add <file>`` on the files that have been modified by ``pre-commit`` and re-enter the same commit message again, such as ``git commit -m "skpkg: start a new project with skpkg template"``. If you are having trouble getting a commit to be accepted, please refer to the FAQ section :ref:`here<faq-pre-commit-error>`.

Add news items in the GitHub pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is just one more thing to do.

.. include:: ../snippets/news-item-PR.rst


#. In your GitHub repository, click :guilabel:`Compare & pull request`.

#. Set the PR title as ``skpkg: start a new project with Level 5 tutorial``.

#. The ``base`` branch should be ``main`` and the ``compare`` branch should be ``skpkg-public``.

#. Click :guilabel:`Create pull request`.

#. Wait all GitHub Action workflows to run including ``Test on PR``.

#. Also wait for ``pre-commit`` CI to run and pass.

    .. note:: Did ``pre-commit CI`` fail?

        If the pre-commit failed, you will need to first pull the new commit created by ``pre-commit CI`` before making any new edits locally. You can do this by running the following command:

        .. code-block:: bash

         $ git pull origin skpkg-public

        If you have more problems, please read the FAQ section on :ref:`faq-pre-commit-error`.

#. Click :guilabel:`Files changed` in the PR to to review the new files added to the repository.

#. Once reviewed, click :guilabel:`Merge pull request`.

#. Delete the remote branch after merging.

#. Visit your GitHub repository and confirm that the ``main`` branch is updated.

#. Congratulations! You are done with uploading your new package!

Ready for public release?
-------------------------

Congratulations! Let's release your package to PyPI and conda-forge. Visit :ref:`release-pypi-github` to have your package avaialble via ``conda install`` and ``pip isntall``!

Useful features available in Level 5
------------------------------------

.. include:: ../snippets/level-5-optional-sections.rst
