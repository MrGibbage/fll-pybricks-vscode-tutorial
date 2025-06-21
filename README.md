# FLL, GitHub, VS Code and pybricks

## Background and introduction
Hello,
I am Skip Morrow. I have been coaching FIRST Lego League (FLL) for over ten years in Virginia-DC ([Team 24277, the Norfolk Collegiate O.A.K.S.](https://github.com/FLL-Team-24277)). In 2020 we switched to Spike Primes. Before that we used EV3's and the LabView programming environment. With the EV3s we always struggled with code sharing and code management. When we switched to Spike Primes, the kids on the team asked if we could use python. Python is an option using the official Spike development software and hub firmware, so yes, we could use python. I was excited that we'd be able to share and manage our code more easily. After doing some more research, I found [pybricks](https://github.com/pybricks), an open source python alternative for Lego hubs. The easiest way to develop using pybricks (and the way that most people use it) is on their [website](https://code.pybricks.com/), which won't meet our needs. However, there is a perfect "workaround" for that, and this page will explain how. I hesitate to call it a workaround, because we are using the software in the way it was intended--it's just that it isn't the most popular way of using pybricks. All in all, I think our solution is pretty much perfect. We can use VS Code, pybricks, and of course, GitHub.

## Decisions, decisions...
This is potentially a very big decision for you and your team. Definitely get your team involved with this decision process. This cannot be a situation where the coach just forces this on a team. This is absolutely a more advanced way of doing FLL, and it isn't for every team. Many, probably MOST, successful FLL teams use the built in Spike firmware and official scratch-like programming, so don't think you HAVE to do this in order to succeed. If you feel determined to use python, there is even an official way to do that with the offical Lego software. You do not have to do it this way, and you have options.

If you and your team think they are ready to make this switch, then here are some other considerations:
* Python learning curve. This is full-on python (or more precisely, micro-python). You will need to know how to write functions that are extensible and reusable so they are easily shared among team members. You and your team will also need to know how to read and use Application Programming Interface (API) documentation for python libraries such as pybricks.
* Git and github learning curve. This is almost certainly new to everyone on your team. You will get a merge conflict at some point, I guarantee it. And when you do, it can be very scary. They are easy to avoid, but we are talking about middle school kids who are used to using things like google docs and google slides where you don't have to save your work or upload changes.
* VS Code learning curve. Most of your team has probably not ever used VS Code, so they will have to learn that too.
* Pyrbicks learning curve. For example, pybricks only has one "slot". If you have been using the Spike or EV3, you probably have your code organized with different missions (runs from base) saved in different slots. Pybricks has one slot. You have to figure out how you will build a master program that will properly launch different missions as needed. There are several ways to do it, but this very much goes back to the python learning curve. You will have to learn the pybricks way of doing everything like movement and using sensors. You will also have to learn how to use pybricksdev.exe, which is how you use pybricks in VS Code. By the way, there is an easier way to use pybricks and still use the scratch-like programming interface, and that is to just use their [web app](https://code.pybricks.com/) (which is actually the default and most common way to use pybricks). I know teams that use the pybricks web app and it seems nice, but I don't personally have any experience with that. We wanted to be able to use VS Code and github, so their web app would not meet that goal.
* You will have to flash specialized firmware on your hubs. This is really easy for someone that has done this many times before, but I know there are people out there very uncomfortable with things like that. I suppose there is risk that you could permanently damage a hub, but I have never heard of anything like that happening. Anyway, if you do turn your brick into a ... BRICK, well, don't blame me! Seriously though, I think it is easy. Just follow the instructions.
* All of that being said, my middle school team wanted to make this switch, and had no problem picking up on all of this. Your mileage may vary.

But there are some very nice benefits to doing it this way.
* The number one reason we switched was because the team wanted to. They asked if we could use python and learn how to program with a "real" programming language using "real" development tools. That was several years ago, and that team is long gone, but as new kids came on the team, they learned everything above and noone has ever asked if we could go back. If your team doesn't want this, then don't do it.
* Pybricks does have some functionality that I don't think is possible in the regular spike software. For one, when driving it is possible to easily drive along a curve. What's more, it is possible to chain movements commands together without having to stop in between commands. This is very nice and very fast.
* Code sharing and backups is automatic with github. If we need to make a change to the master program or base_robot.py, we make the change, push to github, and when the team members do a pull, they will have the latest software. They can also use any team laptop. They all have the same code, so when we go to tournaments, it doesn't matter which laptop we take.
* Some people think the gyro implementation is better and more accurate in pybricks. That may be true, but I don't have much experience using the base firmware, so I don't have anything to compare it to. I'd love to see someone doing some real-life tests that show this to be a fact, but I don't know if that has been done.
* I do think the basic driving implementation is better in pybricks. I don't think the built-in Spike software handles acceleration/deceleration at all, but pybricks does quite well.
* The pybricks developers are very reachable and love to help teams. They are very active on the support pages ([discussions](https://github.com/orgs/pybricks/discussions) and [reporting issues](https://github.com/pybricks/support/issues)) and love seeing FLL teams use their software. Try getting that level of support from Lego if you have questions about your code using the Lego firmware. By the way, Lego has very much endorsed pybricks. There are links to pybricks in several places on the Lego website ([example](https://education.lego.com/en-us/lessons/ev3-real-world-vehicles/speed-control-system/)).

Convinced? Think you and your team are ready for this?

## Goals/Requirements
- [ ] Uses Python
- [ ] Easy code sharing
- [ ] "Real" Integrated Development Environment
- [ ] Enables master program
- [ ] Robot performance should be similar to stock Lego firmware
- [ ] All team member laptops should be set up the same way with a repeatable, documented process. While this goal should theoreticaly be possible with any solution, the goal is to keep it simple, and in a way such that if we need to update something in the setup for the laptops, it is as automatic as possible

## Proposed Solution
- [ ] Pybricks
- [ ] Enables code sharing via GitHub
- [ ] VS Code
- [ ] Master program will work
- [ ] Robot performance will be similar to stock Lego firmware
- [ ] All team member laptops will indeed be set up the same way with a repeatable, documented process.

## What is needed
To get started, you'll need these things:
* A lego hub such as EV3 or Spike Prime. Our team uses Spike Primes, so this tutorial will be Spike Prime-focused. But I think the steps are pretty much the same for EV3s if you are using them.
* Laptop(s). I use Windows, but I think it will all work on a Mac. I cannot confirm. You will need admin access to the laptop because you will be installing software on it.
* Software and user accounts described below. Don't worry, everything is FREE.
* A coach with ownership rights for the team repository on GitHub. The coach will invite collaborators (team members) to be able to edit the files in the repository

## Pybricks vs the built-in Spike python
First, I never used the official Lego Spike python, other than some simple tests. Maybe it can meet all of our goals/requirements. But with my quick tests, I didn't see an easy way to have a master class where we could share methods among the team members. I also didn't see how we'd be able to get all of our code on one laptop. I also felt the official Spike python development software lacking certain features like intellisense and code completion. All of these really led me to think it wasn't an option for us.

## Is all of this necessary?
Short answer is no, all of this is not necessary. If you want to just use pybricks, VS Code and Github, you could do it in a couple of minutes. Obviously you have to have VS Code installed, and a repo to store your code at Github (and if you don't need Github, you can skip that too). You will then have to pip install pybricks and pybricksdev
```bash
pip install pybricks
pip install pybricksdev
```

Then write a simple pybricks program, such as

```python
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

# Optionally, uncomment the line below to use the gyro for improved accuracy.
# drive_base.use_gyro(True)

# Drive forward by 500mm (half a meter).
drive_base.straight(500)

# Turn around clockwise by 180 degrees.
drive_base.turn(180)

# Drive forward again to get back to the start.
drive_base.straight(500)

# Turn around counterclockwise.
drive_base.turn(-180)
```
And finally upload it to your Spike Hub

```bash
pybricksdev.exe run ble --name ROBOTNAME sample_mission.py
```

That should get your robot moving. But if you want to automate as much of this as possible, and keep things simple for a team of middle school kids, then you might want to consider some of the steps below.

## Steps
1. [Set Up Coach and team member accounts on GitHub](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/github-accounts.md)
2. Install software on a laptop (coaches and team members)
   - [VS Code](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/install-vs-code.md)
   - [Git (for Windows)](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/install-git.md)
   - [Python](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/install-python.md)
   - [UV](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/install-uv.md)
   - [Spike V3 software](https://education.lego.com/en-us/downloads/spike-app/software/) (Optional, no instructions in this tutorial) 
   - [Bricklink stud.io](https://www.bricklink.com/v3/studio/download.page) (Optional, no instructions in this tutorial) 
3. [Create a GitHub repository for the season (coach)](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/github-season-repo.md)
4. [Configure team member laptops](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/configure-laptops.md)
   - [Clone the team repository](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/clone-push.md)
   - [Updating Team mission code](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-team-mission-code.md)
   - [VS Code Extensions](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-extensions.md)
   - [Tasks](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-tasks.md)
   - [Snippets](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-snippets.md)
   - [Keybindings](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-keybindings.md)
   - [VS Code Settings](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-settings.md)
   - [Environment Variables](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-env-variable.md)
7. [Install pybricks on your robot](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/install-pybricks.md)
8. TODO Test running a program on the robot
9. [Optional: What is the .vscode folder?](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/dot-vscode-folder.md)

[Next: Set Up Coach and team member accounts on GitHub](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/github-accounts.md)
