import re
import subprocess
from typing import List, Tuple


def run_command(command: List) -> Tuple:
    """Run a bash command via the other click commands."""
    proc = subprocess.Popen(command, stderr=subprocess.PIPE, universal_newlines=True, stdout=subprocess.PIPE)
    return proc.communicate()


def get_changed_files(valid_extension: str) -> List[str]:
    """
    Get a list of changed files via git.

    Remove excluded files that do not need checked.
    """
    command = ["git", "diff", "--name-only", "--diff-filter=d"]
    files = run_command(command)
    files = files[0].replace("\n", " ").strip()
    files = _remove_excluded_files(files)
    pattern = r"[\w\.\/]+" + valid_extension
    files = re.findall(pattern, files)
    return files


def _remove_excluded_files(files: str) -> str:
    """Break apart a string of files separated by a space and remove excluded files."""
    excluded_files = [
        '.flake8',
        '.pylintrc',
        'pyproject.toml',
        '.pydocstyle'
    ]

    files = files.split(' ')
    files = [file for file in files if file not in excluded_files]
    return ' '.join(files)
