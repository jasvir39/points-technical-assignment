from input_parser import InputParser
from docker_runner import DockerRunner

if __name__ == "__main__":
    user_info = InputParser()
    docker_runner = DockerRunner()
    docker_runner.run(user_info.get_name(), user_info.get_age())

