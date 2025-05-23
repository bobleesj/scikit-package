.. _level-5-tutorial:

(Level 5) Share your code as a publicly installable package
===========================================================

Overview
--------

Welcome! By the end of the tutorial, you will be able to share your code as a publicly installable package that can be installed using ``pip install <package-name>`` and ``conda install <package-name>``.

Prerequisites
^^^^^^^^^^^^^

We assume that you have a basic understanding of starting a new project and have hosted at least one project on GitHub. If you are new to GitHub, we recommend starting with the :ref:`level-4-tutorial` where you will learn how to create a new project and host it on GitHub.

Make sure you have the latest version of ``scikit-package`` installed:

.. include:: ../snippets/scikit-installation.rst


Step 1. Create a new project with ``scikit-package``
--------------------------------------------

#. Run the following command to create a new project folder with ``scikit-package`` using the Level 5 ``public`` template.

    .. code-block:: bash

        $ package create public

#. Answer the following questions:

    .. include:: ../snippets/user-input-level-5.rst

#. Now type ``ls`` to check a new folder has been created.

Install and test the new package locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#. Enter into the Level 5 project directory.

    .. code-block:: bash

      $ cd <project_name>

.. include:: ../snippets/test-package-locally.rst

#. Done! Let's learn how to now build the documentation locally.


Build documentation locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^

``/doc`` is the the Sphinx documentation folder. The documentation will be built locally first and then automatically built and hosted on GitHub Pages when a new release is created.


.. include:: ../snippets/doc-local-build.rst


Step 2. Create a new repository on GitHub
-----------------------------------------

.. include:: ../snippets/github-create-new-repo.rst

.. _github-codecov-setup:

Setup Codecov token for GitHub repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/github-codecov-setup.rst

.. _github-news-ci-permission:

Allow GitHub Actions to write comments in PRs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As you will see in the next section, we'd like to have GitHub Actions write comments such as warnings. Let's specify the permissions in the GitHub repository settings by following the steps below.

.. include:: ../snippets/github-ci-permission.rst

.. _github-news-item-PR:


Step 3. Push your code to GitHub repository
-------------------------------------------

Add news items in the GitHub pull request
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../snippets/news-item-PR.rst

What's next?
------------
