


def f(x):
    return len(x)

# Test for Python versions and environments
import os
import sys
import re


def os_and_sys_version():
    python_version = re.search(r"\d+\.\d+", sys.version).group()
    os_name = os.getenv("RUNNER_OS")
    return python_version, os_name
