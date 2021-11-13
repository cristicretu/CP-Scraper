from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
  name='cpscli',
  version='0.0.1',
  author = 'Cristian Crețu',
  author_email = 'crisemcr@gmail.com',
  license = 'MIT',
  description = 'Competitive Programming Input Parser',
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = 'https://github.com/cristicretu/CP-Scraper',
  packages=find_packages(),
  install_requires=[requirements],
  python_requires='>=3.7',
  entry_points='''
      [console_scripts]
      cpsc=cpscli:cpscli
  '''
)