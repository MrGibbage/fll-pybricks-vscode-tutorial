# Tasks

## Explained
Tasks in VS Code are used to integrate with external tools and programs. In this case, we want to be able to easily run our code on the robots using the pybricksdev.exe program. You could run this manually instead of configuring it with tasks, but that seemed like it would be too much of a challenege for the middle school kids. Once the tasks are written, they can easily be run with the "command pallete", which you normally access with ctrl-shift-P. Even better, you can run them with keybindings. For example, we have configured keybindings to run the current open program on "my" robot just by pressing ctrl-l (that's "L", for "launch"). We have instructions for configuring keybindings [here](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-keybindings.md)

## tasks.json
In the .vscode folder there is a file "tasks.json" that contains all of the tasks. I mentioned one task earlier that does the automatic pull from github whenever the folder is opened. There are four other tasks in there:

- Run on my robot (runs the currently open program on my robot)
- Run on alt robot (runs the currently open program on an alternative selected robot)
- Run master program on my robot (runs the master program on my robot)
- Run master program on alt robot (runs the master program on an alternative selected robot)

Here is the "Run on my robot" code. All of the others are basically the same:

```json
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
```
The problemMatcher and presentation secions just make the user interface a little smoother, but the main thing are the "command" and "args" settings. The "command" finds and runs pybricksdev.exe, and the "args" are the command line arguments that pybricksdev.exe expects. Of note "${env:robotName}" finds the environment variable called "robotName" and gets the value for that setting. See [how to update the robotName environment variable](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-env-variable.md) for more information.


There is also a section where you will save the names of all of your robots. This is so it can populate the drop down list of robots when using the "alt" options

```json
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
```

The way this works, if the user types ctrl-alt-l, they will see the list of robots to choose from at the top of the screen. The first one in the list will always be the last robot they used.

![image](https://github.com/user-attachments/assets/5d604a0d-df88-4bdb-b88b-13061d2f79ed)

## Updating
Since the tasks.json file is saved in the .vscode folder, it is automatically updated with the repo. If you have any changes to make to the tasks, just make them and push the updated code.

[Next: How to update snippets](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-snippets.md)
