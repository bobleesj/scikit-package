.. index:: migration-guide

.. _migrate-existing-package-to-level-5:

Migrate your existing package with ``scikit-package``
=====================================================

Prerequisites
-------------

This guide is for developers who have an existing Python package that is under Git control and want to migrate it to Level 5 ``scikit-package`` standard. We assume you have already created a package using ``scikit-package`` Level 4 and Level 5. We will also use a forking workflow. If you are not familiar with contributing via forking,  please read :ref:`faq-github-forking-workflow-overview`.

Tips and how to receive support
-------------------------------

We understand that migration can be challenging. We offer the following ways to help guide migrate your package to ``scikit-package``:

#. You may cross-check with the Billinge group's up-to-date package, ``diffpy.utils``: https://github.com/diffpy/diffpy.utils.

#. If you have any questions, first read the :ref:`frequently-asked-questions` for how to customize your package and certain design decisions in the ``scikit-package`` template.

#. After you've cross-checked and searched through the FAQ, please feel free to ask questions by creating an issue on the ``scikit-package`` repository `here <https://github.com/scikig-package/scikit-package/issues>`_.


.. include:: ../snippets/scikit-installation.rst

.. _migration-pre-commit:

Step 1. Pre-commit workflow
---------------------------

#. If haven't, clone the repository and set ``upstream`` to the original repository.

    .. code-block::

        $ git clone <URL-of-the-forked-repo>
        $ cd <package-name>
        $ git remote add upstream <URL-of-the-original-repo>

    .. note::
        
        Are you the creator of the repository? You can type ``origin`` instead of ``upstream`` in the rest of the tutorial. e.g., ``git pull origin main`` instead of ``git pull upstream main``. Here, we assume a forking workflow.

Run ``black`` in your codebase
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Create a new branch called ``black-edits``. This branch will be used to apply ``black`` to all files in the old project directory.

    $ git checkout main
    $ git pull upstream main
        

#. Activate the conda environment and install ``black``:

    $ conda activate skpkg-env
    $ conda install black

#. Create a new branch called ``black-edits`` and create a new file called ``pyproject.toml``::

    $ git checkout -b black-edits
    $ touch pyproject.toml

#. Copy and paste the following content at the bottom of ``pyproject.toml``:

    [tool.black]
    line-length = 79
    include = '\.pyi?$'
    exclude = '''
    /(
        \.git
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | \.rst
    | \.txt
    | _build
    | buck-out
    | build
    | dist
    | blib2to3
    | tests/data
    )/


#. Type ``black .`` to lint the code. To skip certain files, add them under the ``exclude`` section in the ``pyproject.toml`` file above.

#. Push the changes to the ``black-edits`` branch:

    .. code-block:: bash
    
     $ git add .
     $ git commit -m "skpkg: apply black to all files in the project directory"
     $ git push origin black-edits

#. Create a PR from ``username/black-edits`` to ``upstream/main``. The PR title can be ``skpkg: apply black line-length 79 to all files in the project directory``.

    If your default branch is called ``master``, run ``git pull upstream master`` instead. However, ``main`` is the new default branch name for GitHub.

#. Review and wait for the PR to be merged to ``upstream/main``. If you are the project maintainer, you can merge the PR yourself.

#. Done!

Apply pre-commit auto-fixes without manual edits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Sync with the ``upstream/main`` branch::

     $ git checkout main && git pull upstream main

#. Create a new branch called ``pre-commit-auto``::

    $ git checkout -b pre-commit-auto

#. Create a new package using ``scikit-package``::

    $ package create publicly
    
#. Copy the ``pre-commit`` configuration files from the new to the old directoy::
    
    $ cp <package-name>/.pre-commit-config.yaml .
    $ cp <package-name>/.isort.cfg .
    $ cp <package-name>/.flake8 .

#. Trigger hooks and auto-fixes without manual edits::

    $ pre-commit run --all-files

#. Add the changes to the ``pre-commit-auto`` branch::

    $ git add . && git commit -m "style: apply pre-commit hooks with no manual edits"``

#. Push the changes to the remote repository::
    
    $ git push origin pre-commit-auto

#. Create a PR from ``username/pre-commit-auto`` to ``upstream/migration``. The PR title can be ``skpkg: apply pre-commit to project directory with no manual edits``.

    .. note::

        The new ``upstream/migration`` branch can be created by the project maintainer or owner. On the main page of the upstream repository, click :menuselection:`main -> Switch branches/tags -> Find or create a branch` and type ``migration``. This will create a new branch called ``migration``.

#. Wait for the PR to be merged to ``upstream/migration`` branch.

Apply manual edits to pass ``pre-commit`` hooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The package will most likely have failed pre-commit hooks. We will manually fix the errors raised by ``flake8``, ``codespell``, etc. Here, instead of fixing all errors at once, we will address each type of error one at a time.  For example, a branch called ``pre-commit-spelling`` contained spelling fixes, while another branch, ``pre-commit-flake8-line`` contained fixes of line length errors raised by flake8.


#. Sync with the ``upstream/migration`` branch::

    $ git checkout migration
    $ git pull upstream migration
    $ git checkout -b pre-commit-<theme>

#. Run ``pre-commit run --all-files`` to see the errors.

    Do you want to ignore certain files/folders and also set the preferred line-length? Visit :ref:`faq-pre-commit` to learn how to customize line-lenghts, ignore certain errors, and skip certain files and paths. If you have suprress any errors for the prupose of migration, you can create GitHub issues to track them.

#. Create a PR to ``upstream/migration``. Since you are fixing flake8 errors, the commit message can be ``skpkg: fix flake8 line-length errors`` and the pull request title can be ``skpkg: fix flake8 line-length errors``.

#. Repeat for other errors but ensure you always pull the latest changes from ``upstream/migration`` before creating a new branch::

    $ git checkout migration
    $ git pull upstream migration
    $ git checkout -b pre-commit-<another-theme>

#. After all pre-commit hooks pass, setup ``pre-commit`` hooks to trigger automatically moving forward::

    $ pre-commit install

Setup pre-commit CI
^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-pre-commit-setup.rst

Congratulations if you have successfully passed all the pre-commit hooks! You can now proceed to the next section.

.. _migration-workflow:

Step 2. Migration workflow
--------------------------

Let's migrate existing files from the old project to the new project directory.

.. Attention:: Please read the following carefully before proceeding:

    - Do NOT delete/remove any files before confirming that it is absolutely unnecessary. If you are unsure, contact the project maintainer first.

    - Do NOT delete project-specific content such as project descriptions in README, license information, authors, tutorials, examples.

Folder structure
^^^^^^^^^^^^^^^^

#. Sync with the ``main`` branch by typing ``git checkout main && git pull upstream main``.

#. Before migration, we want to make sure your existing package is structured as a standard recommended Python.

    For a standard package, it should be structured as follows:

    .. code-block::

        <package-name>/
        ├── src
        │   ├── <package_name>
        │   │   ├── __init__.py
        │   │   ├── file_one.py
        │   │   ├── file_two.py

    For a package with namespace import, it should be structured as follows:

    .. code-block::

        <package-name>/
        ├── src
        │   ├── <package_name>
        │   │   ├── __init__.py
        │   │   ├── file_one.py
        │   │   ├── file_two.py
                ├── ...

.. _migration-guide-start-new-project:

Move ``src``, ``tests``, ``requirements`` to setup GitHub CI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Type ``mv ../.git .`` to move ``.git`` to the re-packaged directory created by ``scikit-package``. Please note that there is a ``.`` in ``mv ../.git .``.

#. Type ``git status`` to see a list of files that have been (1) untracked, (2) deleted, (3) modified.

    - ``untracked`` are new files created by the ``scikit-package``

    - ``deleted`` are files in the old directory but the files that are not in the new directory. Most of the ``src`` and ``tests`` and doc files will be in this category. We will move them from the old to the new directory in the next few steps.

    - ``modified`` are files that that exist both in the old and the new directory, while the scikig-package has made changes to them.

#. Type ``git checkout -b setup-CI`` to create a new branch.

#. Notice there is a ``requirements`` folder containing ``pip.txt``, ``tests.txt``, ``docs.txt``, ``conda.txt``. List dependencies. For ``pip.txt`` and ``conda.txt``, you will most likely have the same dependencies listed. Please check the FAQ section on why we provide both ``pip.txt`` and ``conda.txt`` files :ref:`here<faq-dependency-files>`.

#. Type ``git add requirements && git commit -m "skpkg: create requirements folder"``.

#. Now you will move ``src`` and ``tests`` folders in the following steps.

#. Type ``cp -n -r ../src .`` to copy the source code from the ``main`` to the sk-packaged directory, without overwriting existing files in the destination.

#. Type ``cp -n -r ../tests .``.

#. Run ``git diff`` and the differences

#. Then run ``pytest`` locally to ensure the tests are running as expected.

#. Type ``git add src && git commit -m "skpkg: move src folder"``.

#. Type ``git add tests && git commit -m "skpkg: move tests folder"``.

#. Type ``git add .github && git commit -m "skpkg: move and create github CI and issue templates"``.

    .. Attention::
        If your package does not support Python 3.13, you will need to specify the Python version supported by your package. Follow the instructions here to set the Python version under ``.github/workflows`` :ref:`here <github-actions-python-versions>`


#. Push the changes to the ``CI`` branch by typing ``git push origin CI``.

#. Create a PR from ``CI`` to ``package``. The pull request title can be ``skpkg: move src, tests and setup requirements folder to setup CI``.

#. Notice there is a CI running in the PR. Once the CI is successful, review the PR merge to ``package``.

2.4. Move configuration files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Sync with the ``package`` branch by typing ``git checkout package && git pull upstream package``.

#. Copy all configuration files that are, ``.codecov.yml``, ``.flake8``, ``.isort.cfg``, ``.pre-commit-config.yaml`` files from the main repo to the scikit-package repo.

2.5. Move rest of text files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Files showing as (2) "deleted" upon git status are in the main repo but not in the scikit-package repo. We took care of most of these by moving over the src tree, but let's do the rest now. Go down the list and for <filename> in the ``git status`` "delete" files type ``cp -n ../<filepath>/<filename> ./<target_filepath>``. Do not move files that we do not want. If you are unsure, please confirm with the project maintainer.

#. Files that have been (3) modified exist in both places and need to be merged **manually**. Do these one at a time. Differences will show up. Select anything you want to inherit from the file in the main repo. For example, you want to copy useful information such as LICENSE and README files.

.. _scikit-package-workflow-doc:

3.1. Move documentation files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. We want to copy over everything in the ``doc/<path>/source`` file from the old repo to the ``doc/source`` file in the new repo.

#. If you see this extra ``manual`` directory, run ``cp -n -r ../doc/manual/source/* ./doc/source``.

#. If files are moved to a different path, open the project in PyCharm and do a global search (ctrl + shift + f) for ``../`` or ``..`` and modify all relative path instances.

#. Any files that we moved over from the old place, but put into a new location in the new repo, we need to delete them from git. For example, files that were in ``doc/manual/source/`` in the old repo but are not ``doc/source`` we correct by typing ``git add doc/manual/source``.

3.2. Render API documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/api-reference-doc.rst

3.3. Build documentation locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/doc-local-build.rst

.. _scikit-package-workflow-cleanup:

4. Clean up
-----------

4.1. Check LICENSE and README
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. For the ``package`` branch, make a ``<branchname>.rst`` file by copying ``TEMPLATE.rst`` in the news folder and under "fixed" put ``Repo structure modified to the new diffpy standard``

#. Check the `README` and make sure that all parts have been filled in and all links resolve correctly.

#. Run through the documentation online and do the same, fix grammar and make sure all links work.

#. Recall in your local, you are currently in the re-packaged directory.

4.2. Clean up the old directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Then rename the old directory to ``mv ../../<package-name> ../../<package-name>-old``. You will have then ``user/dev/<package-name>/<package-name>`` and ``user/dev/<package-name>-old/<package-name>``.

#. Type ``../..`` to go back to the ``dev`` directory.

#. Type ``git clone <https://github.com<org-name>/<project-name>``.

#. Test your package by running ``pytest``.

    .. include:: ../snippets/pytest-run-local.rst

#. Good to go! Once the test is successful, you can delete the old directory by typing ``rm -rf <package-name>-old``.

Ready for public release?
--------------------------

Congratulations! Your package has been successfully migrated. This has been the most challenging step. Now, let's release your package to PyPI and conda-forge. Please visit the :ref:`Release your package <release-pypi-github>` page to learn how to release your package!
