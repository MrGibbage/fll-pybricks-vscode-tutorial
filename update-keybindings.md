# Keyboard Shortcuts (or Keybindings)

## Explained

Keyboard shortcuts, or keybindings, make life a lot easier in VS Code. You probably already know some of the more famous ones like ctrl-c, ctrl-x, and ctrl-v for copy, cut, and paste, and maybe even ctrl-s for save, but in VS Code, there are many, MANY more keyboard shortcuts. And of course, they are all configurable. What we would like to do is set up our laptops such that the team members can quickly run their code on their robots. I have chosen a combination of keybindings centered around ctrl-L ("L" for "Launch")

- Ctrl-l: (Task) Run on my robot (runs the currently open program on my robot)
- Ctrl-alt-l: (Task) Run on alt robot (runs the currently open program on an alternative selected robot)
- Ctrl-shift-l: (Task) Run master program on my robot (runs the master program on my robot)
- Ctrl-shift-alt-l: (Task) Run master program on alt robot (runs the master program on an alternative selected robot)

I also like these keybindings because while they were already in use by VS Code, they were for things I never used, and I never expected the team members to need. So you may want to consider that before using our keybindings.

Ctrl-l was for chat; Ctrl-alt-l was not in use; Ctrl-shift-l was for some advanced searching features; Ctrl-shift-alt-l was also for chat

There are some other things these keybindings did, and if you want to review them, just open the VS Code palette with ctrl-shift-p, type "keyboard", and choose "Preferences: Open Keyboard Shortcuts".

## Updating keybindings

Keybindings are not saved in .vscode like many of the other settings that we are updating here. Instead, I have created a VS Code extension. If you choose to use that extension, as explained [here](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-extensions.md), then you won't be able to change them. For example, ctrl-l runs the task named "Run on my robot". If you don't want to use my extension, you could configure the keybindings manually on each laptop. For example, if you want to use a different keybinding than the ctrl-l group I am using, you will have to do it manually. Additionally, if you decided you wanted to change that task name to "Run on the robot", my keybindings extension won't work for you.

[This is the repo for my extension](https://github.com/MrGibbage/vs-code-keybindings-for-pybricks). You don't need to do anything with that repo, but if you want to look over the code, there it is.

If you want to do this manually for your laptops, there are a lot of tutorials online, but basically type ctrl-shift-p to open the command palette, type keyboard and choose "Preferences: Open Keyboard Shortcuts (JSON)". Make sure it says "(JSON)" at the end. There you can make the changes, and save the file. Place a copy of it somewhere online so you can copy and paste it in on each laptop.

[Next: How to update Settings](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-settings.md)
