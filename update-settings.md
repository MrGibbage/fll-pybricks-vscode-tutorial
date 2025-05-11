# VS Code Settings

There are several tasks that you will need to do frequently as a team member writing code for your missions. As a coach, you will want to be able to explain to the team members how to do things such as uploading and running code on the robot. This section address the automation and configuration that I recommend. You can skip this section if you think you and your team are going to do everything manually.

This section will address a couple of settings:
* Hiding certain files from the VS Code interface
* Simplifying GitHub pushes

Again, you don't have to do any of these, but I do think it helps the kids a lot.

## Explained
There are many different settings that are configurable in VS Code. These are two of the ones I think you will find helpful.

### Hiding files in the VS Code Interface
There are some files the team members will never need to see in the VS Code interface. I choose to hide them just to keep things neat and easier for the team members. This is a file called settings.json, and it is saved in the .vscode folder in your project folder. You can get to this file pretty easily by typing ctrl-shit-P, then start typing "preferences". Look for an entry that says "Preferences: Open Workspace Setting (JSON)" (be sure it says "workspace" and not "keybindings"... we'll be editing that file later).
<details>
<summary>Click to expand</summary><p>

```json
{
    "files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/.hg": true,
        "**/CVS": true,
        "**/.DS_Store": true,
        "**/Thumbs.db": true,
        "**/.venv/": true,
        "**/.vscode/": true,
        "**/__pycache__/": true,
        "**/.gitignore": true,
        "**/README.md": true,
        "base_robot*.py": true,
        "requirements.txt": true,
        "pyproject.toml": true,
        "colorTest.py": true,
        "master_program.py": true,
        "utils.py": true
    },
    "task.allowAutomaticTasks": "on",
    "git.postCommitCommand": "sync",
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter",
        "editor.formatOnSave": true
    },
    "codetogether.virtualCursorJoin": "sharedVirtualCursor",
    "editor.rulers": [
        80
    ],
    "black-formatter.args": [
        "--line-length",
        "79"
    ]
}
```
</p></details>

The first section, "files.exclude", defines the list of files and folders that I don't want visible in the VS Code file panel. There is a good [help page here](https://code.visualstudio.com/docs/editor/codebasics#_advanced-search-options) on the patterns for file matching. As you can probably tell, the first few entries in our settings are for folders, and the last few entries are for some specific files that we don't want visible to everyone.

By the way, this ONLY hides the files/folders in the VS Code interface. Anyone can still open the windows explorer and see/edit these files. What's more, all files in the repo will be pushed to GitHub **UNLESS** you include them in your .gitignore file. These are two very different things.

I choose to hide our master_program.py and base_robot.py files because most of the kids will not need to edit it. The more advanced kids that help out with writing the base_robot.py file, and the master_program.py file will know that they can always type ctrl-o and browse to the files they need.

### Simplifying GitHub pushes
One other thing that we did was to save one extra button click for GitHub pushes. The default is to prepare a git commit, add a commit message, and then commit the commit (yes, it is a verb and a noun). Afterwards, to get the commit into the GitHub repo, you have to do a push (sync). The setting above `"git.postCommitCommand": "sync"` saves that last button click and automatically syncs every time they do a git commit. Not a huge deal, but still nice.

You can see a couple of the other settings we have configured in our settings.json file. I won't go into them here.

## Updating

The settings.json file is saved in .vscode in the repo so that every laptop will have the same settings. If you make changes to it, they will automatically be updated on all laptops the next time they do a pull.

[Next: How to update environment variables](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-env-variable.md)