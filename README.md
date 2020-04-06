# Brute Force (Python 3.x)

This is a simple Brute Force program to find a correct password among infinite combinations. This program should not, 
under any circumstances, be used for abusive practices but only for educational purposes.

# How to use it ?

Just run the program by passing the required arguments on the command line. See the example below:

```
$ python "Brute Force.py" --command="start app {}" --code=200 
```

You can also edit the `validator.py` file as you wish as long it has a function called `main(command, password)` that 
returns an code ( integer ). 

```
def main(command, password) -> int:
    # ...
    return int()
```
