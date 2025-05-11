# Environment variables

## Explained

Environment variables are used by many operating systems. It's a way of telling the OS certain parameters. For example, a running process can query the value of the TEMP environment variable to discover a suitable location to store temporary files, or the HOME or USERPROFILE variable to find the directory structure owned by the user running the process. We use an environment variable to store the name of the robot the team member uses the most, to make it easy to run their code on their own robot.

## Updating
The first thing to understand is that each team member gets their own robot and they will use that robot for the entire season. All of our practice robots are built the same, so it really doesn't matter which one they choose. As we get closer to the tournaments, we shift to primarily using one robot--the one we are taking to the tournament. Therefore, each team member will need to configure their laptop to know what robot they are using. We do that by setting a Windows Environment Variable called robotName to the name of their robot. You can search the internet for Windows Environment Variables (maybe add the Windows version you are using to the search items), but basically if you click on the start menu, then start typing "env", you should see an option to "Edit environment variables for your account" (make sure to choose the one that says "for your account", and not the "system" option). Add a variable called robotName and set it to the pybricks name of your robot (you will set the name when you flash the pybricks firmware).

![Screenshot 2025-02-17 191224](https://github.com/user-attachments/assets/b6ee2aa0-a973-4d56-9841-5dd167b1d3b6)


Uppercase/lowercase is important, so make you whatever you choose, you set it correctly here. In other words, if your robot pybricks name is "Bob", you need to use the same upper/lower case here.

![Screenshot 2025-02-17 191412](https://github.com/user-attachments/assets/5509df6d-259c-4a34-b3ca-5f7131df713c)

As you can see, this is a manual process. It won't take long for the team members to learn how to do this on thier own.