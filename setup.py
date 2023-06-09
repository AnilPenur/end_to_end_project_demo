from setuptools import find_packages,setup
# whenever find_packages() run it will search folder having __init__.py file and 
# then consider the folder as a packages and then build it to get imported in code.
# setup() is ised tto give information of project and provide required packages

from typing import List 
# to import list type aS output of get_requirements() function

HYPEN_E_DOT = '-e .' #used to trigger setup.py file

def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of requirement packjages'''

    requirement = []

    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n','') for req in requirement]
        
        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
    
    return requirement






setup(
    name='mlproject',
    version='0.0.1',
    author='Anil',
    author_email = 'anilpenur@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn']
    install_requires=get_requirements('requirements.txt')
)