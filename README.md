# CP-Scraper
Competitive Programming Scraper is a python script that automatically creates input and output files, specific folders and pre-completed snippets, when given an online judge url.

Also, it can open *vscode* with all the freshly made files.

Currently, it supports ***codeforces.com***, ***infoarena.ro*** and ***pbinfo.ro***!

## How to use it?

Clone this *repo*,

```
git clone git@github.com:cristicretu/CP-Scraper.git
```

 and change the **path.txt** with your desired path from your PC. (Optionally) change the *snippets.cpp* with your own snippets. (they will be placed before the file input).

## How to run it?

You also need Beautiful Soup and Requests, so make sure you have them installed: (if not, run these commands in your terminal)

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