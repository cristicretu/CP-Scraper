import click
from bs4 import BeautifulSoup
from pathlib import Path
import requests
import os

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

saved_location = ''

settings_path = os.path.join(os.getenv('HOME'), '.cpsc')
if not os.path.exists(settings_path):
    os.mkdir(settings_path)
save_path = os.path.join(settings_path, 'save_location.txt')
standard_snippets_path = os.path.join(settings_path, 'standard_snippets.cpp')
file_snippets_path = os.path.join(settings_path, 'file_snippets.cpp')

standard_snippets = ''
file_snippets = ''

try:
    with open(standard_snippets_path, 'r') as f:
        if f is not None:
          standard_snippets = f.read()
        else:
          standard_snippets = '#include <iostream>\n\nusing namespace std;\n\nint main(void) {\n  cout << "Hello, World!";\n  return 0;\n}'
except:
    standard_snippets = '#include <iostream>\n\nusing namespace std;\n\nint main(void) {\n  cout << "Hello, World!";\n  return 0;\n}'

try:
    with open(file_snippets_path, 'r') as f:
        if f is not None:
          file_snippets = f.read()
        else:
          file_snippets = '#include <fstream>\n\nusing namespace std;\n\nifstream fin("");\nofstream fout("");\n\nint main(void) {\n  fout << "Hello, World!";\n  return 0;\n}'
except:
    file_snippets = '#include <fstream>\n\nusing namespace std;\n\nifstream fin("");\nofstream fout("");\n\nint main(void) {\n  fout << "Hello, World!";\n  return 0;\n}'


def get_value(s):
    return s.get_text()

def replaceS(sinput, pattern, replaceWith):
    return sinput.replace(pattern, replaceWith)

def make_files(input_name, input_value, current_site, file):
    directory_name = input_name[:len(input_name) - 3]
    mainfile_name = directory_name + '.cpp'

    dir_path = Path(saved_location)
    current_site = Path(current_site)

    temp_path = dir_path / current_site
    path = temp_path / directory_name
    os.makedirs(path)

    # write in the files
    if file is True:
        if current_site == '/cf/':
            input_name = 'input.txt'
            output_name = 'output.txt'
        else:
            output_name = directory_name + '.out'


        before = ''
        after = ''
        total = ''

        before = file_snippets[:file_snippets.find("fin")] + f'fin("{input_name}");\n' 
        after = f'ofstream fout("{output_name}");\n' + file_snippets[file_snippets.find('fout("");') + 10:]
        total = before + after

        # now create the files
        with open(os.path.join(path, input_name), 'w') as fp:
            fp.write(input_value)
        with open(os.path.join(path, output_name), 'w') as fp:
            # just create the empty file
            pass
        with open(os.path.join(path, mainfile_name), 'w') as fp:
            fp.write(total)
    elif file is False:
        with open(os.path.join(path, mainfile_name), 'w') as fp:
            fp.write(standard_snippets)

    # now_path = Path().absolute()
    # os.chdir(now_path)

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

    make_files(inputfile_name, inputfile_value, current_site, True)

def pbinfo(soup, current_site, url):
    get_info = soup.find_all('pre')
    # get input value
    inputfile_value = get_value(get_info[0])

    # grab the problem name
    url = url[31:]
    url = url[url.index('/') + 1:] + '.in'

    # search by id 'code' to find the input
    # then parse it
    names = soup.find_all('code')
    inputfile_neim = ''
    for i in names:
        text = i.get_text()
        if '.in' in text:
            inputfile_neim = text
            break

    # check for file input
    file = False
    if inputfile_neim:
        file = True

    # create files
    # following standard or file input
    if file is True:
        make_files(inputfile_neim, inputfile_value, current_site, file)
    else:
        make_files(url, inputfile_value, current_site, file)

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


@click.command()
@click.option('--url', '-u', help="Problem URL.")
@click.option('--location', '-l', 
              type=click.Path(exists=True),
              help='Directory to get files saved.')
def cpscli(url, location):
    '''
            Script to parse challenges from  online judges.
            Creates files with the parsed inputs,
            prepares the main files with user-specified
            snippets.
    '''
    if location is not None:
      with open(save_path, 'w') as f:
          f.write(location)
      click.echo("Location saved. Now use 'cpsc -u <link> to use the script.")
      quit()
    else:
      try:
        with open(save_path, 'r') as f:
          if f == None:
            click.echo("Please use 'cpsc -l <Save location> to set a specific directory.'")
            quit()
          else:
            save_location = f.read()
      except:
        click.echo("Please use 'cpsc -l <Save location> to set a specific directory.'")
        quit()
    
    request_url = requests.get(url, headers=headers);
    soup = BeautifulSoup(request_url.content, 'html.parser')

    if 'infoarena' in url:
      infoarena(soup, 'infoarena')
    elif 'pbinfo' in url:
      pbinfo(soup, 'pbinfo', url)
    elif 'codefores' in url:
      codeforces(soup, 'cf', url)