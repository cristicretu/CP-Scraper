from bs4 import BeautifulSoup
from pathlib import Path
import requests
import os

# user agent
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

# get directory path
with open('path.txt', 'r') as f:
    directory_path = f.read()
    directory_path += '/'
directory_path = directory_path[:len(directory_path) - 2]
# -2 for linux
# -1 for windows...


class Scraper:
    def print(self):
        print(self.url)


def get_value(s):
    ans = s.get_text()
    return ans


def make_files(input_name, input_value, current_site, file, editor):
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
        if (current_site == '/cf/'):
            input_name = 'input.txt'
            output_name = 'output.txt'
        # get snippets
        snippets = ''
        rest = ''
        with open('file_snippets.cpp', 'r') as io:
            rest += io.read()
        with open('headers.cpp', 'r') as fr:
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
        with open('console_snippets.cpp', 'r') as op:
            rest += op.read()
        with open('headers.cpp', 'r') as fx:
            snippets += fx.read()

        snippets += rest
    # write in the snippets
    with open(os.path.join(path, mainfile_name), 'w') as fp:
        fp.write(snippets)

    # user choice
    print('Do you want to open the editor? [y/n]:')
    choice = input()
    if choice == 'y':
        os.chdir(path)
        editor = editor + ' .'
        if editor == 'vscode .':
            editor = editor[2:]
        os.system(editor)

    print('Done! Good luck.')


def infoarena(soup, current_site, editor):
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

    make_files(inputfile_name, inputfile_value, current_site, True, editor)


def pbinfo(soup, current_site, url, editor):
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
        make_files(inputfile_neim, inputfile_value, current_site, file, editor)
    else:
        make_files(url, inputfile_value, current_site, file, editor)


def replaceS(sinput, pattern, replaceWith):
    return sinput.replace(pattern, replaceWith)


def codeforces(soup, current_site, url, editor):
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

    if (get_file.split(' ')[0] == 'standard'):
        make_files(problem_name, '', current_site, False, editor)
    else:
        # get the input
        get_info = soup.find_all('pre')
        inputfile_value = get_info[0]
        for br in inputfile_value.find_all("br"):
            br.replace_with("\n")
        inputfile_value = inputfile_value.get_text()

        make_files(problem_name, inputfile_value, current_site, True, editor)


if __name__ == "__main__":
    clasa = Scraper()
    print('What URL does your problem have?')
    clasa.url = str(input())

    # check for supported site
    while True:
        if clasa.url[12:21] == 'infoarena' or clasa.url[12:18] == 'pbinfo' or clasa.url[8:18] == 'codeforces':
            break
        if clasa.url[12:21] != 'infoarena' or clasa.url[12:18] != 'pbinfo' or clasa.url[8:18] != 'codeforces':
            print('Site not supported, try again:')
            clasa.url = str(input())

    # check for problem in-site 25 - > 33
    current_site = ''
    if clasa.url[12:21] == 'infoarena':
        current_site = 'infoarena'
    elif clasa.url[12:18] == 'pbinfo':
        current_site = 'pbinfo'
    elif clasa.url[8:18] == 'codeforces':
        current_site = 'codeforces'

    while True:
        if (current_site == 'infoarena' and clasa.url[25:33] == 'problema') or (current_site == 'pbinfo' and clasa.url[22:30] == 'probleme') or (current_site == 'codeforces' and (clasa.url[34:41] == 'problem' or clasa.url[35:42] == 'problem' or clasa.url[36:43] == 'problem')):
            break

        if (current_site == 'infoarena' and clasa.url[25:33] != 'problema') or (current_site == 'pbinfo' and clasa.url[22:30] != 'probleme') or (current_site == 'codeforces' and (clasa.url[34:41] != 'problem' or clasa.url[35:42] != 'problem' or clasa.url[36:43] != 'problem')):
            print('Not a valid problem, try again:')
            clasa.url = str(input())

    editor = ''
    with open('editor.txt', 'r') as op:
        editor = op.read()
    if len(editor) < 3:
        print('What is your preffered editor? [vim,vscode,atom]')
        text = str(input())
        while True:
            if text in 'vim' or text in 'vscode' or text in 'atom':
                break
            else:
                print('Not a valid editor, try again:')
                text = str(input())

        with open('editor.txt', 'w') as ww:
            ww.write(text)
    with open('editor.txt', 'r') as op:
        editor = op.read()

    # get info
    # get requests
    url = requests.get(clasa.url, headers=headers)

    # parse the html
    soup = BeautifulSoup(url.content, 'html.parser')

    # uatafac is that switch case python bro
    if (current_site == 'infoarena'):
        infoarena(soup, current_site, editor)
    elif (current_site == 'pbinfo'):
        pbinfo(soup, current_site, clasa.url, editor)
    elif (current_site == 'codeforces'):
        codeforces(soup, 'cf', clasa.url, editor)
