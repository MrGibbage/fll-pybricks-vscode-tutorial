# Install UV

[UV](https://github.com/astral-sh/uv) is a package manager and virtual environment manager that we use to ensure all laptops are configured the same way. It's a very simple install with one line to paste into an admin PowerShell

```PowerShell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Using the PowerShell method above will install a uv binary into the current user's home directory. This may not be ideal for shared domain laptops. In that case, use pip to install uv in your global python installation (not in a virtual environment).

```Python
pip install uv
```

After cloning a repo, we will run `uv sync` to set up the python environment

[Next: Create a repository and invite collaborators](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/github-season-repo.md)
