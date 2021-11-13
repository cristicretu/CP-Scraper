from setuptools import setup, find_packages

setup(
  name='cpscli',
  version='0.0.1',
  author = 'Cristian Crețu',
    author_email = 'crisemcr@gmail.com',
    license = 'MIT',
    description = 'Competitive Programming Input Parser',
  packages=find_packages(),
  install_requires=[
    'click'
  ],
  entry_points='''
      [console_scripts]
      cpsc=cpscli:cpscli
  '''
)