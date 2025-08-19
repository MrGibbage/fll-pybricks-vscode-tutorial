# Clone the Team Repo
You will need a copy of the repo on each laptop. Cloning copies the existing code in a repo into a folder on your local computer. Then, as team members edit their code, they will then "push" those changes to the team repo on GitHub. Then in oder for everyone to have a copy of the most current code, each team member will "pull" the updates from GitHub. Most of these steps are automated with our setup [which you can learn here](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-team-mission-code.md).

Steps:

1. Copy the link to the repo
2. Clone the repo in VS code
3. Create a python virtual environment
4. Create a new python file
5. Push the file to GitHub

All of these steps will need to be performed on each laptop.

## Step 1. Copy the link to the github repo
Using the laptop you are setting up, go to the github page for your repo. Make sure you are logged into github as the user that you are setting up (team member or coach). Then get the link to the repo by clicking the green "code" button.

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

Open a terminal window by typing ctrl-shift-` (hold down the ctrl and shift keys while tapping on the back-tick, which is the key to the left of the number 1 key at the top of your keyboard).

![image](https://github.com/user-attachments/assets/dd93a880-bf3d-434f-acea-7cb57a7d8462)


Type `uv sync` and press enter. You'll see some text scroll by and hopefully no errors.

![image](https://github.com/user-attachments/assets/43728f85-75fa-43ba-8726-12d9428ac608)


In particular, we should see pybricks and pybricksdev near the middle of the list. The virtual environment is created.

Next, we need to activate the virtual environment. Down in the lower right, click on the python environment tag

![image](https://github.com/user-attachments/assets/197794ff-e23a-4a6c-8d7e-cfc5009e844f)


Up at the top of the screen with the command pallete, click on the new (and probably recommended) environment.

![image](https://github.com/user-attachments/assets/79bb0768-9ec2-40f3-bb3d-96a531d7f7d6)


Notice the new tag at the bottom shows the correct environment is selected. Click on the trash can to kill the terminal.

![image](https://github.com/user-attachments/assets/53cca446-fbb5-43f9-83dc-c4d35d691a53)


Now open the terminal one more time with ctrl-shift-`. Notice that the terminal prompt shows the activated environment in parenthesis at the beginning.

![image](https://github.com/user-attachments/assets/1941a7ba-de84-456a-aba8-b4802b757b1a)


## VS Code Extensions
If you have your repo set up like ours, you should get prompted to install some VS Code extensions at this point. We keep a list of recommended extensions in our .vscode folder, and VS Code will recognize that when cloning our repo. The coaches and the team members will use those extensions to make the whole experience better. You can just click "Yes" to install the recommended extensions, but if you ever want to install something else, here's how you do it. If you clicked "Yes" and the extensions are installing, jump down to Step 4.

### Manually installing extensions in VS Code
Click on the fourth icon on the left side (it looks like four blocks, but one block is pulled out). Or you can press ctrl+shift+X

![Screenshot 2025-02-02 121453](https://github.com/user-attachments/assets/1eaa603b-f33e-4fc1-af15-b8fbcb958064)

Coaches and team members should install the python extension, which will also install the pylance extension. The only other *required* extension at this time is GitHub Pull Requests (by GitHub). Use the search bar above the list of extensions to look for "Github" and select it from the list.

![Screenshot 2025-02-16 101911](https://github.com/user-attachments/assets/d52ff211-904a-4374-b764-e5a15f5134d4)

There are some other extensions that coaches and certain team members may find useful, depending on their roles. Read the descriptions for each of these and decide if you want or need them.
* GitLens — Git supercharged (by GitKraken)
* Live Share (by Microsoft)
* TODO Tree (by Gruntfuggly)
* Codeium: AI Coding Autocomplete and Chat for Python, Javascript, Typescript, Java, Go, and more (by Codeium) **OR** GitHub copilot, Google Gemini, and several others. This tutorial will not address using AI, so that is up to you to figure out. I can tell you there are some good ones and I really like having them as an option.
* Black Formatter (by Microsoft) <-- Strongly recommend for coaches and team members
* Error Lens (by Alexander) <-- Strongly recommend for coaches and team members
* git-autoconfig (by shyykoserhiy) <-- strongly recommend for coaches and team members

Once you have all of the extensions installed, we'll be done with VS Code for now. Next we will install git for windows.

## Step 4. Test push update to GitHub
The last thing we will do is a test push to GitHub. You did keep that GitHub window open like I said in step 1, right? On the left hand side of the VS Code window, you should see a list of files. If you don't see the list of files, click on the top icon in the toolbar. Then click on the "New File..." icon. Give your file a name such as test, and type something in it like "hello world". Press ctrl-s to save it. 

![Screenshot 2025-02-17 143403](https://github.com/user-attachments/assets/2d40f234-8f6a-42da-a6c4-faaf7b0cafea)

Notice that the third icon in the tool bar now has a "1". That indicates that there is one update that hasn't been pushed to GitHub, so let's do that.

![Screenshot 2025-02-17 143834](https://github.com/user-attachments/assets/f2ecf180-521c-4e74-9802-4469122c4e15)

Now click on that third icon with the "1". We need to prepare the "commit" first. A "commit" is just a snapshot for git. Write a short commit message, something that identifies what this commit is about. It could be "solved mission #4", or "just testing". Whatever works for you. Then click on the "Commit and Sync" button.

![Screenshot 2025-02-17 144140](https://github.com/user-attachments/assets/8d932c35-8eeb-455f-bb00-75ba2a93d522)

At this point you may get a message that you need to authenticate with GitHub. Just click through and follow the instructions. If that all works, then you are fully connected to GitHub.

Finally, you may get some type checking warnings in VS Code, alerting you to some problems when using the pybricks Axis and Color classes. Just use the special comment `# type: ignore` to make VS Code (or more accurately, Pylance) ignore the error.

[Next: Updating Team mission code (pulls and pushes)](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-team-mission-code.md)
