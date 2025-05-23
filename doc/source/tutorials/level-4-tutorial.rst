.. _level-4-tutorial:

(Level 4) Share code as a locally installable Python package
============================================================

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

For Level 4, we assume you have prior experience in developing scientific code in Python. Additionally, we assume you have hosted at least one project on GitHub. If you are new to GitHub, please refer to the FAQ guide on the GitHub workflow :ref:`here <faq-github-workflow>`.

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

#. Create a new conda environment. Let's call this environment ``my-package-env``:

    .. code-block:: bash

        $ conda create -n my-package-env python=3.13 \
            --file requirements/conda.txt \
            --file requirements/test.txt

#. Activate the conda environment:

    .. code-block:: bash

        $ conda activate my-package-env

#. Build and install the package locally:

    .. code-block:: bash

        $ pip install -e . --no-deps

    .. note:: What is the ``-e`` flag?

        ``pip install`` will also install the dependencies listed in ``requirements/pip.txt``. The ``-e`` flag indicates that you want to install the package in "editable" mode, which means that any changes you make to the source code will be reflected immediately without needing to reinstall the package. This is useful for development purposes.

    .. note:: What is the ``--no-deps`` flag?

        The ``--no-deps`` flag tells pip not to install any dependencies listed in ``requirements/pip.txt``. This is because we have already installed the dependencies in the conda environment using the command above.

    .. seealso::

        Why is it required to list dependencies both under ``pip.txt`` and ``conda.txt``? Please refer to the FAQ section :ref:`faq-dependency-management`.

#. Then, run the tests using the following command:

    .. code-block:: bash

        $ pytest

#. Ensure tests all pass with green checkmarks. Notice that in ``tests/test_functions.py``, we are importing the locally installed package.

#. Congratulations! Your package is now available for use in any Python script or Jupyter notebook on your local computer.

Upload ``README.md`` to your GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At the moment, the GitHub repository is empty. Let's create a local branch called ``main`` and upload this local branch to the remote GitHub repository.

#. Follow the series of steps to initialite ``Git``, create a new branch called ``main`` in the local repository and push the branch to the remote GitHub repository:

    .. code-block:: bash

        $ git init
        $ git add README.md
        $ git commit -m "docs: add README.md"
        $ git branch -M main
        $ git remote add origin <your-github-repo-url>
        $ git push -u origin main

    .. note:: What's ``origin``?

        ``origin`` is the default name for the remote repository under your GitHub account. You can think of it as a nickname for the remote repository. You can also use any other name you like, but ``origin`` is the most common convention. For more, please read :ref:`faq-github-terminology`.

    .. note:: What is ``-u`` next to ``git push``?

        The ``-u`` flag tells Git to set the upstream (remote) branch for the local branch. This means that in the future, you can simply use ``git push`` without specifying the remote and branch name, and Git will know where to push your changes.

#. Done! Ensure that your GitHub repository displays the content of ``README.md``. However, we still haven't upload other files like under ``src`` and ``tests`` files; we will do so to the ``main`` branch of the remote repository through a pull request in the following section. We will also configure some automated testing and linting for incoming code.

.. _automate-code-linting-and-testing:

Step 2. Automate code linting and testing with GitHub Actions
-------------------------------------------------------------

Setup pre-commit to lint code before making a commit in the local repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/pre-commit-local-setup.rst

Setup ``pre-commit CI`` in the remote repository in each pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-pre-commit-setup.rst

.. _use-pull-request-to-upload-code-to-github:

Step 3. Upload rest of files to GitHub repository with pull request
-------------------------------------------------------------------

While we previously uploaded the ``README.md`` file to the remote GitHub ``main`` repository, this is not a recommended workflow. We want to ensure that before any code is pushed to the ``main`` branch, the incoming code **formatted**, **tested**, and **reviewed**. We will try to automate these tasks as much as we can while creating a pull request (PR) to the ``main`` branch.

Create a pull request from ``skpkg`` to ``main``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Just in case, pull the latest code from the remote ``main`` branch:

    .. code-block:: bash

        $ git checkout main
        $ git pull origin main

#. Checkout a new branch called ``skpkg-system`` from the ``main`` branch:

    .. code-block:: bash

        $ git checkout -b skpkg-system
        $ git add .
        $ git commit -m "skpkg: start a new project with skpkg Level 4 template"
        $ git push -u origin skpkg-system

#. Visit your GitHub repository online.

#. Click on the new green button that says ``Compare & pull request``.

#. The PR title can be ``skpkg: start a new project with skpkg system template``.

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

#. Click the :guilabel:`Files changed` in the PR to to review the new files added to the repository.

#. Once reviewed, click on the ``Merge pull request`` button.

#. Delete the ``skpkg-system`` remote branch after merging.

#. Visit your GitHub repository and confirm that the ``main`` branch is updated.

#. Congratulations! You are done with Level 4!

Now that you are done with this tutorial, we provide you how you can further develop your code using pull requests moving forrward in the following section.

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

.. note::

    Make sure you check out the best practices and Billinge group's guidelines for communications and examples in :ref:`frequently-asked-questions`.

Once you are ready to release your package to the wider world, let's proceed to :ref:`level-5-tutorial` where you will learn to release your package to PyPI and conda-forge so that your package can be installed by anyone in the world.
