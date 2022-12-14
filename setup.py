from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='monicahq-client',
    version='0.1.2',
    license='MIT',
    author="Darko Sajben",
    author_email='sajbendarko94@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/sajben94/monicahq-client',
    keywords='monicahq',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
          'requests',
      ],
)
