# The End is Never

A package to make an LLM talk with itself for eternity.

## Requirements

- GPU with CUDA support (recommended, can use Google Colab)
  - If you want to use the CPU (not recommended because it's slow, but it works):
    - Before running `pip install -r requirements.txt` as mentioned in the first step of the [Local Setup](#local-setup) section below:
      1. Remove `torch`, `torchvision`, and `torchaudio` from `requirements.txt`
      1. Follow the instructions [here](https://pytorch.org/get-started/locally/) to install PyTorch without CUDA support
- ~6GB of free disk space (for the LLM)

## Local Setup

1. Install conda if necessary:

    ```bash
    # Install conda: https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation
    # If on Windows, install chocolately: https://chocolatey.org/install. Then, run:
    # choco install make
    ```

2. Create the conda environment and install pip packages locally:

    ```bash
    git clone https://github.com/andrewhinh/theendisnever.git
    cd theendisnever
    conda env update --prune -f environment.yml
    conda activate theendisnever
    pip install -r requirements.txt
    cd ..
    rm -rf theendisnever
    ```

3. In a `.py` file, import and run the package:

   ```python
   from theendisnever import theend
   theend.isnever() # This should run forever unless a (known) issue occurs or you stop it; if not, wrap it in a while True loop
   ```
