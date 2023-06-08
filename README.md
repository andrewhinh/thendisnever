# The End is Never

A script to make an LLM talk with itself for eternity.

## Requirements

- GPU with CUDA support
- ~6GB of free disk space

## Setup

1. Install conda if necessary:

    ```bash
    # Install conda: https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation
    # If on Windows, install chocolately: https://chocolatey.org/install. Then, run:
    # choco install make
    ```

2. Create the conda environment and install pip packages locally:

    ```bash
    git clone https://github.com/andrewhinh/phatic.git
    cd phatic
    conda env update --prune -f environment.yml
    conda activate phatic
    pip install -r requirements.txt
    export PYTHONPATH=.
    echo "export PYTHONPATH=.:$PYTHONPATH" >> ~/.bashrc (or ~/.zshrc)
    # If on Windows, the last two lines probably won't work. Check out this guide for more info: https://datatofish.com/add-python-to-windows-path/
    ```

3. Run the script:

   ```bash
   . ./run.sh
   # This reruns `main.py` in case downloading model/some other issue occurs, so rest assured this will happen for eternity.
   ```
