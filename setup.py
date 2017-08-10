from setuptools import setup

setup(name='phigaro',
      version='0.0.1',
      packages=['phigaro', 'phigaro.finder'],
      entry_points={
          'console_scripts': [
              'phigaro = phigaro.cli:main'
          ]
      }, install_requires=['plotly', 'numpy', 'six']
      )