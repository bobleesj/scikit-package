.. index:: cli-commands

.. _cli-commands:

========================================
Summary of useful ``skpkg-cli`` commands
========================================

Here we summarize ``skpkg-cli`` commands. While integrated in our tutorials and guides, it can be helpful to have a source of reference for intermediate to advnaced users and ``scikit-package`` contributors and maintainers. If you have any suggestions or questons, please feel free to leave GitHub issues.

    #. **package update conda-forge**

        - Streamline ``conda-forge`` version update after PyPI/GitHub full release. 
        - This command creates a PR to from ``<username>/<latest-version>`` to ``upstream/main`` after modifying ``meta.yaml`` with the latest version and its SHA256 sourced from PyPI. 
        - Ensure ``feedstock_path`` is provided in ``~/.skpkgrc``. For more, please refer to :ref:`conda-forge-pr-automate`.

    #. **package add news --add -m "<message>"**

        - Streamline creating the news file and writing news item(s) later compiled to ``CHANGELOG.rst``.
        - Create ``news/<branch.rst>`` and append the news item under ``**Added:**``. ``--add`` can be replaced with ``-a``. Other available flags are ``--change``, ``--fix``, ``--deprecate``, ``--remove``, ``--security`` or  ``-c``, ``-f``, ``-d``, ``-r``, ``-s``.
        - For best practices, please refer to :ref:`news-item-practice`.

    #. **package add no-news -m "<brief-reason>"**
        
        - Streamline creating the news file and writing the news item that is skipped during ``CHANAGELOG.rst`` compiliation.
        - Create ``news/<branch.rst>`` and append the news item of ``No news: <brief-reason>`` under ``**Added:**``.
