from setuptools import find_packages ,setup
#from typing import list 
#from typing import List

def get_requirement()->list[str]:
    reuirements_list = list[str]=[]
    return reuirements_list






setup(
    name="sensor",
    version="0.0.1",
    author="prince",
    author_email="anupstxavier12@gmail.com",
    packages=find_packages(),
    install_requires = get_requirement(), # ["pymongo"]

)