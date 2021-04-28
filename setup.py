import setuptools
import pkutils

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = list(pkutils.parse_requirements('requirements.txt'))

setuptools.setup(
     name='gclassifier',  
     version='0.4',
     author="Dip Ghosh",
     author_email="dipghoshraj@gmail.com",
     description="Gender classifier module for python",
     package_data= {
         'gclassifier': ['algo_model.model']
     },
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/dipghoshraj/Gender-classifer-module",
     packages=setuptools.find_packages(),
     install_requires = requirements,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )