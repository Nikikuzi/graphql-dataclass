import sys
import os
import pathlib


sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0])).absolute()))
sys.path.append(str(pathlib.Path(os.path.dirname(sys.path[0]), 'test').absolute()))

import unittest
from .help_unittest import run_generator_cmd_help
from .help_unittest import run_generator_cmd_help
import logging as logger


class TestCLI(unittest.TestCase):

    def test_generator_cmd_help(self):
      return run_generator_cmd_help()

    def test_download_cmd_ra_file_rel(self):
      return run_download_cmd_ra_file_rel()

    def test_generate_cmd_ra_api_abs(self):
      return run_generate_cmd_ra_api_abs()

    def test_download_cmd_gdbc_file_rel(self):
      return run_download_cmd_gdbc_file_rel()

    def test_generate_cmd_gdbc_file_rel(self):
      return run_generate_cmd_gdbc_file_rel()

    def test_download_cmd_gh_file_rel(self):
      return run_download_cmd_gh_file_rel()

    def test_generate_cmd_gh_api_abs(self):
      return run_generate_cmd_gh_api_abs()

    def test_generate_cmd_gh_file(self):
      return run_generate_cmd_gh_file()


def run_download_cmd_ra_file_rel():
    logger.debug('\nRunning run_download_cmd_ra_file_rel...')
    command = "gqldataclass download ./tests/cmd_output/rapidapi/schema.json -apiArgs ./tests/cli_input/rapid_api/downloaderArgs.json -v" #command to be executed
    logger.debug("Launching: " + command)

    res = os.system(command)
    assert res == 0
    logger.debug("End of run_download_cmd_ra_file_rel")

def run_generate_cmd_ra_api_abs():
    logger.debug('\nRunning run_generate_cmd_ra_api_abs...')
    command = "gqldataclass generate ./tests/cmd_output/rapidapi -v -apiArgs ./tests/cli_input/rapid_api/generatorArgs.json -v" #command to be executed
    logger.debug("Launching: " + command)

    res = os.system(command)
    assert res == 0
    logger.debug("End of run_generate_cmd_ra_api_abs")

def run_download_cmd_gdbc_file_rel():
  logger.debug('\nRunning run_download_cmd_gh_file_rel...')
  command = "gqldataclass download ./tests/cmd_output/gdbc/schema.json -apiArgs ./tests/cli_input/gdbc_api/downloaderArgs.json -v" #command to be executed
  logger.debug("Launching: " + command)

  res = os.system(command)
  assert res == 0
  logger.debug("End of run_download_cmd_gh_file_rel")

def run_generate_cmd_gdbc_file_rel():
    logger.debug('\nRunning run_generate_cmd_gdbc_file_rel...')
    command = "gqldataclass generate ./tests/cmd_output/gdbc -apiArgs tests/cli_input/gdbc_api/schema.json -v" #command to be executed
    logger.debug("Launching: " + command)

    res = os.system(command)
    assert res == 0
    logger.debug("End of run_generate_cmd_gdbc_file_rel")

def run_generate_cmd_gdbc_api_rel():
    logger.debug('\nRunning run_generate_cmd_gdbc_api_rel...')
    command = "gqldataclass generate ./tests/cmd_output/gdbc -apiArgs ./tests/cli_input/gdbc_api/generatorArgs.json -v" #command to be executed
    logger.debug("Launching: " + command)

    res = os.system(command)
    assert res == 0
    logger.debug("End of run_generate_cmd_gdbc_api_rel")


def run_download_cmd_gh_file_rel():
    logger.debug('\nRunning run_download_cmd_gh_file_rel...')
    command = "gqldataclass download ./tests/cmd_output/github/schema.json -apiArgs ./tests/cli_input/gh_api/downloaderArgs.json -v" #command to be executed
    logger.debug("Launching: " + command)

    res = os.system(command)
    assert res == 0
    logger.debug("End of run_download_cmd_gh_file_rel")

def run_generate_cmd_gh_api_abs():
    logger.debug('\nRunning run_generate_cmd_gh_api_abs...')
    command = "gqldataclass generate ./tests/cmd_output/github -v -apiArgs ./tests/cli_input/gh_api/generatorArgs.json -v" #command to be executed
    logger.debug("Launching: " + command)

    res = os.system(command)
    assert res == 0
    logger.debug("End of run_generate_cmd_gh_api_abs")

def run_generate_cmd_gh_file():
    logger.debug('\nRunning run_generate_cmd_gh_api_abs...')
    command = "gqldataclass generate ./tests/cmd_output/github -v -apiArgs ./tests/cli_input/gh_api/generatorArgs.json -v" #command to be executed
    logger.debug("Launching: " + command)

    res = os.system(command)
    assert res == 0
    logger.debug("End of run_generate_cmd_gh_api_abs")
