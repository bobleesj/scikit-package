Before merging to ``main``, we require that each PR includes a file documenting the changes under ``\news``. This ensures that the changes are documented in the ``CHANGELOG.rst`` when you create a new release, as shown in https://scikit-package.github.io/scikit-package/release.html, for example.

    .. important::

        If no news file is created for this PR, the CI will not only fail but also write a comment to remind you to create a news file. Recall we granted GitHub Actions permission to write comments in the PR in the previous section.

Let's create a news item for the changes made in this PR.

#. Get the latest updates from the remote GitHub repository.

    .. code-block:: bash

        $ git fetch --all

#. Check out the ``skpkg-migration`` branch and sync with the remote branch.

    .. code-block:: bash

        $ git checkout skpkg-migration
        $ git pull origin skpkg-migration

#. Make a copy of ``news/TEMPLATE.rst`` and rename to ``news/<branch-name>.rst``.

#. (optional) If you are using a Linux shell, you can setup an ``alias`` to make the creation of the news file ready for editing much quicker and easier:


    Add the following line to ``~/.bashrc`` or ``~/.zshrc`` file:

    .. code-block:: bash

        $ alias cpnews="cp news/TEMPLATE.rst news/$(git rev-parse --abbrev-ref HEAD).rst"

    Run the following command to apply the shell configuration.

    .. code-block:: bash

        $ source ~/.bashrc  # if you are using bash
        $ source ~/.zshrc  # if you are using zsh

    Now, whenever you want to create a news file, simply navigate to the top-level directory in the project and type ``cpnews`` on the command line.

    You can then open the project in an editor. The news file located under ``news`` will have the name ``<branch-name>.rst`` where ``<branch-name>`` is replaced by the current branch name.

    Add a description of the edits made in this PR. This should be a user-facing high-level summary of the edits made in this PR and will be automatically converted into the ``CHANGELOG.rst`` when the code is released.

    .. note::

        How do I write good news items? What if the changes in the PR are trivial and no news is needed? Please check out the news guide in the FAQ :ref:`here<news-item-practice>`.


#. Do not delete ``news/TEMPLATE.rst``. Leave it as it is.

#. Do not modify other section headers in the rst file. Replace ``* <news item>`` with the following item:

    .. code-block:: text

        **Added:**

        * Support public releases with scikit-package by migrating the package from Level 4 to Level 5 in the scikit-package standard.

#. Push the change to the remote GitHub repository.

    .. code-block:: bash

        $ git add news/skpkg-migration.rst
        $ git commit -m "chore: Add news item for skpkg-migration"
        $ git push origin skpkg-migration
