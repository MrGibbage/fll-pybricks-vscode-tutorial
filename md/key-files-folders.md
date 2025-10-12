# Key files and folders/directories within our project

There are some files and folders/directories (I will usually just use the term "folder" from here on) that you should have in your project folder. Most have been discussed in other places throughout this turorial. To organize everything, I will briefly discuss them here.

## Non-python files

## What is .vscode and where is it?

There is a folder in the project called .vscode (yes, it starts with a dot). While you may not always see it in the file explorer within VS Code, it is there.

<img width="574" height="120" alt="image" src="https://github.com/user-attachments/assets/798b40a8-9546-4a60-a967-3c6a0a3b37cc" />

What is so special about this folder is that it contains a lot of the settings for our "project" in VS Code. A project is really nothing more than a folder with files and perhaps other folders. When you open a folder in VS Code, you also open everything that is in it. At that point it becomes a project in VS Code. And that includes the .vscode folder. Since that folder is a part of the project, you can have individual "per-project" settings in VS Code. For us this probably isn't a big deal since the team members are probably not using VS Code for anything else other than FLL, but the settings are stored there anyway.

As you do a lot of the confiuration here, just remember that a lot of these settings are saved in the repository along with the team mission files. So that means everyone will have the same settings.

Here are the files in the .vscode folder

<img width="662" height="179" alt="image" src="https://github.com/user-attachments/assets/691fe4c6-e133-4aa4-8933-5887694ca2b6" />

**extensions.json** is a list of VS Code extensions that we use.   
**gitpull.py** is a python program for doing a git pull  
**settings.json** has VS Code settings, such as what files to hide in the project browser  
**tasks.json** are the VS Code tasks, such as Ctrl-L to launch our program on the robot  
**unearthed-snippets.code-snippets** are the snippets we use to make the programming faster and easier 

## .gitignore

.gitignore (starts with a dot) is used to define any files that should not be pushed to the git/github repo. For example, you will never push your python virtual environment because each laptop needs to generate the virtual environment for itself. If this folder was included in the github repo, it would then attempt to synchronize across all devices. THerefore, you will see an entry in .gitignore:

/.venv/

By having this line  in .gitignore, that instructs git to not include .venv in the repo

Similarly, we don't synchronize the .git folder in each repo. That folder very much needs to be generated and maintained locally on each computer.

However, we DO want to synchronize the .gitignore file itself. THere fore we have a line in our .gitignore file to make sure it always gets pushed

!/.gitignore

There are many websites that discuss the use of .gitignore, as well as websites that discuss recommended best practices for what files should and/or should not be included in a repo

## pyproject.toml and requirements.txt

These two files are pretty similar in purpose, but there are important differences. It doesn't hurt to have both of them, but you will probably only actually use one of them.

### pyproject.toml

The pyproject.toml file is used by uv, which we generally use for managing our python environments. The most important lines in it are

dependencies = [  
    "pybricks==3.6.1",  
    "pybricksdev==2.0.0",  
]

These two lines will make sure your virual environment have pybricks and pybricksdev. The other lines are important for making sure each environment is exactly the same across each computer.

### requirements.txt

This file is for listing all of the packages required for the project virtual environment when using the venv tool. You will see the same two requirements here:

pybricks==3.6.1  
pybricksdev==2.0.0

## Python files

These will vary depending on how you want to structure your projects. We organize our project with all of the .py files in the top level of the project. So that will include 
mission1.py  
mission2.py  
etc  

As well as our other shared files, such as
base_robot.py  
master_program.py

