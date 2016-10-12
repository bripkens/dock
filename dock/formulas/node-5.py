import docker

def run(args):
  docker.run(image='node:5',
             name='node-5',
             auto_remove=True,
             detach=False,
             interactive=True,
             silent=True,
             command=['bash'])
