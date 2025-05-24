Before merging to ``main``, we require that each PR includes a file documenting the changes under ``\news``. This ensures that the changes are documented in the ``CHANGELOG.rst`` when you create a new release, as shown in https://scikit-package.github.io/scikit-package/release.html, for example.

    .. important::

        If no news file is created for this PR, the CI will not only fail but also write a comment to remind you to create a news file. Recall we granted GitHub Actions permission to write comments in the PR in the previous section.

Let's create a news item for the changes made in this PR.

#. Get the latest updates from the remote GitHub repository.

    .. code-block:: bash

        $ git fetch --all

#. Check out the ``skpkg-public`` branch and sync with the remote branch.

    .. code-block:: bash

        $ git checkout skpkg
        $ git pull origin skpkg

#. Make a copy of ``news/TEMPLATE.rst`` and rename to ``news/<branch-name>.rst``.

#. (optional) If you are using a Linux shell, you can setup an ``alias`` to make the creation of the news file ready for editing much quicker and easier. Read :ref:`faq-github-news-automate` to learn how to setup shortcuts.

#. Do not delete ``news/TEMPLATE.rst``. Leave it as it is.

#. Do not modify other section headers in the rst file. Replace ``* <news item>`` with the following item:

    .. code-block:: text

        **Added:**

        * Support public releases with scikit-package by migrating the package from Level 4 to Level 5 in the scikit-package standard.

#. Push the change to the remote GitHub repository.

    .. code-block:: bash

        $ git add news/skpkg-public.rst
        $ git commit -m "chore: Add news item for skpkg-public"
        $ git push origin skpkg-public
