from setuptools import setup

setup(name='phigaro',
      description='Phigaro is a scalable command-line tool for predictions phages and prophages '
                  'from nucleid acid sequences (including metagenomes) and '
                  'is based on phage genes HMMs and a smoothing window algorithm.',
      version="0.2.1.8",
      license='MIT',
      author='E.Starikova, N.Pryanichnikov, P.Tikhonova',
      author_email='hed.robin@gmail.com',
      url='https://github.com/bobeobibo/phigaro',
      packages=['phigaro',
                'phigaro.finder',
                'phigaro.cli',
                'phigaro.batch',
                'phigaro.batch.task',
                'phigaro.misc',
		'phigaro.to_html',
                ],
      package_data = {
        '': ['*.pickle', 'Readme.md']
      },
      entry_points={
          'console_scripts': [
              'phigaro = phigaro.cli.batch:main',
              'phigaro-setup = phigaro.cli.helper:main',
          ]
      }, install_requires=['numpy', 'six>=1.7.0', 'pandas>=0.23.4','sh', 'singleton', 'PyYAML', 'future', 'argparse', 'numpy', 'plotly', 'bs4', 'beautifulsoup4>=4.4.0', 'lxml','biopython']
)
