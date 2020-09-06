from setuptools import setup, find_packages

setup(
    name='orb.commands',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        orb-commands:pylint=orb.commands.code_check:pylint_check
    ''',
)