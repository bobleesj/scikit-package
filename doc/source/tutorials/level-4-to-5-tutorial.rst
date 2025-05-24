.. _level-4-to-5-tutorial:

Migrate your package from Level 4 to Level 5
============================================

Overview
---------

In this guide, you will learn to migrate your package from Level 4 to Level 5. Once you have your package up to the Level 5 standard, you can share your code with the world. Here are the 3 main steps:

- :ref:`migrate-existing-level-4-code-to-level-5`
- :ref:`set-up-github-repository-for-level-5`
- :ref:`create-pull-request-to-finalize-migration`
- :ref:`other-useful-features-in-level-5`
- :ref:`ready-for-public-release`


What's the difference between Level 4 and Level 5?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Besides the final goal of releasing your package, you will also have the following features:

- Develop documentation with Sphinx with live loading.
- Host documentation on a public URL with GitHub Pages.
- Use GitHub tags to release your package to GitHub and PyPI.
- Maintain changelogs and release notes automatically for each version.

Prerequisites
^^^^^^^^^^^^^

We assume you have already completed and created your scientific code in Level 4, where you have a lightweight Python package that can be installed locally and have your project hosted on GitHub.

.. include:: ../snippets/scikit-installation.rst

.. _migrate-existing-level-4-code-to-level-5:

Step 1. Create a new Level 5 project and migrate files
------------------------------------------------------

The first step is to create a new project with ``scikit-package`` using the Level 5 ``public`` template. Then we will migrate the files and folderes from the existing Level 4 project to the new Level 5 project. Let's begin!

.. _level-5-new-project:

Create a new project with ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Visit your project directory and sync with the latest version of the main branch.

    .. code-block:: bash

        $ cd <project-name>
        $ git checkout main
        $ git pull origin main

#. Create a new branch where you will initiate a new project.

    .. code-block:: bash

        $ git checkout -b skpkg-public

#. Create a new project with ``scikit-package`` using the Level 5 ``public`` template.

    .. code-block:: bash

        $ package create public

#. Answer the following questions:

    .. include:: ../snippets/user-input-level-5.rst

#. Enter into the Level 5 project directory.

    .. code-block:: bash

        $ cd my-package

#. Check that you have the following nested folder structure. Here is the structure. We will go through each file and folder.

    .. code-block:: text

        my-package     # (Level 4)
        └── my-package # (Level 5)
            ├── AUTHORS.rst
            ├── CHANGELOG.rst
            ├── CODE_OF_CONDUCT.rst
            ├── LICENSE.rst
            ├── MANIFEST.in
            ├── README.rst
            ├── doc
            ├── news
            ├── pyproject.toml
            ├── requirements
            ├── src
            └── tests
        ├── LICENSE.rst
        ├── README.md
        ├── pyproject.toml
        ├── requirements
        ├── src
        └── tests

Migration files from Level 4 to Level 5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Enter into the nested Level 5 project directory.

    .. code-block:: bash

        $ cd my-package

#. Move the local ``git`` repository from the Level 4 (``..``) to the Level 5 folder (``.``).

    .. code-block:: bash

        $ mv ../.git .

#. Move the ``src`` and ``tests`` folders from Level 4 to Level 5.

    .. code-block:: bash

        $ cp -n -r ../src .
        $ cp -n -r ../tests .

#. Copy the requirements files from Level 4 to Level 5.

    .. code-block:: bash

        $ cp ../requirements/conda.txt ./requirements/conda.txt
        $ cp ../requirements/pip.txt ./requirements/pip.txt
        $ cp ../requirements/test.txt ./requirements/test.txt

#. At this point, you should be able to install the package locally and test it.

    .. code-block:: bash

        $ conda activate my-package-env
        $ pip install --no-deps -e .
        $ pytest

#. Once the tests pass, let's manually migrate hand-written files like ``README.md`` from Level 4 to Level 5.

    .. note::

        In Level 5, we provide a rich template for ``README.rst`` instead of using ``README.md``. If you already had a rich ``README.md`` in Level 4, you can use a tool to convert ``.md`` to ``.rst``. For example, you may use this free `CloudConvert <https://cloudconvert.com/md-to-rst/>`_ tool.

Build documentation locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^

``/doc`` is the the Sphinx documentation folder. The documentation will be built locally first and then automatically built and hosted on GitHub Pages when a new release is created.

.. include:: ../snippets/doc-local-build.rst

.. _set-up-github-repository-for-level-5:

Step 2. Setup Codecov CI, and GitHub Actions permission in GitHub repository
--------------------------------------------------------------------------

In Level 5, we offer more powerful GitHub Actions CI workflows beyond ``pre-commit CI``. First, we will set up ``Codecov``, which will report the code coverage of incoming code via a PR comment.

Setup Codecov token for GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-codecov-setup.rst

.. _github-news-ci-permission:

Allow GitHub Actions to write comments in PRs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As you will see in the next section, we'd like to have GitHub Actions write comments such as warnings. Let's specify the permissions in the GitHub repository settings by following the steps below.

.. include:: ../snippets/github-ci-permission.rst

.. _create-pull-request-to-finalize-migration:

Step 3. Push your code to GitHub and create a pull request
----------------------------------------------------------

#. In the ``skpkg-public`` branch, since the template is expected to work out of the box from Level 4 to 5, we can simply git add all the files and folders to the GitHub repository.

    .. code-block:: bash

        $ git add .
        $ git commit -m "skpkg: migrate from Level 4 to Level 5"

.. _news-keyboard-shortcut:

Add news items in the GitHub pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/news-item-PR.rst

Push your code to GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that you have added the news items, let's push the code to the GitHub repository

#. Push the code to the GitHub repository.

    .. code-block:: bash

        $ git push origin skpkg-public

#. Create a pull request in the GitHub repository to ``main``.

#. As we have done in Level 4, wait for the CI to pass. You can also check the status of the CI in the pull request.

#. Once the CI passes, you can merge the pull request as you are the owner of the repository.

#. Done!

.. _other-useful-features-in-level-5:

Other useful features available in Level 5
------------------------------------------

.. include:: ../snippets/level-4-5-optional.rst

.. _ready-for-public-release:

Ready for public release?
-------------------------

Congratulations! Your package has been successfully migrated. This has been the most challenging step. Now, let's release your package to PyPI and conda-forge. Please visit the :ref:`Release your package <release-pypi-github>` page to learn how to release your package!
