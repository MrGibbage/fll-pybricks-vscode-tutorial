# Creating and configuring GitHub repositories for FLL teams
GitHub repositories (or "repos", plural of "repo") are like projects. You are reading this tutorial in a repo. There are thousands of tutorials online about how to use GitHub (and git... they are not the same!)


## Create the Repository in the Team Account
This will only need to be done once for each season. The coach will probably do this, but if you have a team member that knows what they are doing, they could certainly do this. The team account will be used to hold all of the repos for the team. I have a new repo for each season. You may decide to just continue using the same repo each year. Both will work, and it is just up to you. If you decide to reuse the same repo each year you can skip this step.

Be sure you are logged in with the team account. To create a new repo using the team account, click the "New" button in the top left of the screen. Give your repo a name and optional description. You can make it public or private as desired (all of our repos are public). All of the other options are optional. I usually just ignore them. Click on "Create Repository" and you are done. 

Next you can start adding some files and folders to your repo, or you can add the collaborators. It really doesn't matter which one is done first. In fact, allong the way you (as coach) may need to add some more files, or add more collaborators (for instance, if a new team member joins the team). These are both things that you can do at any point during the season.

## Collaborators
These steps assume you are starting with a new repo. If you are reusing an old repo, just clear out any collaborators that aren't needed and add in the new ones using the same steps as when you added them before.

To start you should have two laptops. You could do it with one, but you will spend a lot of time logging in and out of different accounts. On one laptop log into GitHub with one of the team member accounts. On the other, log in as the Team account and start there.

In GitHub, collaborators will have the ability to add new files, edit existing files, and even delete files. They will have full ownership of all of the repo files. If that sounds scary, don't be worried. This is GitHub. Everything is logged, so you will know who did what, and everything is reversible. You can always go back in time. I have never had a problem where someone was messing with a file that they shouldn't have. 

These steps will need to be completed for each collaborator (team member/coaches). To add a collaborator, click on the repo settings (make sure you are logged in as the team account):

![Screenshot 2025-02-16 085945](https://github.com/user-attachments/assets/dc9ae865-7729-44c4-a920-393ae7218860)


Right up at the top is the Collaborator link

![Screenshot 2025-02-16 090145](https://github.com/user-attachments/assets/745b5865-04dc-4877-8015-5bf49565e3ba)


Click on the Add People button

![Screenshot 2025-02-16 090253](https://github.com/user-attachments/assets/d8037a20-5f1d-46df-a9f3-957e79f1c981)


Search for the account name of one of the team members or coaches and add them

![Screenshot 2025-02-16 090728](https://github.com/user-attachments/assets/88da1796-94b5-4df1-ba58-464f48d87d7b)


Assuming you invited a team member that is logged into GitHub on a different laptop, go to that laptop and accept the invite. It may take a minute or two, but that user should get a new message in their inbox.

![Screenshot 2025-02-16 091348](https://github.com/user-attachments/assets/eee70851-7dad-4f39-bf79-8592f3f10457)


Here is the invite message in the inbox.

![Screenshot 2025-02-16 091506](https://github.com/user-attachments/assets/41012439-9c99-4cfc-a346-74f582592a3f)


And once you click on the message, you will see this

![Screenshot 2025-02-16 091636](https://github.com/user-attachments/assets/29768f15-d10a-4be1-be46-561aa32df7eb)


Click on "Accept" and then go back to the team account laptop. If you go into the collaborator settings again, you will see that the account is now listed as a collaborator. Do that again for all of the team members and coaches as desired.


## Season Files
### Python files
If you look at one of our past seasons, such as https://github.com/FLL-Team-24277/FLL-Fall-2024-Submerged, you will see how we do it. Each run from base has a python file of its own. We also have a master_program.py and a base_robot.py file. The master program is the sequencer that manages and runs the mission files at the right time. In pybricks there are several ways to manage this. Our team uses the light sensor to detect which attachment is installed and then launches the correct mission for that attachment. There are other ways to do such as [this method provided by pybricks](https://docs.pybricks.com/en/stable/tools/index.html#pybricks.tools.hub_menu). Is part of the team's job to figure out how that will be managed. There are other python files saved in the top level of the repo such as different utility programs and testing programs as needed. To start a new season, I will usually put in the last season base_robot, master_program, and a sample mission file so there is something to work off of.

### Help folder
I have a "help" folder where we put build instructions for the base robot, base attachment, and season mission model build instructions. The mission model build instructions are available on firstinspires, but I want them locally on the laptops in case they are needed. Basically, just put any other files such as packing lists, to-do lists, innovation project scripts, rubrics, season updates, etc. that you think the team may need during the season. 

### .vscode folder
You may have also noticed the .vscode folder in our repo. And yes, that folder name starts with a dot. That folder contains files for the VS Code workspace configuration. I include it in the repo so that all of the laptops will be configured the same way. In that folder there are three files that we use to help automate some of the GitHub work that we do, and to automate uploading code to the robot and running it. Read [here to learn more about the VS code configuration for pybricks and FLL teams](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/configure-pybricks-vscode.md).

### .gitignore
.gitignore is a special file that you can include at the top of your repo, and yes, the filename does tart with a dot. There are some files and folders that really don't make sense to store on github, such as compiled python code and virtual python environments. Also, from a security point of view, you may want some sensitive files to not be uploaded to GitHub (for instance, that file where you are saving the passwords for your team members). There are many tutorials online about .gitignore if you want more information. This is the .gitignore file that we typically use:

```
# Will not sync these

/.venv/
/.git/
__pycache__/
~*

# will sync .gitiginore 
!/.gitignore
```

[Next: Clone a repo in VS Code](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/clone-push.md)
