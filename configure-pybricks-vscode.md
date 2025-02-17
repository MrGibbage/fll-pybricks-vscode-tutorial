# VS Code Configuration and Automation

There are several tasks that you will need to do frequently as a team member writing code for your missions. As a coach, you will want to be able to explain to the team members how to do things such as uploading and running code on the robot. This section address the automation and configuration that I recommend. You can skip this section if you think you and your team are going to do everything manually.

This section will adress a couple of things:
* Hiding certain files from the VS Code interface
* Formatting python code
* Automating GitHub Pulls
* Simplifying GitHub pushes
* Running mission code on robots (includes master programs and single mission programs)

Again, you don't have to do any of these, but I do think it helps the kids a lot.

## Hiding files in the VS Code Interface
There are some files the team members will never need to see in the VS Code interface. I choose to hide them just to keep things neat and easier for the team members. This is a file called settings.json, and it is saved in the .vscode folder in your project folder.
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
The first section, "files.exclude", define the list of files and folders that I don't want visible in the VS Code file panel. 
