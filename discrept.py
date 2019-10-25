import subprocess
from sys import argv

import os


def execute(cmd):
    p_open = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(p_open.stdout.readline, ""):
        print(stdout_line)
    p_open.stdout.close()
    return_code = p_open.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)


if __name__ == '__main__':
    execute(["cd", os.getcwd()])
    execute(["python", os.path.dirname(os.path.abspath(__file__)) + "/__init__.py"] + argv[1:])
