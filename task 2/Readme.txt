I have written two ansible files
 - docker.yml (main configuration file for the requested execution steps)
 - vars.yml (contains variables used in the docker.yml)

I have assumed that system does not have any versions of docker or any of the used packages installed

I have assumed that /etc/docker/daemon.json does not exist in the system