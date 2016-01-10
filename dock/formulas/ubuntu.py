import docker

def run(args):
  docker.run(image='ubuntu:14.04',
             name='ubuntu',
             auto_remove=True,
             detach=False,
             interactive=True,
             silent=True,
             command=['bash'])
