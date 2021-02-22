from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(
	name="toto",
	description="My first python package",
	packages=["toto"],
	scripts=["scripts/toto-run"],
	install_requires=requirements,
)
