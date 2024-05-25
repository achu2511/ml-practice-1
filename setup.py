from setuptools import find_packages,setup
from typing import List


hypen='-e .'
def get_requirements(file_path:str)-> List[str]:
    ''' this function will return list of requirements'''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[r.replace("\n","") for r in requirements]

        if hypen in requirements:
            requirements.remove(hypen)
            
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='achyuth',
    author_email='achyuth2511@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)