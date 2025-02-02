# FLL, GitHub, VS Code and pybricks

## Background and introduction
Hello,
I am Skip Morrow. I have been coaching FIRST Lego League (FLL) for over ten years in Virginia-DC ([Team 24277, the Norfolk Collegiate O.A.K.S.](https://github.com/FLL-Team-24277)). In 2000 we switched to Spike Primes. Before that we used EV3's and the LabView programming environment. We always struggled with code sharing and code management. When we switched to Spike Primes, the kids on the team asked if we could use python. It turns out we could. I was excited that we'd be able to share our code more easily. But the Spike software required us to use their official development software. After doing some more research, I found [pybricks](https://github.com/pybricks), an open source python alternative for lego hubs. But even pybricks is more or less set up for doing development on their website. However, there is a perfect workaround for that. All in all, I think our solution is pretty much perfect. We can use VS Code, pybricks, and of course, GitHub.

## Decisions, decisions...
This is potentially a very big decision for you and your team. Definitely get your team involved with this decision process. This cannot be a situation where the coach just forces this on a team. This is absolutely a more advanced way of doing FLL, and it isn't for every team. Many, probably MOST, successful FLL teams use the built in scratch-like programming, so don't think you HAVE to do this in order to succeed. 

If you and your team think they are ready to make this switch, then here are some other considerations:
* Python learning curve. This is full-on python (or more precisely, micro-python). You will need to know how to write functions that are extensible and reusable so they are easily shared among team members. You and your team will also need to know how to read and use documentation for python libraries such as pybricks.
* Git and github learning curve. This is almost certainly new to everyone on your team. You will get a merge conflict at some point, I guarantee it. And when you do, it can be very scary. They are easy to avoid, but we are talking about middle school kids who are used to using things like google docs and google slides where you don't have to save your work or upload changes.
* VS Code learning curve. Most of your team has probably not ever used VS Code, so they will have to learn that too.
* Pyrbicks learning curve. For example, pybricks only has one "slot". If you have been using the Spike or EV3, you probably have your code organized with different missions (runs from base) saved in different slots. Pybricks has one slot. You have to figure out how you will build a master program that will properly launch different missions as needed. There are several ways to do it, but this very much goes back to the python learning curve. You will have to learn the pybricks way of doing everything like movement and using sensors. You will also have to learn how to use pybricksdev.exe, which is how you use pybricks in VS Code. By the way, there is an easier way to use pybricks and still use the scratch-like programming interface, and that is to just use their web app (which is the default). I know teams that use that and it seems nice, but I don't personally have any experience with that. We wanted to be able to use VS Code and github, so their web app would not meet that goal.
* You will have to flash specialized firmware on your hubs. This is really easy for someone that has done this many times before, but I know there are people out there very uncomfortable with things like that. I suppose there is risk that you could permanently damage a hub, but I have never heard of anything like that happening. Anyway, if you do turn your brick into a ... BRICK, well, don't blame me! Seriously though, I think it is easy. Just follow the instructions.
* All of that being said, my middle school team wanted to make this switch, and had no problem picking up on all of this. Your mileage may vary.

But there are some very nice benefits to doing it this way.
* The number one reason we switched was because the team wanted to. They asked if we could use python and learn how to program with a "real" programming language using "real" development tools. That was several years ago, and that team is long gone, but as new kids came on the team, they learned everything above and noone has ever asked if we could go back. If your team doesn't want this, then don't do it.
* Pybricks does have some functionality that I don't think is possible in the regular spike software. For one, when driving it is possible to easily drive along a curve. What's more, it is possible to chain movements commands together without having to stop in between commands. This is very nice and very fast.
* Code sharing and backups is automatic with github. If we need to make a change to the master program or base_robot.py, we make the change, push to github, and when the team members do a pull, they will have the latest software. They can also use any team laptop. They all have the same code, so when we go to tournaments, it doesn't matter which laptop we take.
* Some people think the gyro implementation is better and more accurate in pybricks. That may be true, but I don't have much experience using the base firmware, so I don't have anything to compare it to. I'd love to see someone doing some real-life tests that show this to be a fact, but I don't know if that has been done.
* I do think the basic driving implementation is better in pybricks. I don't think the built-in Spike software handles acceleration/deceleration at all, but pybricks does quite well.
* The pybricks developers are very reachable and love to help teams. They are very active on the support pages ([here](https://github.com/orgs/pybricks/discussions) and [here](https://github.com/pybricks/support/issues)) and love seeing FLL teams use their software. Try getting that level of support from Lego if you have questions about your code using the Lego firmware. By the way, Lego has very much endorsed pybricks. There are links to pybricks in several places on the Lego website ([example](https://education.lego.com/en-us/lessons/ev3-real-world-vehicles/speed-control-system/)).

Convinced? Think you and your team are ready for this?

## What is needed
To get started, you'll need these things:
* A lego hub such as EV3 or Spike Prime. Our team uses Spike Primes, so this tutorial will be Spike Prime-focused. But I think the steps are pretty much the same for EV3s if you are using them.
* Laptop. I use Windows, but I think it will all work on a Mac. I cannot confirm. You will need admin access to the laptop because you will be installing software on it.
* Software and user accounts described below. Don't worry, everything is FREE.
* A coach with ownership rights for the team repository on GitHub. The coach will invite collaborators (team members) to be able to edit the files in the repository

## Steps
1. [Set Up Coach and team member accounts on GitHub](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/github-accounts.md)
2. Install software on a laptop (coaches and team members)
   - [VS Code](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/install-vs-code.md)
   - [Git (for Windows)](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/install-git.md)
   - [Python](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/install-python.md)
3. TODO [Create a GitHub repository for the season (coach)](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/github-season-repo.md)
4. TODO [Clone the repository (team member)](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/clone-push.md)
