#. Deactivate your conda environment and create a new conda environment. Below, replace ``<max_python_version>`` with, for example, |PYTHON_MAX_VERSION|.

    .. code-block:: bash

        $ conda deactivate
        $ conda create -n <project_name>-env python=<max_python_version>
        $ conda activate <project_name>-env

#. Install the dependencies listed in ``requirements/conda.txt`` and ``requirements/test.txt``:

    .. code-block:: bash

        $ condaa install \
            --file requirements/test.txt \
            --file requirements/conda.txt \

#. Install the package mode and run the unit tests:

    .. code-block:: bash

        $ pip install .
        $ pytest