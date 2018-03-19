#!/usr/bin/env python

from distutils.core import setup

setup(
    name='django-debug-toolbar-user-panel',
    description="Panel for the Django Debug toolbar to quickly switch between "
        "users.",
    version='1.1.1',
    url='https://chris-lamb.co.uk/projects/django-debug-toolbar-user-panel',

    author="Chris Lamb",
    author_email="chris@chris-lamb.co.uk",
    license='BSD',

    packages=(
        'debug_toolbar_user_panel',
    ),
    package_data={'': [
        'templates/debug_toolbar_user_panel/*',
    ]},
)
