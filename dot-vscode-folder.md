# What is .vscode and where is it?

There is a folder in the project called .vscode (yes, it starts with a dot). While you may not always see it in the file explorer within VS Code, it is there.

<img width="574" height="120" alt="image" src="https://github.com/user-attachments/assets/798b40a8-9546-4a60-a967-3c6a0a3b37cc" />

What is so special about this folder is that it contains a lot of the settings for our "project" in VS Code. A project is really nothing more than a folder with files and perhaps other folders. When you open a folder in VS Code, you also open everything that is in it. At that point it becomes a project in VS Code. And that includes the .vscode folder. Since that folder is a part of the project, you can have individual "per-project" settings in VS Code. For us this probably isn't a big deal since the team members are probably not using VS Code for anything else other than FLL, but the settings are stored there anyway.

As you do a lot of the confiuration here, just remember that a lot of these settings are saved in the repository along with the team mission files. So that means everyone will have the same settings.

Here are the files in the .vscode folder

<img width="662" height="179" alt="image" src="https://github.com/user-attachments/assets/691fe4c6-e133-4aa4-8933-5887694ca2b6" />

extensions.json is a list of VS Code extensions that we use.
gitpull.cmd is a PowerShell command script for doing a git pull (not used any more)
gitpull.py is a python program for doing a git pull
settings.json has VS Code settings, such as what files to hide in the project browser
tasks.json are the VS Code tasks, such as Ctrl-L to launch our program on the robot
unearthed-snippets.code-snippets are the snippets we use to make the programming faster and easier
