Contributing to SCT
===================

Thank you for your interest in contributing to Spinal Cord Toolbox! 🎉

Please refer to SCT's `GitHub Developer Wiki <https://github.com/spinalcordtoolbox/spinalcordtoolbox/wiki/Contributing>`__ for contributing guidelines.

Local Python environment
------------------------

With ``uv`` installed, run these commands from the repository root to create
a Python 3.11 environment and install SCT in editable mode with its runtime
dependencies and development tools:

.. code-block:: console

    uv python install 3.11
    uv venv --python 3.11 .venv
    uv pip install --python .venv --index-strategy unsafe-best-match -r requirements.txt --editable . pytest flake8 build

The index strategy matches pip's selection across PyPI and the CPU PyTorch
index specified in ``requirements.txt``. Runtime dependencies are installed
separately from the package metadata, as in the SCT installers.

Activate the environment with ``source .venv/bin/activate`` on Linux/macOS or
``.\.venv\Scripts\Activate.ps1`` in Windows PowerShell. Then run:

.. code-block:: console

    python -m pytest testing/api/test_math.py testing/api/test_qmri.py
    uv build

Pytest downloads the official test dataset on its first run. Tests that use
segmentation models or native SCT tools also require the corresponding assets
installed by ``install_sct`` (``install_sct.bat`` on Windows).
