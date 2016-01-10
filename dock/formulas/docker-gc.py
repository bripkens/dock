import docker

def run(args):
  docker.run(image='spotify/docker-gc',
             name='docker-gc',
             auto_remove=True,
             detach=False,
             mount_docker_socket=True,
             silent=True)
