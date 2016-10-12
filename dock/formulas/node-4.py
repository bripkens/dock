import docker

def run(args):
  docker.run(image='node:4',
             name='node-4',
             auto_remove=True,
             detach=False,
             interactive=True,
             silent=True,
             command=['bash'])
