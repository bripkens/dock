import docker

def run(args):
  print('Starting cleanup process via docker-gc...')
  docker.run(image='spotify/docker-gc',
             name='docker-gc',
             auto_remove=True,
             detach=False,
             mount_docker_socket=True,
             silent=True)
