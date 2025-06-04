Why do I need a news file for each PR?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We want to write good ``CHANGELOG.rst`` for each release version. These news items are of interest to both developers and technical users looking for specific keywords. We can streamline the process of writing ``CHANGELOG.rst`` for each release by compiling the news items from the ``news`` directory.

Here is an example ``CHANGELOG.rst`` https://github.com/scikit-package/scikit-package/blob/main/CHANGELOG.rst

How do I create a news file?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. In your repository, confirm the ``news/TEMPLATE.rst`` file exists,

#. We want to make a copy of ``news/TEMPLATE.rst`` and name it as ``news/<branch-name>.rst``. Let's automate the process creating the news file and add new items by running the commands:

    .. code-block:: bash

        $ package add news --add -m "<Describe the first feature added in the PR.>"
        $ package add news --a -m  "<Describe the second feature added in the PR.>"

    .. note::

        As shown above, you may use ``-a`` or ``--add``. The second flag ``-m`` stands for ``message``.

#. Confirm that your ``news/<branch-name>.rst`` has the following content:

    .. code-block:: text

            **Added:**

            * <Describe the first feature added in the PR.>
            * <Describe the second feature added in the PR.>

            **Changed:**

            * <news item>

            **Deprecated:**

            * <news item>

            **Removed:**

            * <news item>

            **Fixed:**

            * <news item>

            **Security:**

            * <news item>

    .. note::

        Once you are happy with the news item(s) that you have added, you don't need to modify anything in ``news/<branch-name>.rst`` and ``news/TEMPLATE.rst``.


Where do I place my news item in ``<branch-name>.rst``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``**Added:**`` (``-a``, ``--add``) includes features or functionality of interest to users and developers, such as support for a new Python version or the addition of a useful feature.
- ``**Changed:**`` (``-c``, ``--change``) includes modifications that affect end-users or developers, such as API changes or dependencies replaced.
- ``**Fixed:**`` (``-f``, ``--fix``)  includes bug fixes or refactoring.
- ``**Deprecated:**`` (``-d``, ``--deprecated``) includes methods, classes, or workflows that are no longer supported in the future release.
- ``**Removed:**`` (``-r``, ``--remove``) includes the opposite of the "Added" section, referring to features or functionality that have been removed.
- ``Security:**`` (``-s``, ``--security``) : includes fixes or improvements related to vulnerabilities, authentication, or access control.

How do I write good news/CHANGLEOG?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Maintain consistency:

    a. Start with an active verb.
    b. Capitalize the first word.
    c. End with a period
    d. Use the ``rst`` style of backquotes instead of the markdown style of backquotes. For example, use ````scikit-package```` instead of ```scikit-package```.

    e.g., Add automatic linting of ``.md``, ``.yml``, ``.rst`` files via prettier hook in pre-commit.

My PR has trivial fixes that shouldn't be in ``CHANGELOG.rst``. Should I still create a news file?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. In this case,we want to communiate with the reviewer(s) the reason it should not be in the ``CHANGELOG.rst``. You can simply run the following:

    .. code-block:: bash

        $ package add no-news -m "<brief-reason>."

You will see a new file has been created ``news/<branch-name>.rst``

    .. code-block:: text

        **Added:**

        * No news: <brief-reason>

        ...
