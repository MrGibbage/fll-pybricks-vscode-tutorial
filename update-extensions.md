Extensions are one of the things that makes VS Code so versatile and, well, just great! Extensions in VS Code are a lot like extensions for a lot of other programs, such as your web browser. People write extensions and sometimes (OK, a LOT of times) make them available to the public. Most of the time for free. All of the extensions that I am recommending are free, and provide some functionality to make the programming experience easier or at least better.

You can make a list of extensions and save them in the .vscode folder, named extensions.json. When a team member performs the first repo pull to their laptop, it will ask if they want to install the recommended extensions, in which case all they have to do is click "Yes". So while it doesn't automatically install the extensions for them without any intervention, it is pretty simple. THen, if you decide that you want to make a change to the extensions.json file, when they next pull the repo, VS Code will ask them if they want to install the newly recommended extensions.

This is the current extensions.json file:

```json
{
	// See https://go.microsoft.com/fwlink/?LinkId=827846 to learn about workspace recommendations.
	// Extension identifier format: ${publisher}.${name}. Example: vscode.csharp

	// List of extensions which should be recommended for users of this workspace.
	"recommendations": [
		"ms-python.black-formatter",
		"shyykoserhiy.git-autoconfig",
		"GitHub.vscode-pull-request-github",
		"ms-python.vscode-pylance",
		"ms-python.python",
		"ms-python.debugpy",
		"SkipMorrow.vs-code-keybindings-for-pybricks"
	],
	// List of extensions recommended by VS Code that should not be recommended for users of this workspace.
	"unwantedRecommendations": [
		
	]
}
```

"ms-python.black-formatter": Formats python code using industry standards
"shyykoserhiy.git-autoconfig": manages git configurations
"GitHub.vscode-pull-request-github": needed for github
"ms-python.vscode-pylance": needed for python
"ms-python.python": needed for python
"ms-python.debugpy": needed for python
"SkipMorrow.vs-code-keybindings-for-pybricks": extension that I wrote with some specific keybindings. See [update keybindings](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-keybindings.md) for more info.

[Next: How to update Tasks](https://github.com/MrGibbage/fll-pybricks-vscode-tutorial/blob/main/update-tasks.md)