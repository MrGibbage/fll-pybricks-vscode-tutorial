As the team members write code for their missions, we will need to make sure all team members have a copy of that code. Additionally, the BaseRobot class and master program will also need to be replicated on each laptop. Finally, we will want as many settings as possible to be replicated through the same process. This is the beauty of git/github. We will store all team code, along with certain configuration settings in the team repo. That way when a team member does a pull from github, they will get the latest versions and updates. The only thing is, performing a github pull is meant to be a manual step, and expecting the team members to do that frequently enough may be expecting a little too much.

We automate our github pulls so that at the very least everyone will get a fresh copy of the repo at the start of practice. We have a small script in the .vscode folder that runs whenever the project folder is opened. Of course, if someone doesn't CLOSE the project folder at the end of practice, when they come back to practice the next day, their project will still be open and the update script won't actually run. So it isn't perfect, but so far it has been Good Enough.

The .vscode\tasks.json file has the following code that is triggered whenever the project is opened:

```json
{
    "label": "git pull on startup",
    "type": "shell",
    "command": "python ${fileWorkspaceFolder}\\.vscode\\gitpull.py",
    "windows": {
        "command": "python ${fileWorkspaceFolder}\\.vscode\\gitpull.py"
    },
    "presentation": {
        "reveal": "always",
        "panel": "new"
    },
    "runOptions": {
        "runOn": "folderOpen"
    },
    "problemMatcher": []
}
```

If you study that code, you will see that the "runOn" is set to "folderOpen". That's how it gets triggered whenever the folder is opened. If someone has the project open, then exits out of VS code, then when they reopen VS Code, this will trigger. The "command" setting is what is actually run. You can see that we run a python program, so let's take a look at that.

```python
import os
import subprocess

import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        seconds -= 1

robot_name = os.getenv("robotName")

if robot_name:
    print(f"\033[92mYour robot name is {robot_name}\033[0m")
else:
    print(
        "\033[91mYour robotName environment variable has not been set\033[0m"
    )

print("git pull in five seconds")
countdown(5)
subprocess.run(["git", "pull"])
```

There's not a whole lot here, but bascially it checks to see if the robotName environmnet variable has been set, and if so, prints the value. The weird codes like \033[92m set colors so the printing is in color. Then there is a five second delay and then it performs the git pull.

Remember that the kids can do a git pull at any time by going to the "Source Control" in the left had quick menu, and then clicking on the three dot menu and choosing "Pull".

Because these files are saved in the repo itself, if you ever need to update them, it's just a matter of making the update and doing a git push. Once it has been pushed, then the next time the team member does a pull, they will have your updates. Now, that means any team member could make a change to those files, and then push them to the repo, potentially breaking the automation. I have never seen that with any of my teams. One thing I do is hide the .vscode folder (along with a lot of other folders and files) from them. More on that in the "[Configure settings](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-settings.md)" section.

[Next: How to update VS Code Extensions](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-extensions.md)