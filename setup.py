from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'cpsc',
    version = '0.0.1',
    author = 'Cristian Crețu',
    author_email = 'crisemcr@gmail.com',
    license = 'MIT',
    description = 'Competitive Programming Input Parser',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/cristicretu/CP-Scraper',
    # py_modules = ['my_tool', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        cooltool=my_tool:main
    '''
)