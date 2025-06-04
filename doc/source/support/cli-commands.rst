.. index:: cli-commands

.. _cli-commands:

========================================
Summary of useful ``skpkg-cli`` commands
========================================

Here we summarize ``skpkg-cli`` commands. While these are embedded in our tutorials and guides, it can be helpful to have a single place for advanced users and ``scikit-package`` maintainers. If you have any suggestions or questons, please feel free to leave GitHub issues.

    **package update conda-forge**

        - Streamline your ``conda-forge`` version update after PyPI/GitHub full release. 
        - This command creates a PR to from ``<username>/<latest-version>`` to ``upstream/main`` after modifying ``meta.yaml`` with the latest version and its SHA256 sourced from PyPI. 
        - Ensure you have configured ``feedstock_path`` in ``~/.skpkgrc``. For more, please refer to :ref:`conda-forge-pr-automate`.

    **package add news --add -m "<message>"**

        - Streamline a news file creation and writing process for each PR.
        - Create ``news/<branch.rst>`` and append the news item under ``**Added:**``. ``--add`` can be replaced with ``-a``. Other available flags are ``--change``, ``--fix``, ``--deprecate``, ``--remove``, ``--security`` or  ``-c``, ``-f``, ``-d``, ``-r``, ``-s``.
        - For best practices, please refer to :ref:`news-item-practice`.

    **package add no-news -m "<brief-reason>"**
        
        - Streamline a news file creation that is skipped during ``CHANAGELOG.rst`` compiliation.
        - Create ``news/<branch.rst>`` and append the news item of ``No news: <brief-reason>`` under ``**Added:**``.
