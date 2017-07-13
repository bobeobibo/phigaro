from setuptools import setup

setup(name='phigaro',
      version='0.0.1',
      packages=['phigaro'],
      entry_points={
          'console_scripts': [
              'phigaro = phigaro.cli:main'
          ]
      },
)