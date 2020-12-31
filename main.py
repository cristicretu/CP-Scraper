from bs4 import BeautifulSoup
import requests
import os

# user agent
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

# get directory path
with open('path.txt', 'r') as f:
    directory_path = f.read()
directory_path = directory_path[:len(directory_path) - 1]


class Scraper:
    def print(self):
        print(self.url)


def get_value(s):
    ans = s.get_text()
    return ans


def make_files(input_name, input_value):
    directory_name = input_name[:len(input_name) - 3]
    output_name = directory_name + '.out'
    mainfile_name = directory_name + '.cpp'

    # get snippets
    snippets = ''
    with open('snippets.cpp', 'r') as f:
        snippets += f.read()
        snippets += '\nstd::ifstream fin("' + input_name + '");'
        snippets += '\nstd::ofstream fout("' + output_name + '");'
        snippets += '\n\nint main() {\n\n  return 0;\n}'

    # now make the directory
    path = os.path.join(directory_path, directory_name)
    os.mkdir(path)

    # now create the files
    with open(os.path.join(path, input_name), 'w') as fp:
        fp.write(input_value)
    with open(os.path.join(path, output_name), 'w') as fp:
        pass
    with open(os.path.join(path, mainfile_name), 'w') as fp:
        fp.write(snippets)

    os.chdir(path)
    os.system('code .')
    print('Done! Good luck.')


def infoarena(soup):
    get_info = soup.find(class_="example")
    get_input = get_info.get_text()

    # get input name
    inputfile_name = get_input[:get_input.index('.')] + '.in'
    outputfile_name = inputfile_name[:len(inputfile_name) - 3] + '.out'

    # get problem name for directory
    directory_name = inputfile_name[:len(inputfile_name) - 3]

    get_info = get_info.find_all('td')
    # this will make get_info a list,
    # even index -> input
    # odd index -> output
    # get_info[0], get_info[1] = first pairs of input and output

    # get the input, separately
    inputfile_value = get_value(get_info[0])
    # outputfile_value = get_value(get_info[1]) no need for this

    make_files(inputfile_name, inputfile_value)


def pbinfo(soup):
    return 0


if __name__ == "__main__":
    clasa = Scraper()
    print('What URL does your problem have?')
    clasa.url = str(input())

    # check for supported site
    while True:
        if clasa.url[12:21] == 'infoarena' or clasa.url[12:18] == 'pbinfo':
            break
        elif clasa.url[12:21] != 'infoarena' or clasa.url[12:18] != 'pbinfo':
            print('Site not supported, try again:')
            clasa.url = str(input())

    # check for problem in-site 25 - > 33
    current_site = ''
    if clasa.url[12:21] == 'infoarena':
        current_site = 'infoarena'
    elif clasa.url[12:18] == 'pbinfo':
        current_site = 'pbinfo'
    while True:
        if (current_site == 'infoarena' and clasa.url[25:33] == 'problema') or (current_site == 'pbinfo' and clasa.url[22:30] == 'probleme'):
            break
        elif (current_site == 'infoarena' and clasa.url[25:33] != 'problema') or (current_site == 'pbinfo' and clasa.url[22:30] != 'probleme'):
            print('Not a valid problem, try again:')
            clasa.url = str(input())

    # get info
    # get requests
    url = requests.get(clasa.url, headers=headers)

    # parse the html
    soup = BeautifulSoup(url.content, 'html.parser')

    # uatafac is that switch case python bro
    if (current_site == 'infoarena'):
        infoarena(soup)
    elif (current_site == 'pbinfo'):
        pbinfo(soup)
    # elif (current_site == 'codeforces')
    #     tobecontinued
