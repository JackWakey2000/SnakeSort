# <p align="center">SnakeSort - A simple Python file organizer.</p>

<div align="center">

  <a href="">![version: unfinished](https://img.shields.io/badge/version-1.0-red)</a>
  <a href="">![python version: 3.14.0](https://img.shields.io/badge/python_version-3.14.0-%233776AB?logo=python&logoColor=%23FFFFFF
  )</a>

</div>

## Q&A
### Q. Why are you using os.system, which is deprecated?
A. Mobile users do not have accses to subproccess.run()

### Q. Help! Im getting a FileExistsError 
A. Make sure your none of your folders are named "Directories"

## Required Python Packages
- os (bundled with python)
- os.path (bundled with python)
- shutil (bundled with python)
- termcolor


## Disclaimer
- Snakesort may break symlinks.
- Snakesort is tested on windows. Might have limited functionality on linux.
- SnakeSort is written and tested on Python 3.14. Feel free to test on other versions and do a PR to add here if they work!