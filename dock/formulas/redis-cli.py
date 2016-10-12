import docker

def run(args):
  docker.run(image='redis:3.0.6',
             name='redis-cli',
             auto_remove=True,
             detach=False,
             interactive=True,
             link=[['redis', 'redis']],
             silent=True,
             command=['sh', '-c', 'redis-cli -h "$REDIS_PORT_6379_TCP_ADDR" -p "$REDIS_PORT_6379_TCP_PORT"'])
