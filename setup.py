from setuptools import setup

setup(name='phigaro',
      version='0.1.0',
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
              'phigaro-help = phigaro.cli.helper:main',
          ]
      }, install_requires=['numpy', 'six', 'sh', 'singleton', 'PyYAML']
)