from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements_lst: List[str] = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please create it with the necessary dependencies.")
    return requirements_lst
setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Abhiram S R',
    author_email='abhiramsr173@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)