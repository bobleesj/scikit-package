
``/doc`` is the the Sphinx documentation folder. The documentation will be built locally first and then automatically built and hosted on GitHub Pages when a new release is created.

#. Install dependencies for documentation. The ``requirements/docs.txt`` file contains the dependencies needed to build the documentation:

    .. code-block:: bash

        conda install --file requirements/docs.txt

#. Install an external tool called ``sphinx-reload`` to automatically reload the documentation when you make changes to ``.rst`` files:

    .. code-block:: bash

        pip install sphinx-reload

    .. note::

        ``sphinx-reload`` is only available via pip install.

#. A new webpage will appear automatically by running the following command:

    .. code-block:: bash

        sphinx-reload doc

#. Done! Once you are ready for public release, we will learn to host this documentation on GitHub Pages via public URL.
