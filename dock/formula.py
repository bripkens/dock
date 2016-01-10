import importlib
import os.path
import re
import subprocess

HERE = os.path.abspath(os.path.dirname(__file__))
FORMULA_DIR = os.path.join(HERE, 'formulas')

def list_available_formulas():
  print(':: Built-In Formulas')
  for formula in sorted(os.listdir(FORMULA_DIR)):
    if formula.endswith('.py') and not formula == '__init__.py':
      match = re.search('([^.]+)\\.', formula)
      print(match.group(1))


def print_unknown_formula_contribution_hint(formula):
  print('Unknown formula: {}'.format(formula))
  print('')
  print('If you feel like {} should be supported by dock, please'.format(formula))
  print('consider opening an issue or sending a pull request to')
  print('')
  print('       https://github.com/bripkens/dock')
  print('')
  print('Thanks!')


def ensure_docker_usage_is_possible():
  returnCode = subprocess.call(['docker', 'ps'], stdout=open(os.devnull, 'w'))
  if not returnCode == 0:
    print('It seems like there are issues with your Docker setup.')
    sys.exit(1)


def execute_formula(formula, formula_args):
  ensure_docker_usage_is_possible()
  module_name = 'formulas.' + formula
  try:
    mod = importlib.import_module(module_name)
    path_to_module = os.path.join(FORMULA_DIR, formula + '.py')
    mod.run(formula_args)
  except ImportError as e:
    if e.message.endswith(formula):
      print_unknown_formula_contribution_hint(formula)
    else:
      raise
