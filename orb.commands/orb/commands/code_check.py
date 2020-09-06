import os
from orb.commands.base_commands import run_command, get_changed_files, run_command_2

def main():
    command = ['echo', 'test']
    run_command(command)


def pylint_check():
    command = ['pylint']
    files = get_changed_files(valid_extension='.py')
    if files:
        files_str = ' '.join(files)
        print(f"Running pylint on {files_str}")
        command.extend(files)
        output = run_command(command)
        print('/n'.join(output))
