# Snippets

## Explained
Snippets are an awesome way to save a lot of typing and preventing typos. For example, we have an instance method in our BaseRobot class called "driveForDistance" and there are several parameters that can be used. A line of code running that method might look like this:

`br.driveForDistance(100)`

Because we use this method so much, we all know the 100 in the example is the distance in millimeters, but admittedly this isn't very clear way of calling this method. And there are still other options that can be entered. Here's another example, but better written, line of code:

`br.driveForDistance(speedPct=20, distance=40, then=Stop.NONE, wait=true)`

All of those parameters are important, but there are a lot of opportunities for typos. So is there anything that can be done to save some typing? VS Code snippets are the solution. Snippets allow us to program a prefix character sequence, and whenever that is typed, VS Code will use intellisense to popup an option to use the snippet. If the user chooses the snippet, it will replace the prefix sequence with some assigned text, and it will place the cursor where it needs to be, and even enable the user to just press tab to get to the next needed cursor place. Snippets are saved in the VS Code Profile, so they are NOT saved in the .vscode folder. That means the update process is a little more manual, but it isn't too difficult. But first I will explain the snippet in a little more detail.

For example, we have the following snippet programmed
```json
"Drive Straight Distance": {
    "prefix": ["dfd"],
    "body": ["br.driveForDistance(distance=${1}, speedPct=${2:80}, then=${3:Stop.BRAKE}, wait=${4:True})"],
    "description": "Drive the robot straight for a given distance"
},
```

So in this case, if the user types "dfd" (without the quotes), VS Code will popup an option use the snippet. If the user chooses the snippet, it will replace the "dfd" with `br.driveForDistance(distance=|, speedPct=80, then=Stop.BRAKE, wait=true)` and the cursor will be placed right after the equals sign following `distance=`. That way all they have to type is the distance value, say "100". Then if they hit the tab key, the cursor will move to the number 80 following `speedPct=` (80 is our default speed). That way they could easily update the speed parameter as well. Same for the `then=` parameter and the `wait=` parameter.

Here's what it looks like after typing dfd

![image](https://github.com/user-attachments/assets/55af02a1-11f8-450b-be01-6820326bedc0)

And here is what it looks like after selecting the snippet

![image](https://github.com/user-attachments/assets/efb3a12b-4991-464d-b34e-4020881ddb47)

The cursor is right where the red squiggle underline is (VS code is complaining that there is an error because nothing has been entered yet).

## Getting started with Snippets for FLL Teams
If you have method names that are the same as ours, you could just use our snippets configuration file. But this might be a good example of a place where it might be better for you to just create your own snippets. Or maybe not use snippets at all, which is perfectly OK.

## Updating snippets
Snippets are saved in the .vscode folder so it is updated when a team member pulls from GitHub.

[Next: How to update Keybindings](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-keybindings.md)
