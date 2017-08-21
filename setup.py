from setuptools import setup

setup(name='phigaro',
      description='Phigaro is a scalable command-line tool for predictions phages and prophages '
                  'from nucleid acid sequences (including metagenomes) and '
                  'is based on phage genes HMMs and a smoothing window algorithm.',
      version='0.1.3',
      # author='Greg Ward',
      # author_email='gward@python.net',
      # url='https://www.python.org/sigs/distutils-sig/',
      packages=['phigaro',
                'phigaro.finder',
                'phigaro.cli',
                'phigaro.scheduling',
                'phigaro.scheduling.task',
                'phigaro.misc',
                ],
      entry_points={
          'console_scripts': [
              'phigaro = phigaro.cli.batch:main',
              'phigaro-setup = phigaro.cli.helper:main',
          ]
      }, install_requires=['numpy', 'six', 'sh', 'singleton', 'PyYAML', 'future']
)