import docker

def run(args):
  docker.run(image='cassandra:3.1.1',
             name='cassandra-cli',
             auto_remove=True,
             detach=False,
             interactive=True,
             link=[['cassandra', 'cassandra']],
             silent=True,
             command=['sh', '-c', 'cqlsh -u cassandra -p cassandra "$CASSANDRA_PORT_9042_TCP_ADDR" "$CASSANDRA_PORT_9042_TCP_PORT"'])
