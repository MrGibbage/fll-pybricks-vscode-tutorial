# Snippets

## Explained
Snippets are an awesome way to save a lot of typing and preventing typos. For example, we have a program in our BaseRobot class called "driveForDistance" and there are several parameters that can be used. A line of code might look like this:

`br.driveForDistance(100)`

Because we use this function so much, we all know the 100 is the distance in millimeters, but admittedly this isn't very clear. And there are still other options that can be entered. Here's another possible line of code:

`br.driveForDistance(speedPct=20, distance=40, then=Stop.NONE, wait=true)`

All of those parameters are important, and there are a lot of opportunities for typos. So is there anything that can be done to save some typing? VS Code snippets are the solution. Snippets allow us to program a prefix character sequence, and whenever that is typed, VS Code will use intellisense to popup an option to use the snippet. If the user chooses the nippet, it will replace the prefix sequence with some assigned text, and it will place the cursor where it needs to be, and even enable the user to just press tab to get to the next needed curson place. Snippets are saved in the VS Code Profile, so they are NOT saved in the .vscode folder. That means the update process is a little more manual, but it isn't too difficult. But first I will explain the snippet in a little more detail.

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


## Updating snippets
Snippets are not saved in the .vscode folder. Instead, they are saved in the profile. We keep a copy of the profile saved in the repo, so it is available on each laptop, but just having the profile saved is not enough to activate that profile. You can view and update profiles by clicking on the gear icon in the lower left of the VS Code screen. From there you can click on "Profile" and then "Profiles" (your exact wording may be different depending on if you have an active profile or not).

![image](https://github.com/user-attachments/assets/dd6cddad-96fe-4be5-b3c7-f4658f9d0d83)

From there, click on New Profile, and then Import profile

![image](https://github.com/user-attachments/assets/b02dca6b-7363-4ee8-b2a5-07c508779fbb)

Since we have the profile saved in the repo, it is just a matter of browsing to that profile file.

You then have the option of selecting what parts of the profile you want to use.

![image](https://github.com/user-attachments/assets/f80c69ae-0edc-4a12-8de4-7432a8302e12)

We are doing this primarily for the snippets, so be sure to select that option. You can also choose to enable the extensions here, and they will be automatically installed, which is nice. But I usually manage the extensions through the extensions.json file, as explained [here](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-extensions.md).

I do have a copy of our profile in the basic repository. It being in the repo doesn't do anything to your laptop settings. You have to manually import it using the steps above before they will take place. Or you can just edit your own snippets, add them to a profile then share that with the team members.

[Next: How to update Keybindings](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-keybindings.md)
