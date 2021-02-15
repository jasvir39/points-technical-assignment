import docker
import os
import traceback
import time

class DockerRunner():
    '''This class provides methods to run docker container. It creates a docker client object from environment varialbes'''
    def __init__(self):
        try:
            self.client = docker.from_env()
        except docker.errors.DockerException:
            traceback.print_exc()
            print("can not connect to Docker Engine")

    def run(self, name, age):
        '''This method takes name and age as arguments, starts a container with given arguments, reads logs from the container'''
        try:
            self.client.ping()
            print("docker run", end='', flush=True)
            container_id = self.client.containers.run(image=os.environ.get('DOCKER_IMAGE'),
                                                command="python main.py -name {} -age {}".format(name, age),
                                                stderr=False, remove=False, detach=True)

            count = 0
            while container_id.status != 'exited':
                time.sleep(1)
                if count < age:
                    print(".", end='', flush=True)
                count = count + 1
                container_id.reload()
            print()
            for line in container_id.logs(stream=True, follow=True):
                print(line.decode('utf-8').strip())
        except docker.errors.APIError:
            print("can not connect to docker client")
            traceback.print_exc()
        except AttributeError:
            traceback.print_exc()
            print("client object does not exist")