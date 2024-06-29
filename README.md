## Toy Robot (v1.0.0)

This repo contains an implementation of a toy robot that moves in a 5x5 grid axis starting

from (0,0) at the bottom left SOUTH WEST corner of the grid. The robot can move through commands

entered via command list or via console.

##### Command List:
| Command | Params      | Description                                  |
|---------|-------------|----------------------------------------------|
| PLACE   | (x, y, face)| Places the robot based on params             |
| MOVE    |             | Moves the robot based on current face        |
| RIGHT   |             | Rotates the robot 90 degrees to the right    |
| LEFT    |             | Rotates the robot 90 degrees to the left     |
| REPORT  |             | Reports the current location of the robot    |
| PRINT   |             | Displays a visual representation of the grid |

##### Face List:
| Face Name | Description                                 |
|-----------|---------------------------------------------|
| NORTH     | Changes the robot's face direction upward   |
| EAST      | Changes the robot's face direction to the right |
| SOUTH     | Changes the robot's face direction downward |
| WEST      | Changes the robot's face direction to the left  |

##### Examples:
```
a)----------------
PLACE 0,0,NORTH
MOVE
REPORT
Output: 0,1,NORTH
b)----------------
PLACE 0,0,NORTH
LEFT
REPORT
Output: 0,0,WEST
c)----------------
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
Output: 3,3,NORTH
```

### Dependencies
#### Required:
* [Python][1] 3.6+

### Python libs
#### Regarding `requirements.txt` and `requirements-test.txt` dependencies

`Requirements.txt` - Contains application specific libraries needed during run-time
`Requirements-test.txt` - Contains test (unit, static, etc) specific libraries during test execution
   
Requirements are listed in alphabetical order with the following general
format. Note that `<repo` can be used as a substitution, to help shorten urls if needed.

```

dep==version

# usage: <short description>

# repo: <link to code repo>

# license: <license> - <license url>

# docs: <link to documentation (if any)>
```

Example:
```
graphene==1.4.1

# usage: framework to support GraphQL schema definitions

# repo: https://github.com/graphql-python

# license: MIT - <repo>/graphene/blob/v1.4.1/LICENSE

# docs: http://graphene-python.org
```

 
### Setup

1. Install python on to your local machine 
2. Install the required packages in the new environment.
```
pip install -r requirements-test.txt
```

### Execution
There are  2 ways to run the Toy Robot, `CONSOLE` and `COMMANDLIST` 

- `CONSOLE` - Opens a command line like console where in users can input the commands (listed ) above and obtain the  its present state 
- `COMMANDLIST` - Together with a command list file, the robot would try to execute each of the commands in the list. The robot would return an error message if the an error is encountered during the batch processing. Otherwise it would return the last known position of the robot.

##### CONSOLE MODE
```
	>> python main.py CONSOLE
```
Console Prompt: 
```
COMMAND: <insert command here>
```
Example Execution:
```
COMMAND: PLACE 0,0,NORTH
0,0,NORTH
COMMAND: MOVE
0,1,NORTH
COMMAND: MOVE
0,2,NORTH
COMMAND: RIGHT
0,2,EAST
COMMAND: MOVE
1,2,EAST
COMMAND: PRINT
 .   .   .   .   .
 .   .   .   .   .
 .   ▶   .   .   .
 .   .   .   .   .
 .   .   .   .   .
COMMAND:
```
 
##### COMMANDLIST MODE
```
	>> python main.py COMMANDLIST <file path>
```
Example: 
```
PS C:\Users\Irvin\Desktop\Toy Robot> python main.py COMMANDLIST .\tests\fixtures\example_3.txt                                                     
```
Example Command List
```
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
```

Example Output:
  ```
1,2,EAST
2,2,EAST
3,2,EAST
3,2,NORTH
3,3,NORTH
3,3,NORTH
 .   .   .   .   .
 .   .   .   ▲   .
 .   .   .   .   .
 .   .   .   .   .
 .   .   .   .   .
3,3,NORTH  
```
  
  

### Testing 
Basic testing facility has been setup for the repository Formatter, Static and Unit Tests

* Formatter Check - Black
```
	>> black .
```  
* Linter Check - PyLint, Flake8
```
	>> pylint .
	>> flake8 . 
```
* Unit Test - Pytest
```
	>> pytest --verbose
```
 
[1]: https://www.python.org/