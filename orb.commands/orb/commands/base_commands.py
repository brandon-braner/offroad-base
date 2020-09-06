import re
import subprocess
from typing import List, Tuple


def run_command(command: List) -> Tuple:
    """
    Used to run a bash command via the other click commands.
    :param command: List ['command', 'arguments']
    :return: Tuple(output, error)
    """
    p = subprocess.Popen(command, stderr=subprocess.PIPE, universal_newlines=True,
                         stdout=subprocess.PIPE)
    return p.communicate()


def run_command_2(command: List):
    result = subprocess.check_output(command)
    return result


def get_changed_files(valid_extension: str) -> List[str]:
    command = ['git', 'diff', '--name-only', '--diff-filter=d']
    files, err = run_command(command)
    files = files.replace("\n", ' ').strip()

    pattern = r'[\w\.\/]*' + valid_extension
    files = re.findall(pattern, files)
    return files
