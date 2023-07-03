from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as fille_obj:
        requirements=fille_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements

setup(
    name="Diamon Price Prediction",
    verson="0.0.1",
    author="Swadhn Gyanajyoti Nayak",
    author_email="nayakswadhingyanajyoti@gmail.com",
    install_require=get_requirements("requirement.txt"),
    packages=find_packages()
)