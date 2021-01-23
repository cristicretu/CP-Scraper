[![DeepSource](https://deepsource.io/gh/cristicretu/CP-Scraper.svg/?label=resolved+issues)](https://deepsource.io/gh/cristicretu/CP-Scraper/?ref=repository-badge)[![DeepSource](https://deepsource.io/gh/cristicretu/CP-Scraper.svg/?label=active+issues)](https://deepsource.io/gh/cristicretu/CP-Scraper/?ref=repository-badge)![CodeQL](https://github.com/cristicretu/CP-Scraper/workflows/CodeQL/badge.svg)

*Feel free to **contribute** to this project!*

# CP-Scraper

Competitive Programming Scraper is a python script that automatically creates input and output files, specific folders and pre-completed snippets, ***instantly***.

Also, it can open *VSCode, Vim or Atom* with all the freshly made files.

Your favourite editor is not in this list? No problem. It can still create the files with all the snippets, all you have to do is to open the freshly created folder by this script.

Currently, it supports ***codeforces.com***, ***infoarena.ro*** and ***pbinfo.ro***!

## Why?

Because it's cool.

No wasting time making folders and files, getting snippets and inputs from the Online Judge. This script makes you forget about small stuff, and gets you going straight into programming - no time wasted, 3 seconds and you're set.

## How to use it?

Clone this *repo*,

```
git clone git@github.com:cristicretu/CP-Scraper.git
```

 or download the zip file, and change the **path.txt** with your desired path from your PC. (Optionally) you can change from the folder *snippets*:  *headers.cpp* - to use your own headers;  *file_snippets.cpp* - to use your main snippets for file input;  *console_snippets.cpp* -  to use your main snippets for console input.

## How to run it?

For Linux, and more specifically Debian-based distros, run from *setup/unix* the *install.sh* to install the required packages. (If permission is denied, use chmod +x install.sh, and the run it with ./install.sh)

Then navigate to this repo, and type:

```
python3 main.py
```

Now, it will run in the background, and every time you **copy** (*ctrl+c*) a link, it will automatically start.

------

The Windows version is 1 update behind the Unix one, so no running in the background (for now). To do the  setup, run the 2 scripts from *setup/windows* and follow the instructions there. After that, just open with *powershell* **run.ps1**.

------

*Ex: Codeforces*

<img src="https://cdn.discordapp.com/attachments/797485737272541250/800042557769908275/codeforces.gif" style="zoom:150%;" /><img src="https://cdn.discordapp.com/attachments/797485737272541250/800042578388975646/infoarenapbinfo.gif" />

*Ex: Infoarena & Pbinfo*

## Now

- I'm currently working on making the program run on startup, and after wake up from sleep. (Linux)

- Next thing on the list is updating the Windows version, and then doing the same thing, running on startup.

- Code cleanup, repo cleanup

  Great resource: 

  https://stackoverflow.com/questions/43284969/python-how-to-resume-excecution-of-python-script/43385347

