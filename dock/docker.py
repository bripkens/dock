import json
import os
import re
import subprocess
import time

import formula

devnull = open(os.devnull, 'w')

def msg(k, v):
  label = k + ':' if len(k) > 0 else ''
  print(label.ljust(20, ' ') + v)


def add_name_prefix(container_name):
  return 'dock-' + container_name


def force_stop(name):
  name = add_name_prefix(name)
  subprocess.call(['docker', 'stop', name],
                  stdout=devnull,
                  stderr=devnull)
  subprocess.call(['docker', 'rm', name],
                  stdout=devnull,
                  stderr=devnull)


def is_container_running(name):
  try:
    output = subprocess.check_output(['docker', 'inspect', name],
                                     stderr=devnull)
  except Error:
    return False

  return json.loads(output)[0]['State']['Running']


def requires(dependent, dependency):
  prefixed_dependency = add_name_prefix(dependency)
  if not is_container_running(prefixed_dependency):
    print('{} requires {} in order to run. Starting {}'.format(dependent,
                                                               dependency,
                                                               dependency))
    formula.execute_formula(dependency, [])


def run(image,
        name,
        publish=[],
        auto_remove=False,
        detach=True,
        mount_docker_socket=False,
        silent=False,
        interactive=False,
        link=[],
        command=None,
        entrypoint=None,
        env={}):
  name = add_name_prefix(name)

  args = ['docker', 'run', '--name', name]

  if detach:
    args.append('--detach')

  if auto_remove:
    args.append('--rm')

  if interactive:
    args.extend(['--interactive', '--tty'])

  if not entrypoint == None:
    args.extend(['--entrypoint', entrypoint])

  if mount_docker_socket:
    args.extend(['--volume', '/var/run/docker.sock:/var/run/docker.sock'])

  for publishedPort in publish:
    args.extend(['--publish', '{}:{}'.format(publishedPort, publishedPort)])

  for each_link in link:
    args.extend(['--link', '{}:{}'.format(add_name_prefix(each_link[0]),
                                          each_link[1])])

  for key in env:
    args.extend(['--env', '{}={}'.format(key, env[key])])

  args.append(image)

  if not command == None:
    args.extend(command)

  if not silent:
    print('Starting image {} as container {}'.format(image, name))

  result = subprocess.call(args)
  if not result == 0:
    print('Failed to start container.')
    return

  if not silent:
    # Docker cli can return before the new container can be inspected. This
    # is very unfortunate. The following is a fragile solution which needs
    # to be revisited in time.
    time.sleep(0.5)
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

  msg('Container Name', name)
  msg('IP', get_ip())

  if len(ports) > 0:
    msg('Ports', 'Host  -> Container')

  for port in ports:
    stripped_port = strip_protocol_from_port(port)

    host_ports = port_mappings[port]
    # host ports may be None when the ports are not published
    if host_ports == None:
      continue

    for host_port in host_ports:
      msg('', '{} -> {}'.format(host_port['HostPort'].ljust(5, ' '),
                                stripped_port))
