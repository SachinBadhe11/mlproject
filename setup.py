from setuptools import find_packages, setup
from typing import list 

Hyphen_E_Dot='-e .'
def get_requirements(File_path:str)->list[str]:
    requirements=[]
    with open(File_path) as file_obj:
        requirements=file_obj.readlines
        requirements=[req.replace("\n","") for req in requirements]

        if Hyphen_E_Dot in requirements:
            requirements.remove(Hyphen_E_Dot)

    return requirements        

setup(
    name='mlproject',
    version='0.0.1',
    author_email='sachinbadhe983@gmail.com',
    packages= find_packages(),
    install_requires=['pandas','numpy','seaborn'],
    install_requires=get_requirements('requirements.txt')

)