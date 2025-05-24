.. seealso::

    You can also find "dead" code in your codebase. You can do so by installing ``vulture`` and running the following command:

    .. code-block:: bash

        $ conda install vulture
        $ vulture src/ tests/

    This will generate a report of unused code in the ``src`` and ``tests`` directories. Below is an example of what these outputs might look like. You can then review the report and decide whether to remove the identified unused code.

    .. code-block:: bash

        #### Example outputs after running vulture ####
        $ vulture src/ tests/
        src/module1.py:10: unused function 'helper_function' (60% confidence)
        src/module2.py:45: unused variable 'temp_var' (80% confidence)
        tests/test_module1.py:22: unused import 'os' (100% confidence)

    For more details on how ``vulture`` works, visit the `vulture GitHub repository <https://github.com/jendrikseipp/vulture>`_.
