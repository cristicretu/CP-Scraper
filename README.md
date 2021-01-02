[![DeepSource](https://deepsource.io/gh/cristicretu/CP-Scraper.svg/?label=resolved+issues)](https://deepsource.io/gh/cristicretu/CP-Scraper/?ref=repository-badge)[![DeepSource](https://deepsource.io/gh/cristicretu/CP-Scraper.svg/?label=active+issues)](https://deepsource.io/gh/cristicretu/CP-Scraper/?ref=repository-badge)![CodeQL](https://github.com/cristicretu/CP-Scraper/workflows/CodeQL/badge.svg)

# CP-Scraper

Competitive Programming Scraper is a python script that automatically creates input and output files, specific folders and pre-completed snippets, when given an online judge problem url.

Also, it can open *VSCODE, VIM OR ATOM* with all the freshly made files.

Currently, it supports ***codeforces.com***, ***infoarena.ro*** and ***pbinfo.ro***!

It works on unix systems and windows* (not the best), but it will fully support windows soon!

## How to use it?

Clone this *repo*,

```
git clone git@github.com:cristicretu/CP-Scraper.git
```

 or download the zip file, and change the **path.txt** with your desired path from your PC. (Optionally) you can change *headers.cpp*-to use your own headers; *file_snippets.cpp*-to use your main snippets for file input; and *console_snippets.cpp*- to use your main snippets for console input.

## How to run it?

For Windows, run the 2 scripts from *setup/windows* and follow the instructions there. After that, just open with *powershell* **run.ps1**.

For Linux, make sure you have Beautiful Soup and Requests installed. (if not, run these commands in your terminal)

```
pip3 install requests
pip3 install bs4
```

and then navigate to this repo, and type:

```
python3 main.py
```

Then, all you have to do is to paste the *full link* of your problem.

*Ex: Infoarena*

![](https://cdn.discordapp.com/attachments/427049682364268544/794227851753816084/ezgif.com-gif-maker.gif)![](https://cdn.discordapp.com/attachments/427049682364268544/794265081423724624/aaa.gif)

*Ex: Pbinfo; file-console input*