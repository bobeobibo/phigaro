from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='phigaro',
      description='Phigaro is a scalable command-line tool for predictions phages and prophages '
                  'from nucleid acid sequences (including metagenomes) and '
                  'is based on phage genes HMMs and a smoothing window algorithm.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      version=open("phigaro/_version.py").readlines()[-1].split()[-1].strip("\"'"),
      author='E.Starikova, N.Pryanichnikov, P.Tikhonova',
      author_email='hed.robin@gmail.com',
      url='https://github.com/lpenguin/phigaro',
      packages=['phigaro',
                'phigaro.finder',
                'phigaro.cli',
                'phigaro.batch',
                'phigaro.batch.task',
                'phigaro.misc',
		'phigaro.to_html',
                ],
      package_data = {
        '': ['*.pickle', 'README.md']
      },
      entry_points={
          'console_scripts': [
              'phigaro = phigaro.cli.batch:main',
              'phigaro-setup = phigaro.cli.helper:main',
          ]
      }, install_requires=['numpy', 'six>=1.7.0', 'pandas>=0.23.4','sh', 'singleton', 'PyYAML', 'future', 'argparse', 'numpy', 'plotly', 'bs4', 'beautifulsoup4>=4.4.0', 'lxml','biopython']
)
