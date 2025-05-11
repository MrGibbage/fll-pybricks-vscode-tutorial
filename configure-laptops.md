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

## Summary
Because most of these configurations are saved in the .vscode folder, once you do a pull the settings that are saved there are pretty much done. You only have to do three things after doing the first pull:

1. Install the keybindings extension, which should have happened if you chose to install all of the recommended extensions anyway, so now there is only one thing left to do
2. Set up the snippets in the profile
3. Set the environment variable

[Next: Clone a repo](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/clone-push.md)
