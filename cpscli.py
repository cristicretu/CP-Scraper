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
      save_location = location
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
    click.echo(save_location)
    