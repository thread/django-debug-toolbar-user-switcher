from setuptools import setup

setup(
    name="django-debug-toolbar-user-switcher",
    description="Panel for the Django Debug toolbar to quickly switch between users.",
    version="2.0.0",
    author="Thread Engineering",
    author_email="tech@thread.com",
    license="BSD",
    packages=["debug_toolbar_user_switcher"],
    package_data={"": ["templates/debug_toolbar_user_switcher/*"]},
)
