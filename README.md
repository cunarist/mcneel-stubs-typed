> This is a fork of the original `mcneel/pythonstubs` repository. Modifications are focused on improving type hint support.

# McNeel Python Stubs

[![PyPI](https://img.shields.io/pypi/v/Rhino-stubs.svg)](https://pypi.org/project/Rhino-stubs)

Python stubs for .NET assemblies that ship with Rhino. Specifically:

- [Rhino-stubs](https://pypi.org/project/Rhino-stubs/)
- [Eto-stubs](https://pypi.org/project/Eto-stubs/)
- [Grasshopper-stubs](https://pypi.org/project/Grasshopper-stubs/)
- [GH-IO-stubs](https://pypi.org/project/GH-IO-stubs/)
- [GH-Util-stubs](https://pypi.org/project/GH-Util-stubs/)

For more details about the purpose of these packages, see the following posts:

- [Autocomplete while editing Python scripts outside of Rhino](https://discourse.mcneel.com/t/autocomplete-while-editing-python-scripts-outside-of-rhino/79329) on the Rhino forums
- [Autocomplete and Type Hints with Python Scripts for Rhino/Grasshopper](https://stevebaer.wordpress.com/2019/02/25/autocomplete-and-type-hints-with-python-scripts-for-rhino-grasshopper) on Steve Baer's Notes

## Using with [VSCode](https://code.visualstudio.com/)

1. Open your project in VSCode.
2. Open a terminal.
3. Depending on the Python package manager you are using, install the stub packages into your project environment. While using `pip` is possible, we recommend using the `poetry` or `pipenv` package manager.

   ```sh
   pip install Rhino-stubs
   ```

4. Now you can import `Rhino` or `Grasshopper` and use the autocomplete feature as well as type prediction.

   ![Stub preview](static/rhino-stub-vscode.gif)
