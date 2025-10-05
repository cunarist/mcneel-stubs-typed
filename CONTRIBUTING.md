## Preparation

Install system dependencies.

- https://visualstudio.microsoft.com/
- https://code.visualstudio.com/
- https://docs.astral.sh/uv/

## Commands

Create the Python virtual environment.

```shell
uv sync
```

Generate Python stubs code from Binary files.

```shell
uv run scripts/build_rhino_stubs.py
```

Publish packages.

```shell
uv build --all-packages
uv publish
```
