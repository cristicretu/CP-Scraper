from bs4 import BeautifulSoup
from pathlib import Path
from pymsgbox import *
import pyperclip
import requests
import time
import os

# user agent
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

# get directory path
with open('path.txt', 'r') as f:
    directory_path = f.read()
    directory_path += '/'

directory_path = Path(directory_path[:len(directory_path) - 2])


def get_value(s):
    ans = s.get_text()
    return ans


def make_files(input_name, input_value, current_site, file, editor, option):
    directory_name = input_name[:len(input_name) - 3]
    mainfile_name = directory_name + '.cpp'

    # now make the directory

    # this is the old version for linux
    # current_site = '/' + current_site + '/'
    # temp_path = directory_path + current_site
    # path = os.path.join(temp_path, directory_name)
    # os.mkdir(path)

    # pathlib
    dir_path = Path(directory_path)
    current_site = Path(current_site)

    temp_path = dir_path / current_site
    path = temp_path / directory_name
    os.makedirs(path)

    # write in the files
    if file is True:
        output_name = directory_name + '.out'
        if current_site == '/cf/':
            input_name = 'input.txt'
            output_name = 'output.txt'
        # get snippets
        snippets = ''
        rest = ''
        with open('snippets/file_snippets.cpp', 'r') as io:
            rest += io.read()
        with open('snippets/headers.cpp', 'r') as fr:
            snippets += fr.read()
            snippets += '\nstd::ifstream fin("' + input_name + '");'
            snippets += '\nstd::ofstream fout("' + output_name + '");'

        snippets += rest
        # now create the files
        with open(os.path.join(path, input_name), 'w') as fp:
            fp.write(input_value)
        with open(os.path.join(path, output_name), 'w') as fp:
            pass
    elif file is False:
        snippets = ''
        rest = ''
        with open('snippets/console_snippets.cpp', 'r') as opes:
            rest += opes.read()
        with open('snippets/headers.cpp', 'r') as fx:
            snippets += fx.read()

        snippets += rest
    # write in the snippets
    with open(os.path.join(path, mainfile_name), 'w') as fp:
        fp.write(snippets)

    now_path = Path().absolute()

    print(now_path)
    if option == 'Yes and open the editor':
        os.chdir(path)
        if editor == 'VSCode':
            editor = 'code .'
        elif editor == 'Atom':
            editor = 'atom .'
        elif editor == 'Vim':
            editor = 'vim *'
        os.system(editor)

    os.chdir(now_path)
    # done


def infoarena(soup, current_site, editor, option):
    get_info = soup.find(class_="example")
    get_input = get_info.get_text()

    # get input name
    inputfile_name = get_input[:get_input.index('.')] + '.in'

    get_info = get_info.find_all('td')
    # this will make get_info a list,
    # even index -> input
    # odd index -> output
    # get_info[0], get_info[1] = first pairs of input and output

    # get the input, separately
    inputfile_value = get_value(get_info[0])
    # outputfile_value = get_value(get_info[1]) no need for this

    make_files(inputfile_name, inputfile_value,
               current_site, True, editor, option)


def pbinfo(soup, current_site, url, editor, option):
    get_info = soup.find_all('pre')
    # get input value
    inputfile_value = get_value(get_info[0])

    url = url[31:]
    url = url[url.index('/') + 1:] + '.in'

    names = soup.find_all('code')
    inputfile_neim = ''
    for i in names:
        text = i.get_text()
        if '.in' in text:
            inputfile_neim = text
            break

    file = False
    if inputfile_neim:
        file = True

    if file is True:
        make_files(inputfile_neim, inputfile_value,
                   current_site, file, editor, option)
    else:
        make_files(url, inputfile_value, current_site, file, editor, option)


def replaceS(sinput, pattern, replaceWith):
    return sinput.replace(pattern, replaceWith)


def codeforces(soup, current_site, url, editor, option):
    get_file = soup.find_all(class_='input-file')
    get_file = get_file[0].get_text()[5:]
    get_file.split(' ')

    # get problem name and number
    url = url[::-1]
    letter = url[0]
    url = replaceS(url, '/', ' ')
    number = str([int(s) for s in url.split() if s.isdigit()])
    number = number[::-1]
    number = number[1:len(number) - 1]

    problem_name = number + '_' + letter + '.in'

    if get_file.split(' ')[0] == 'standard':
        make_files(problem_name, '', current_site, False, editor, option)
    else:
        # get the input
        get_info = soup.find_all('pre')
        inputfile_value = get_info[0]
        for br in inputfile_value.find_all("br"):
            br.replace_with("\n")
        inputfile_value = inputfile_value.get_text()

        make_files(problem_name, inputfile_value,
                   current_site, True, editor, option)


while True:  # reset the program

    recent_value = ""
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            print("Value changed: %s" % str(recent_value))

        if ('infoarena' in recent_value and 'problema' in recent_value) \
                or ('pbinfo' in recent_value and 'probleme' in recent_value) \
                or ('codeforces' in recent_value and 'problem' in recent_value):
            break
        time.sleep(0.1)

    option = confirm(text='Do you want to open CP-Scraper?',
                     title='CP-Scraper', buttons=['Yes', 'Yes and open the editor', 'No'])

    if option in 'Yes' or option in 'Yes and open the editor':
        with open('setup/settings/editor.txt', 'r') as op:
            editor = op.read()
        if len(editor) < 3:
            optiune = confirm(text='What is your preffered editor?',
                              title='CP-Scraper', buttons=['VSCode', 'Atom', 'Vim'])
            with open('setup/settings/editor.txt', 'w') as ww:
                ww.write(optiune)
            editor = optiune

        # get info
        # get requests
        url = requests.get(recent_value, headers=headers)

        # parse the html
        soup = BeautifulSoup(url.content, 'html.parser')

        if 'infoarena' in recent_value:
            infoarena(soup, 'infoarena', editor, option)
        elif 'pbinfo' in recent_value:
            pbinfo(soup, 'pbinfo', recent_value, editor, option)
        elif 'codeforces' in recent_value:
            codeforces(soup, 'cf', recent_value, editor, option)

    pyperclip.copy('Hello, World! Looks like you found an easter egg')
