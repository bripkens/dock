import docker

def run(args):
  docker.run(image='postgres:9.5.0',
             name='postgres-cli',
             auto_remove=True,
             detach=False,
             interactive=True,
             link=[['postgres', 'postgres']],
             silent=True,
             command=['sh', '-c', 'psql -h "$POSTGRES_PORT_5432_TCP_ADDR" -p "$POSTGRES_PORT_5432_TCP_PORT" -U admin'])
