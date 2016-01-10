import json
import os
import re
import subprocess

devnull = open(os.devnull, 'w')


def add_name_prefix(container_name):
  return 'dock-' + container_name


def generate_name_from_image(image):
  # Docker container names cannot contain slashes
  return image.replace('/', '_')


def force_stop(name):
  name = add_name_prefix(name)
  subprocess.call(['docker', 'stop', name],
                  stdout=devnull,
                  stderr=devnull)
  subprocess.call(['docker', 'rm', name],
                  stdout=devnull,
                  stderr=devnull)


def run(image,
        name=None,
        publish=[],
        auto_remove=False,
        detach=True,
        mount_docker_socket=False,
        silent=False):
  if name == None:
    name = generate_name_from_image(image)

  name = add_name_prefix(name)

  args = ['docker', 'run', '--name', name]

  if detach:
    args.append('--detach')

  if auto_remove:
    args.append('--rm')

  if mount_docker_socket:
    args.extend(['--volume', '/var/run/docker.sock:/var/run/docker.sock'])

  for publishedPort in publish:
    args.extend(['--publish', '{}:{}'.format(publishedPort, publishedPort)])

  args.append(image)
  if not silent:
    print('Starting image {} as container {}'.format(image, name))
  subprocess.call(args)

  if not silent:
    print_run_data(name)


def strip_protocol_from_port(port):
  return re.search('^(\d+)', port).group(1)


def get_ip():
  try:
    docker_machine_name = os.environ['DOCKER_MACHINE_NAME']
    return subprocess.check_output(['docker-machine',
                                    'ip',
                                    docker_machine_name],
                                   stderr=devnull).strip()
  except KeyError:
    pass

  try:
    return subprocess.check_output(['boot2docker', 'ip'],
                                   stderr=devnull)
  except subprocess.CalledProcessError:
    pass

  return '127.0.0.1'


def print_run_data(name):
  output = subprocess.check_output(['docker', 'inspect', name])
  port_mappings = json.loads(output)[0]['NetworkSettings']['Ports']
  ports = port_mappings.keys()
  ports.sort()

  print('Container Name:    {}'.format(name))
  print('IP:                {}'.format(get_ip()))

  if len(ports) > 0:
    print('Ports:             Host  -> Container')

  for port in ports:
    stripped_port = strip_protocol_from_port(port)
    for host_port in port_mappings[port]:
      print('                   {} -> {}'.format(host_port['HostPort'].ljust(5, ' '),
                                                 stripped_port))
