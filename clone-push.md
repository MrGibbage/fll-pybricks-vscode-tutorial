# Clone a Repo in VS Code
To get started using VS Code as a team member (or coach) to edit/add team files in the repo, you have to first "clone" the repo. Cloning copies the existing code in the repo into a folder on your local computer. Then, as team members edit their code, they will then "push" those changes to GitHub. Then in oder for everyone to have a copy of the most current code, each team member will "pull" the updates from GitHub. Most of these steps are automated with our setup [which you can learn here](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/configure-pybricks-vscode.md). These step do require you have the files in .vscode that I have.

Steps:
1. Copy the link to the repo
2. Clone the repo in VS code
3. Create a python virtual environment
4. Create a new python file
5. Push the file to GitHub

## Step 1. Copy the link to the github repo
Using the laptop you are setting up, go to the github page for your repo. Make sure you are logged into github as the user that you are setting up (team member or coach). Then get the link to the repo.

![Screenshot 2025-02-16 181100](https://github.com/user-attachments/assets/af39f2ce-f6d9-4fc6-98ab-3d7943f866da)

Get the link to the repo and click on the copy icon to copy the link to the clipboard. You will need this link for the next step. Do not close the web browser or close the tab to the repo. Just keep it all open.

## Step 2. Clone the repo in VS Code

Start VS code on the laptop. If it was already running, exit out and start VS code again. Hopefully you see this screen:

![2025-02-16](https://github.com/user-attachments/assets/868596a3-2d60-4f8e-9281-e1c9526a80ec)


Click on the link to "Clone Git Repository...". Then at the top of the screen, paste in the link that you copied earlier.

![Screenshot 2025-02-16 181806](https://github.com/user-attachments/assets/62726949-7c86-4712-9871-ade2dcc32059)


Here I have selected the fll-seasons folder to save the repo. Feel free to choose whatever you want.

![2025-02-16 (1)](https://github.com/user-attachments/assets/21198cd6-6ab0-42b7-9f18-7d4182f02575)

Click on the "Select as Repository Destination" button


Shortly you should see this button. Choose "Open".

![Screenshot 2025-02-16 182239](https://github.com/user-attachments/assets/81b5e1c7-624a-4f3f-a51c-d549b643a683)


You will possibly see this dialog asking if you trust the authors of the files in that folder. Click the check box that you trust the authors of all the files in the parent folder and then click the button that you trust the authors.

![Screenshot 2025-02-16 182341](https://github.com/user-attachments/assets/b03070a5-0730-4065-8a33-f7695cfc6481)


If you chose to install the optional git autoconfig extension when you set up VS code, you will see this popup. I already have some configurations in this screenshot, but you will probably need to create a custom one. Just fill in the email address and name as requested.

![Screenshot 2025-02-16 182635](https://github.com/user-attachments/assets/f8459305-71da-4173-93bd-f72450b3d09e)


There you go! You have cloned the repo. All of the code is now on your local laptop, exactly like it was in the repo.

## Step 3. Create a python virtual environment

Before actually writing code though, you should create a python virtual environment. Virtual environments are a wonderful way of setting up a python environment specifically for each laptop and keep it separate from any other python development projects you have on the laptop.


In VS Code, type ctrl-shift-P to bring up the command pallete. The items at the top of the list will always be the most recently run commands, so your list will look different.

![Screenshot 2025-02-16 183225](https://github.com/user-attachments/assets/19121f94-ac71-4c8f-864f-1524c79e84a7)


Start typing "python" and you will see the list of commands will filter. Select the one that says "Python: Create Environment..."

![Screenshot 2025-02-16 183409](https://github.com/user-attachments/assets/9167c401-1fc5-4a10-961f-3730e712259c)


Choose "venv". Press "enter"

![Screenshot 2025-02-16 183527](https://github.com/user-attachments/assets/6902b859-c5fe-4c8d-96c2-90068b8ad9fe)


You should have a Global python installation. Choose that.

![Screenshot 2025-02-16 183624](https://github.com/user-attachments/assets/b63df736-8a3e-45de-b3d5-a67bf4c3a5a9)


If you watch quickly in the lower right corner, you will see the environment being created;

![Screenshot 2025-02-16 183830](https://github.com/user-attachments/assets/889b621c-06f3-438f-9549-e2afd655426e)

![Screenshot 2025-02-16 183842](https://github.com/user-attachments/assets/733224ed-3262-45d2-b8b3-121d3ef8d2ac)


Next we need to install any python packages that are needed. For sure that will mean installing `pybricks` and `pybricksdev`. I also include the black python formatter. A nice feature for python is that you can put all of the requirements in a requirements.txt file and it is then easy to install them all at once. Otherwise you just have to open a new terminal and run a couple of commands

In VS Code, press ctrl-\` That's ctrl plus the "tick mark", which is the key to the left of the number 1 (shared with the tilde ~). When you press ctrl-\`, a terminal should open up at the bottom of your screen


