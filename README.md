[![DeepSource](https://deepsource.io/gh/cristicretu/CP-Scraper.svg/?label=resolved+issues)](https://deepsource.io/gh/cristicretu/CP-Scraper/?ref=repository-badge)[![DeepSource](https://deepsource.io/gh/cristicretu/CP-Scraper.svg/?label=active+issues)](https://deepsource.io/gh/cristicretu/CP-Scraper/?ref=repository-badge)![CodeQL](https://github.com/cristicretu/CP-Scraper/workflows/CodeQL/badge.svg)

*Feel free to **contribute** to this project!*

# CP-Scraper

Competitive Programming Scraper is a python script that automatically creates input and output files, specific folders and pre-completed snippets, ***instantly***, for C++.

Also, it can open *VSCode, Vim or Atom* with all the freshly made files.

Your favourite editor is not in this list? No problem. It can still create the files with all the snippets, all you have to do is to open the freshly created folder by this script.

Currently, it supports ***codeforces.com***, ***infoarena.ro*** and ***pbinfo.ro***!

## Why?

Because it's cool.

No wasting time making folders and files, getting snippets and inputs from the Online Judge. This script makes you forget about small stuff, and gets you going straight into programming - no time wasted, 1 second and you're set.

## How to use it?

Clone this *repo*,

```
git clone git@github.com:cristicretu/CP-Scraper.git
```

 or download the zip file, *and change the **path.txt** with your desired path from your PC.* (Optionally) you can change from the folder *snippets*:  *headers.cpp* - to use your own headers;  *file_snippets.cpp* - to use your main snippets for file input;  *console_snippets.cpp* -  to use your main snippets for console input.

For Linux, and specifically Debian-based distros, make sure you have installed python3 and the required dependencies :

```
sudo apt install python3
sudo apt install python3-tk
pip3 install pymsgbog
pip3 install bs4
pip3 install requests
pip3 install pyperclip
```

Then navigate to this repo, and type:

```
python3.8 main.py
```

Now, it will run in the background, and every time you **copy** (*ctrl+c*) a link from an supported Online Judge Site, it will automatically start.

------

*Ex: Codeforces*

<img src="https://cdn.discordapp.com/attachments/797485737272541250/800042557769908275/codeforces.gif" style="zoom:150%;" /><img src="https://cdn.discordapp.com/attachments/797485737272541250/800042578388975646/infoarenapbinfo.gif" />

*Ex: Infoarena & Pbinfo*

## Now

- Add support for more sites
- Figure out how to make it work on Windows

