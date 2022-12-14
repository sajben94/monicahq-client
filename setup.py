from setuptools import setup, find_packages


setup(
    name='monicahq-client',
    version='0.0.1',
    license='MIT',
    author="Darko Sajben",
    author_email='sajbendarko94@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/sajbend/monicahq-client',
    keywords='monicahq',
    install_requires=[
          'requests',
          'json',
      ],

)
