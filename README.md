# PYTHON PROBLEMS

## GENERAL INFO
This project contains a series of problems that needs to be solved in python. 
Each module requires a student to write one main method with name speciefied in the assignment and appropriate unit test. 
Additional helper methods may be needed (with some tests as well), but tests are required for only main method.

Main method must also have *docstring* explaining the purpose of that method (not the solution). For convention checkout official python docs [pep-0257](https://www.python.org/dev/peps/pep-0257/).
Comments are also welcomed, as long as they are not redundant.

You can check *example.py* and *test_example.py* for help, but remember - those files are only a guidance not a pattern that you should stick to!

## BRANCHES STRUCTURE
- **master** - has the starting code
- **problems** - has only the problems; only trainer can update the branch
- **solutions** - has code of problems and solutions; changes to this branch are only possible via PR
- **soulution/name_of_problem** - temporarry branch created by student where current work can be stored

## HOW TO SUBMIT NEW SOLUTION
1) check if problems branch has new code
2) create new temporary solution branch with name *solution/name_of_problem*
3) create two new files *name_of_problem.py* and *test_name_of_problem.py*
4) write your solution with unit tests, commit the changes when you see fit and push them to your origin solution branch
5) create pull request from your soulution branch to **solutions** - during a PR unittests will be run so be absolutly sure they all pass before you create your PR
6) wait for the changes to be reviewed (additional pushes to your solution branch may be required) and once approved merge the PR and remove your solution branch afterwards

## USEFUL COMMANDS
### Running all unittests
`python3 -m unittest discover`
### Running unit test from selected file
`python3 -m unittest discover filename_without_test`
