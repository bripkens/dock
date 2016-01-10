import docker

def run():
  print('Starting cleanup process via docker-gc...')
  docker.run(image='spotify/docker-gc',
             auto_remove=True,
             detach=False,
             mount_docker_socket=True,
             silent=True)
