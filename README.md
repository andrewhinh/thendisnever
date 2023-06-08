# The End is Never

A package to make an LLM talk with itself for eternity.

## Requirements

- GPU with CUDA support (recommended, can use Google Colab)
  - If you want to use the CPU (not recommended because it's slow, but it works):
    - Before running `pip install -r prod.txt` as mentioned in the first step of the [Setup](#setup) section below:
      1. Remove `torch`, `torchvision`, and `torchaudio` from `prod.txt`
      1. Follow the instructions [here](https://pytorch.org/get-started/locally/) to install PyTorch without CUDA support
- ~6GB of free disk space (for the LLM)
- ~15GB of RAM (for the LLM)

## Setup

1. Install conda if necessary:

    ```bash
    # Install conda: https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation
    # If on Windows, install chocolately: https://chocolatey.org/install. Then, run:
    # choco install make
    ```

1. Create the conda environment and install pip packages locally:

    ```bash
    git clone https://github.com/andrewhinh/theendisnever.git
    cd theendisnever
    conda env update --prune -f environment.yml
    conda activate theendisnever
    pip install -r prod.txt
    cd ..
    rm -rf theendisnever
    ```

1. Run the package:

   ```bash
   python -c "from theendisnever.theend import isnever; isnever()"
   ```

## Contributing

1. [Email me](ajhinh@gmail.com) to be added as a collaborator (on GitHub, TestPyPI, and PyPI)
1. Follow the steps in the [Setup](#setup) section above, except:
  a. Replace `pip install -r prod.txt` with `pip install -r dev.txt`, keeping in mind this change for the [Requirements](#requirements) section above if applicable
1. Make your changes
  a. Remember to update the version number in `pyproject.toml` as necessary

1. Run `python -m build` to build the package, removing old builds from dist/ first if necessary
1. Run `python -m twine upload --repository theendisnever dist/*` to upload the package to TestPyPI
1. Run `pip install --index-url https://test.pypi.org/simple/ --no-deps --upgrade theendisnever` in a fresh environment to test the package
1. Once confirmed to work, make a PR from a feature branch to main on GitHub
1. Once PR is merged, run `python -m twine upload dist/*` to upload the package to PyPI
