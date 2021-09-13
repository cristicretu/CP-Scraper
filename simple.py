from bs4 import BeautifulSoup
from pathlib import Path
import requests
import os

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

# get directory path
with open('.setup/settings/path.txt', 'r') as f:
    directory_path = f.read()
    # if directory_path:
        # directory_path += '/'
        # directory_path = Path(directory_path[:len(directory_path) - 1])


def get_value(s):
    ans = s.get_text()
    return ans


def make_files(input_name, input_value, current_site, file):
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
    print(path)
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
            snippets += '\nstd::fstream fin("' + \
                input_name + '", std::ios::in);'
            snippets += '\nstd::fstream fout("' + \
                output_name + '", std::ios::out);'

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
    os.chdir(now_path)
    # done


def infoarena(soup, current_site):
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

    make_files(inputfile_name, inputfile_value, current_site, True)


def pbinfo(soup, current_site, url):
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
        make_files(inputfile_neim, inputfile_value, current_site, file)
    else:
        make_files(url, inputfile_value, current_site, file)


def replaceS(sinput, pattern, replaceWith):
    return sinput.replace(pattern, replaceWith)


def codeforces(soup, current_site, url):
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
        make_files(problem_name, '', current_site, False)
    else:
        # get the input
        get_info = soup.find_all('pre')
        inputfile_value = get_info[0]
        for br in inputfile_value.find_all("br"):
            br.replace_with("\n")
        inputfile_value = inputfile_value.get_text()

        make_files(problem_name, inputfile_value, current_site, True)


url = input()

nurl = requests.get(url, headers=headers);
soup = BeautifulSoup(nurl.content, 'html.parser')

if directory_path == '':
        with open('.setup/settings/path.txt', 'w') as f:
            directory_path = input("Where do you want to save the files? [navigate there and copy the output of 'pwd' command and paste it here: ")
            f.write(directory_path)

if 'infoarena' in url:
  infoarena(soup, 'infoarena')
elif 'pbinfo' in url:
  pbinfo(soup, 'pbinfo', url)
elif 'codefores' in url:
  codeforces(soup, 'cf', url)