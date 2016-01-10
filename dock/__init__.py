#!/usr/local/opt/python/bin/python2.7

import argparse

import formula


def print_version():
  print('dock {} by Ben Ripkens and contributors'.format('2.0.2'))
  print('https://github.com/bripkens/dock')


def main():
  parser = argparse.ArgumentParser(prog='dock',
                                   usage='%(prog)s [options] [formula] [formula arguments...]',
                                   description='easily bootstrap development tools with Docker')
  parser.add_argument('formulas',
                      help='Execute the given formulas in the order in which they are defined on the command line.',
                      nargs='*')
  parser.add_argument('-v', '--version',
                      action='store_true',
                      help='Display current script version')
  parser.add_argument('-l', '--list',
                      action='store_true',
                      help='List available formulas')
  parser.add_argument('--cleanup',
                      action='store_true',
                      help='Remove unused containers and images via docker-gc')
  args = parser.parse_args()

  if args.version:
    print_version()
  if args.cleanup:
    formula.execute_formula('docker-gc', [])
  elif args.list:
    formula.list_available_formulas()
  elif len(args.formulas) == 0:
    parser.print_help()
  else:
    formula.execute_formula(args.formulas[0], args.formulas[1:])


if __name__ == '__main__':
  main()
