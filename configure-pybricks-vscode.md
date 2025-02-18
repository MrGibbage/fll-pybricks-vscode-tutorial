# VS Code Configuration and Automation

There are several tasks that you will need to do frequently as a team member writing code for your missions. As a coach, you will want to be able to explain to the team members how to do things such as uploading and running code on the robot. This section address the automation and configuration that I recommend. You can skip this section if you think you and your team are going to do everything manually.

This section will adress a couple of settings:
* Hiding certain files from the VS Code interface
* Simplifying GitHub pushes

And it will also address what are called "tasks" in VS Code:
* Automating GitHub Pulls
* Running mission code on robots (includes master programs and single mission programs)

Again, you don't have to do any of these, but I do think it helps the kids a lot.

## Settings
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

The first section, "files.exclude", define the list of files and folders that I don't want visible in the VS Code file panel. There is a good [help page here](https://code.visualstudio.com/docs/editor/codebasics#_advanced-search-options) on the patterns for file matching. As you can probably tell, the first few entries in our settings are for folders, and the last few entries are for some specific files that we don't want visible to everyone.

By the way, this ONLY hides the files/folders in the VS Code interface. Anyone can still open the windows explorer and see/edit these files. What's more, all files in the repo will be pushed to GitHub **UNLESS** you include them in your .gitignore file. These are two very different things.

### Simplifying GitHub pushes
One other thing that we did was to save one extra button click for GitHub pushes. The default is to prepare a git commit, add a commit message, and then commit the commit (yes, it is a verb and a noun). Afterwards, to get the commit into the GitHub repo, you have to do a push (sync). The setting above `"git.postCommitCommand": "sync"` saves that last button click and automatically syncs every time they do a git commit. Not  ahuge deal, but still nice.

You can see a couple of the other settings we have configured in our settings.json file. I won't go into them here.

I do sync the settings.json file in our repo so that every laptop will have the same settings.

## Tasks
Tasks are like macros in VS Code. You can configure them to do a lot of different things. Then you can assign keybindings to the tasks and you can do things like press ctrl-shift-L and that will upload the current program to the team member's robot and run it.

Tasks are configured in .vscode/tasks.json

Here is our tasks.json file:

<details>
<summary>Click to expand</summary><p>

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Run on my robot",
            "type": "shell",
            "command": "${workspaceFolder}/.venv/Scripts/pybricksdev.exe",
            "args": [
                "run",
                "ble",
                "--name",
                "${env:robotName}",
                "${file}"
            ],
            "problemMatcher": {
                "owner": "python",
                "fileLocation": [
                    "absolute"
                ],
                "pattern": {
                    "regexp": "^(.*)File(.*)(C:(.*)\\.py)(.*)(line(\\s*))([0-9]+),",
                    "file": 3,
                    "line": 8
                }
            },
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared",
                "showReuseMessage": false,
                "clear": false,
                "revealProblems": "onProblem"
            }
        },
        {
            "label": "Run master_program.py on robot",
            "type": "shell",
            "command": "${workspaceFolder}/.venv/Scripts/pybricksdev.exe",
            "args": [
                "run",
                "ble",
                "--name",
                "${env:robotName}",
                "master_program.py"
            ],
            "problemMatcher": {
                "owner": "python",
                "fileLocation": [
                    "absolute"
                ],
                "pattern": {
                    "regexp": "^(.*)File(.*)(C:(.*)\\.py)(.*)(line(\\s*))([0-9]+),",
                    "file": 3,
                    "line": 8
                }
            },
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared",
                "showReuseMessage": false,
                "clear": false,
                "revealProblems": "onProblem"
            }
        },
        {
            "label": "git pull on startup",
            "type": "shell",
            "command": "${fileWorkspaceFolder}\\.vscode\\gitpull.cmd",
            "windows": {
                "command": "${fileWorkspaceFolder}\\.vscode\\gitpull.cmd"
            },
            "presentation": {
                "reveal": "always",
                "panel": "new"
            },
            "runOptions": {
                "runOn": "folderOpen"
            },
            "problemMatcher": []
        },
        {
            "label": "Run on alt robot",
            "type": "shell",
            "command": "${workspaceFolder}/.venv/Scripts/pybricksdev.exe",
            "args": [
                "run",
                "ble",
                "--name",
                "${input:robotName}",
                "${file}"
            ],
            "problemMatcher": {
                "owner": "python",
                "fileLocation": [
                    "absolute"
                ],
                "pattern": {
                    "regexp": "^(.*)File(.*)(C:(.*)\\.py)(.*)(line(\\s*))([0-9]+),",
                    "file": 3,
                    "line": 8
                }
            },
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared",
                "showReuseMessage": false,
                "clear": false,
                "revealProblems": "onProblem"
            }
        },
        {
            "label": "Run master_program.py on any robot",
            "type": "shell",
            "command": "${workspaceFolder}/.venv/Scripts/pybricksdev.exe",
            "args": [
                "run",
                "ble",
                "--name",
                "${input:robotName}",
                "master_program.py"
            ],
            "problemMatcher": {
                "owner": "python",
                "fileLocation": [
                    "absolute"
                ],
                "pattern": {
                    "regexp": "^(.*)File(.*)(C:(.*)\\.py)(.*)(line(\\s*))([0-9]+),",
                    "file": 3,
                    "line": 8
                }
            },
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "shared",
                "showReuseMessage": false,
                "clear": false,
                "revealProblems": "onProblem"
            }
        }
    ],
    "inputs": [
        {
            "type": "pickString",
            "id": "robotName",
            "description": "Which Robot?",
            "options": [
                "BOB",
                "CURIOSITY",
                "GABE",
                "LEROYYY",
                "MITZVAH",
                "NOTDECLAN",
                "OAKS",
                "PATRIOT",
                "SUPERNOVA",
                "TIM",
                "TIMOTHY"
            ]
        }
    ]
}
```

</p></details>

### Automating GitHub pulls
I have a task that does a GitHub pull every time VS Code is started up. That way I can be sure that everyone has the latest code. If you look through the tasks.json file, you will see a line for "Git pull on startup". The code there does exactly what you would expect-when the user opens VS Code, it will do a git pull right away so they have the latest code. The runOn folderOpen is what triggers it.

### Running Mission code on the robots
We have a couple of different use cases. The first thing to understand is that each team member gets their own robot and they will use that robot for the entire season. All of our practice robots are built the same, so it really doesn't matter which one they choose. As we get closer to the tournaments, we shift to primarily using one robot--the one we are taking to the tournament. Therefore, each team member will need to configure their laptop to know what robot they are using. We do that by setting a Windows Environment Variable called robotName to the name of their robot (you can choose any variable name you want). You can search the internet for Windows Environment Variables (maybe add the Windows version you are using to the search items), but basically if you click on the start menu, then start typing "env", you should see an option to "Edit environment variables for your account". Add a variable called robotName and set it to the pybricks name of your robot (you will set the name when you flash the pybricks firmware).

![Screenshot 2025-02-17 191224](https://github.com/user-attachments/assets/b6ee2aa0-a973-4d56-9841-5dd167b1d3b6)


Uppercase/lowercase is important, so make you whatever you choose, you set it correctly here. In other words, if your robot pybricks name is "Bob", you need to use the same upper/lower case here.

![Screenshot 2025-02-17 191412](https://github.com/user-attachments/assets/5509df6d-259c-4a34-b3ca-5f7131df713c)

The first entry in the tasks.json is to "Run on my robot"

```json
"label": "Run on my robot",
            "type": "shell",
            "command": "${workspaceFolder}/.venv/Scripts/pybricksdev.exe",
            "args": [
                "run",
                "ble",
                "--name",
                "${env:robotName}",
                "${file}"
            ],
```

Explanation of the settings:
* type: shell -> run in a command shell
* command: "${workspaceFolder}/.venv/Scripts/pybricksdev.exe" -> runs the pybricksdev.exe command, which should be located in the .venv/Scripts folder within your project
* args -> These are all of the command line options that would normally follow the pybricksdev command if you were to run it manually (which you could, if you wanted).  For example, this would be a valid command: `pybricksdev.exe run ble --name BOB mission1.py`. You can see the `run` (which means to run the program we are editing), `ble` (which means to use BlueTooth Low Energy, the wireless connection that the Spike hub uses), `--name`, followed by `"${env:robotName}"` (which gets the robotName environment variable that we set), and finally the `${file}`, which is the name of the currently open file. So this task gets all of those commands, bundles them all up and runs them when triggered.

Speaking of triggering, the way we do it is ctrl-shift-L will always run the current program on YOUR robot. ctrl-alt-L allows you run your program on an alternate robot. You can see the list of robots at the bottom of the tasks.json. This will bring up a list of all of our robots and the user can select any robot they want. Be careful with this. We have had kids accidentaly run a mission on a robot that someone else was working on and suddenly have that robot drive off a desk. For that reason you may choose to not do that. Finally, we have a task to run the master program. This one is handy because sometimes the team member will be editing their mission code, but still want to run it from the master program. No matter what python program is currently being edited, this will always run the master program instead.

To set the keybindings, press ctrl-shift-P, then start typing "keyb", and choose "Preferences: Open Keyboard Shortcuts (JSON)"

