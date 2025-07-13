#used to install all the requiemrnts when i call my project as a package,makes my code importable as a package,
#and it also enables u to run and reuse ur project easily


from setuptools import find_packages,setup#find_packages= find all folders that contain an __init__.py file and include them as python module
#setup()=It tells Python and pip how to install your project.
#The whole point of setup() (with find_packages()) is to make your project's modules importable from anywhere — just like real Python libraries and we can call modules from the src folder.

from typing import List #Just adds type hinting to your function

HYPEN_E_DOT='-e .' #It tells pip to install the project in editable mode and trigger the setup.py file from requirements.txt
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject', #of the package
version='0.0.1', #version of the package
author='Palak',
author_email='palakmathur2811@gmail.com',
packages=find_packages(), # to detect all folders with __init__.py in it i.e a module in src(source)
install_requires=get_requirements('requirements.txt')

)
# therefore when we do pip install -r requirements.txt the -e. will trigger and will help us go to setup.py to help in setting up the project/package and now mlproject.egg-info gets created 