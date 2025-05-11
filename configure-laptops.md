The next few steps are all about making sure all of the team member laptops (including the coaches) are configured identically. So far we have loaded all of the major software, but now let's get into the details.

Our goal is to make sure all of the following components are the same on each laptop:
- Team mission code
- VS Code extensions
- VS Code tasks
- VS Code snippets
- VS Code keyboard shortcuts
- VS Code settings
- Robot named and set as default for each team member

This table defines where the configuration is stored for each item and how that item is updated

| Item          | Storage        | Update method    |
| ------------- | -------------- | ---------------- |
| Team code     | Github repo    | git pull         |
| Extensions    | .vscode folder | git pull/ Manual |
| Tasks         | .vscode folder | git pull         |
| Snippets      | Profile        | git pull/ Manual |
| Keybindings   | Extension      | Update Extension |
| Settings      | .vscode folder | git pull         |
| Robot name    | Environment    | Manual           |

We have a mostly empty repo that is already configured with the settings that will be described in these few steps. That repo is available [here](https://github.com/MrGibbage/pybricks-fll).

[Next: How to update Team mission code](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-team-mission-code.md)
