from typing import List

import click
from orb.commands.base_commands import run_command, get_changed_files


@click.group(invoke_without_command=True)
@click.pass_context
def precommit_check(ctx):
    """Command to run with a git precommit hook."""
    click.echo(click.style('Running Precommit Hook', fg="green"))
    ctx.invoke(flake8_check)
    ctx.invoke(pylint_check)
    ctx.invoke(pydocstyle_check)


@precommit_check.command()
def pylint_check():
    """
    Run pylint on the files changed in git with a .py extension.

    Update settings in the .pylintrc file in the root of the project.
    """
    command = ["pylint"]
    output = _run_command_on_changed_files("PyLint", command)
    click.echo(click.style(output, fg="blue"))


@click.command()
def flake8_check():
    """
    Run flake8 on files that have changed in git with a .py extension.

    Update settings .flake8 file in the root of the project.
    """
    command = ["flake8"]
    output = _run_command_on_changed_files("Flake8", command)
    click.echo(click.style(output, fg="blue"))


@click.command()
def black_check():
    """
    Run black on files that have changed in git with a .py extension.

    Update settings in the pyproject.toml.
    """
    command = ["black"]
    output = _run_command_on_changed_files("Black", command)
    click.echo(click.style(output, fg="blue"))


@click.command()
def pydocstyle_check():
    """
    Run pydocstyle on changed files in git with a .py extension.

    Configuration handled via .pydocstyle in root.
    """
    command = ["pydocstyle"]
    output = _run_command_on_changed_files("PyDoc", command)
    click.echo(click.style(output, fg="blue"))


def _run_command_on_changed_files(name: str, command: List[str], extension: str = ".py"):
    """Get the changed files and run the requested command on those files."""
    click.echo(click.style(f"Running {name} ...", fg="green"))
    files = get_changed_files(valid_extension=extension)
    command.extend(files)
    output = run_command(command)
    output = "/n".join(output)
    return output.strip("/n")
