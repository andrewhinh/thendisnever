# [The End is Never](pypi.org/project/theendisnever/)

A package to make an LLM talk with itself for eternity.

```python
from theendisnever.theend import isnever
isnever(
  model_name='Fredithefish/ScarletPajama-3B-HF', # Default LLM
  prompt='THE END IS NEVER THE END IS NEVER ', # Default prompt
  max_memory_ratio=0.25 # Default % of latest tokens to remember
)
```

## Notes

For the default LLM (which you can change as shown above), you'll need at least:

- ~ 6GB of free disk space
- ~ 15GB of RAM

When running `isnever()` for the first time, it will download the model and tokenizer from HuggingFace. This will take a while, but it only needs to be done once.

If you want to use the CPU (not recommended because it's slow, but it works), make sure you have [PyTorch for CPU](https://pytorch.org/get-started/locally/) installed.

## Contributing

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
    pip install -r requirements.txt
    ```

1. Make your changes.
  a. Remember to update the `requires` and `version` fields in `pyproject.toml` as necessary

1. Run `python -m build` to build the package, removing old builds from dist/ first if necessary.
1. Run `python -m twine upload --repository theendisnever dist/*` to upload the package to TestPyPI.
1. Run `pip install --index-url https://test.pypi.org/simple/ --no-deps --upgrade theendisnever` in a fresh environment to test the package.
1. Once confirmed to work, make a PR from a feature branch to main on GitHub.
1. Once PR is merged, [email me](ajhinh@gmail.com) to be added as a collaborator on PyPI.
1. Once added as a collaborator, run `python -m twine upload dist/*` to upload the package to PyPI.
