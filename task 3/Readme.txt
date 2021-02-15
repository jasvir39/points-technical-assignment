I have shared two project folder for this task:
 1. Ager/ folder contains 
     -- ager.py script (which is the main script to test the requested behavior, it initiates the docker_runner() method in class DockerRunner, with                 given arguments (name, age))

     -- docker_runner.py script (it contains class DockerRunner which defines methods to create client object and run docker container with passed                   aruguments from CLI using ager.py and docker image built using Dockerfile in the UserApp project)

     -- input_parser.py script (it containes class InputParser which provides a CLI parser for arguments(name, age) using argparse module)

     -- test_input_parser.py (it contains a few tests (using pytest module) for the validation of behavior of python script for varied inputs)
     

2. UserApp/ folder contains
     -- user.py (it contains class User() which provides methods to initialize variables (name, age) and print message
     -- main.py (it creates argument parser for arguments(name, age) using argparse module, and pass on the parsed values to class User and method print())
     -- Dockerfile (it takes Python as a base image, creates directory and set it as work directory, copies both scripts (user.py, main.py) to the created           directory)