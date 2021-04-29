[![DeepSource](https://deepsource.io/gh/cristicretu/CP-Scraper.svg/?label=resolved+issues)](https://deepsource.io/gh/cristicretu/CP-Scraper/?ref=repository-badge)[![DeepSource](https://deepsource.io/gh/cristicretu/CP-Scraper.svg/?label=active+issues)](https://deepsource.io/gh/cristicretu/CP-Scraper/?ref=repository-badge)![CodeQL](https://github.com/cristicretu/CP-Scraper/workflows/CodeQL/badge.svg)

*Feel free to **contribute** to this project!*

# CP-Scraper

Competitive Programming Scraper is a python script that automatically creates input and output files, specific folders and pre-completed snippets, ***instantly***, for C++.

Also, it can open *VSCode, Vim or Atom* with all the freshly made files.

Your favourite editor is not in this list? No problem. It can still create the files with all the snippets, all you have to do is to open the freshly created folder by this script.

Currently, it supports ***codeforces.com***, ***infoarena.ro*** and ***pbinfo.ro***!

## Running

Clone this *repo*,*and change the **path.txt** with your desired path from your PC.

For MacOS and Linux make sure you have installed python and this project' s dependencies:

```
pip3 install pymsgbox bs4 requests pyperclip
```

Then execute using:
```
python3.9 main.py #for linux
python3.9 mac.py #for mac
```

Now, it will run in the background, and every time you **copy** a link from an supported Online Judge Site, it will automatically start.

------

*Ex: Codeforces*

<img src="https://cdn.discordapp.com/attachments/797485737272541250/800042557769908275/codeforces.gif" style="zoom:150%;" /><img src="https://cdn.discordapp.com/attachments/797485737272541250/800042578388975646/infoarenapbinfo.gif" />

*Ex: Infoarena & Pbinfo*

*Ex: Infoarena on Mac*
<img src="https://cdn.discordapp.com/attachments/797485737272541250/836523541125005319/mac.gif" />


## Now

- Add support for more sites
