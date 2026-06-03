##i will able to build ml apllication as package and deploy it on pypy so other people use it
from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''this funtion return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
#metadata info about project

setup(            
name = 'mlproject',
version ='0.0.1',
author = 'Tushar',
author_email='alonetushar334@gmail.com',
packages = find_packages(),
install_requires=get_requirements('requirements.txt')

)