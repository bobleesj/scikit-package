.. _level-4-tutorial:

(Level 4) Share your code as a locally installable Python package
=================================================================

Overview
--------

You will learn to share code across any files in your computer. By the end of this tutorial, you will also have your package hosted on GitHub, where you will utilize GitHub Actions to run automatic linting and testing for the incoming code in your GitHub repository.

This tutorial should take about 10 to 15 minutes.

Table of contents
^^^^^^^^^^^^^^^^^

1. :ref:`create-new-project-with-scikit-package`

2. :ref:`automate-code-linting-and-testing`

3. :ref:`use-pull-request-to-upload-code-to-github`

Prerequisites
^^^^^^^^^^^^^

For Level 4, we assume you have prior experience in developing scientific code in Python.

.. seealso:: Are you new to Git and GitHub?

    Please read the GitHub workflow section in :ref:`faq-github-workflow` to familiarize yourself with the common jargon and terms used.

.. include:: ../snippets/scikit-installation.rst

.. _create-new-project-with-scikit-package:

Step 1. Create a new package with ``scikit-package``
----------------------------------------------------

Create a new GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this tutorial, we will start by creating a new GitHub repository. The GitHub repository is where we will host our code online (remote).

.. include:: ../snippets/github-create-new-repo.rst

Let's now create a new package in your computer (local) next using ``scikit-package``.

Create a new project with ``scikit-package``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Run the following command to create a new project with ``scikit-package``:

    .. code-block:: bash

        $ package create system

#. Answer the following questions:

    .. list-table::
       :header-rows: 1
       :widths: 25 75

       * - Field
         - Description and example
       * - project_name
         - The project name displayed on README. e.g., my-package
       * - github_username_or_orgname
         - The GitHub username or organization name, e.g., sbillinge or billingegroup
       * - github_repo_name
         - The GitHub repository name. Use ``name-with-hypens``. e.g., my-package
       * - conda_pypi_package_dist_name
         - The name displayed on PyPI and conda-forge. Use ``name-with-hypens``. e.g., my-package
       * - package_dir_name
         - The name of the package directory under ``src``. Use ``name_with_underscores``. e.g., my_package
       * - contributors
         - The contributors involved in the project. e.g., Sangjoon Lee, Simon Billinge

    .. note::

        You may press the "Enter" key on your keyboard to accept the default value for the field provided in parentheses.

#. ``cd`` into the project directory created by the ``package create system`` command above. We will assume that the user has entered the project name as ``my-package``.

    .. code-block:: bash

        $ cd my-package

#. Confirm that you have the following folder structure shown below:

    .. code-block:: text

        my-package/
        ├── LICENSE.rst
        ├── README.md
        ├── pyproject.toml
        ├── requirements
        │   ├── conda.txt
        │   ├── pip.txt
        │   └── test.txt
        ├── src
        │   └── my_package
        │       ├── __init__.py
        │       └── functions.py
        └── tests
            └── test_functions.py

#. Done! Let's now install your package in your local computer where the code can be used in any Python script or Jupyter notebook.

Install your package locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/package-install-test-local.rst

Upload ``README.md`` to your GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-upload-readme-pre-commit.rst

.. _automate-code-linting-and-testing:

Step 2. Automate code linting and testing with GitHub Actions
-------------------------------------------------------------

Setup pre-commit to lint code before making a commit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/pre-commit-local-setup.rst

Setup ``pre-commit CI`` in the remote repository in each pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-pre-commit-setup.rst


Step 3. Upload rest of files to GitHub repository with pull request
-------------------------------------------------------------------

While we previously uploaded the ``README`` file to the remote GitHub ``main`` repository, this is not a recommended workflow. We want to ensure that before any code is pushed to the ``main`` branch, the incoming code **formatted**, **tested**, and **reviewed**. We will try to automate these tasks as much as we can while creating a pull request (PR) to the ``main`` branch.

#. Just in case, pull the latest code from the remote ``main`` branch to your local ``main`` branch:

    .. code-block:: bash

        $ git checkout main
        $ git pull origin main

#. Checkout a new branch called ``skpkg-system`` from the ``main`` branch:

    .. code-block:: bash

        $ git checkout -b skpkg-system
        $ git add .
        $ git commit -m "skpkg: start a new project with skpkg"
        $ git push -u origin skpkg-system

#. Visit your GitHub repository online.

#. Click on the new green button that says ``Compare & pull request``.

#. The PR title can be ``skpkg: start a new project with skpkg template``.

#. The ``base`` branch should be ``main`` and the ``compare`` branch should be ``skpkg-system``.

#. Click on the ``Create pull request`` button.

#. Wait for ``Tests on PR`` to run and pass. It runs ``pytest`` on the incoming code in each pull request.

#. Also wait for ``pre-commit`` CI to run and pass.

    .. note:: Did ``pre-commit CI`` fail?

        If the pre-commit failed, you will need to first pull the new commit created by ``pre-commit CI`` before making any new edits locally. You can do this by running the following command:

        .. code-block:: bash

         $ git pull origin skpkg-system
         $ git add <file-modified-that-fixes-pre-commit-error>
         $ git commit -m "chore: <your commit message>"
         $ git push

#. Click :guilabel:`Files changed` in the PR to to review the new files added to the repository.

#. Once reviewed, click :guilabel:`Merge pull request`.

#. Delete the ``skpkg-system`` remote branch after merging.

#. Visit your GitHub repository and confirm that the ``main`` branch is updated.

#. Congratulations! You are done!


(Recommended) How to develop your code moving forward using pull requests
-------------------------------------------------------------------------

Assume that you have successfully followed the previous steps. Now, you want to add new code to your GitHub repository. Perhaps you are working with a group of people. Here is a high-level overview with step-by-step instructions on how to do that:

#. Pull the latest code from the remote ``main`` branch:

    .. code-block:: bash

        $ git checkout main
        $ git pull origin main

    .. note::

        Recall that we used the name ``origin`` as the nickname for the remote GitHub repository.

#. Ensure that your local ``main`` branch is synced with the remote ``main`` branch by running:

    .. code-block:: bash

        $ git log

#. Create a new local branch from the ``main`` branch. Let's call this branch ``skpkg``:

    .. code-block:: bash

        $ git checkout -b <branch-name>

#. Modify any file that you want. Then, stage and commit the changes:

    .. code-block:: bash

        $ git add <file-modified-added-deleted>
        $ git commit -m "feat: <your commit message>"

#. Push your code from ``<branch-name>`` to the remote ``<branch-name>`` branch:

    .. code-block:: bash

        $ git push --set-upstream origin <branch-name>

#. Visit your GitHub repository.

#. Create a PR from ``origin/<branch-name>`` to ``origin/main``.

#. Wait for the ``Tests on PR`` and ``pre-commit`` checks to pass.

#. Merge the PR, delete the branch.

#. Repeat the steps in this section.

#. Done!

What's next?
------------

Once you are ready to release your package to the wider world, let's proceed to :ref:`level-5-tutorial` where you will learn to release your package to PyPI and conda-forge so that your package can be installed by anyone in the world.
