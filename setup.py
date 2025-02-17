from distutils.core import setup

setup(name='rfdiffusion',
      version='1.0.0',
      description='RFdiffusion is an open source method for protein structure generation.',
      author='Rosetta Commons',
      url='https://github.com/RosettaCommons/RFdiffusion',
      scripts=["scripts/run_inference.py"],
      packages=["rfdiffusion"],
      install_requires=['torch', 'se3-transformer'])