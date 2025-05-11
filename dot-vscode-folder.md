# What is .vscode and where is it?

There is a file in the project called .vscode (yes, it starts with a dot). While you may not always see it in the file explorer within VS Code, it is there.

Here is the top of the file explorer within VS Code


But if you press ctrl-o to open an existing file, you should see the .vscode folder in there. If it isn't there then you did not create your repo from a copy of mine, in which case you can create it manually. Here is the file browser after pressing ctrl-o


What is so special about this folder is that it contains a lot of the settings for our "project" in VS Code. A project is really nothing more than a folder with files and perhaps other folders. When you open a folder in VS Code, you also open everything that is in it. At that point it becomes a project in VS Code. And that includes the .vscode folder. Since that folder is a part of the project, you can have individual "per-project" settings in VS Code. For us this probably isn't a big deal since the team members are probably not using VS Code for anything else other than FLL, but the settings are stored there anyway.

As you do a lot of the confiuration here, just remember that a lot of these settings are saved in the repository along with the team mission files. So that means everyone will have the same settings.