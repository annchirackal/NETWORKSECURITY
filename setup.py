from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements

    """
    try : 
        with open("requirements.txt",'r') as file :
          ##Read lines from the file
          lines = file.readlines()
          ## Process each line
          requirement_list =[]
          for line in lines:
             requirement = line.strip()
             ## ignore the empty lines and -e .
             if requirement and requirement != '-e .':
                requirement_list.append(requirement)
    except FileNotFoundError :
       print("requirements.txt file not found")
    ##print(requirement_list)

    return requirement_list

setup(
   name = "NETWORKSECURITY",
   version = "0.0.1",
   author = " Ann Chirackal",
   email = " annchirackal@gmail.com",
   packages = find_packages(),
   intstall_requires = get_requirements()

)
          



