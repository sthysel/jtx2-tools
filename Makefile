.PHONY: clean-pyc clean-build test

VENV_NAME?=~/.virtualenvs/jtx2tools
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python

.DEFAULT: help
help:
	@echo "Open the Makefile and have a look"
	@echo
	@echo "venv is at $(VENV_NAME)"

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: setup.py requirements.txt dev-requirements.txt
	test -d $(VENV_NAME) || python3.6 -m venv $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -e .
	${PYTHON} -m pip install -r dev-requirements.txt
	touch $(VENV_NAME)/bin/activate


all: clean sdist wheel

clean: clean-build clean-pyc

clean-build:
	$(info # Removing build artefacts)
	-rm -fr build/
	-rm -fr dist/
	-rm -fr *.egg-info

clean-pyc:
	$(info # Removing pycies artefacts)
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +


lint: venv
	${VENV_ACTIVATE}; flake8 --exclude=.tox
	${PYTHON} -m mypy src/


test: venv
	${PYTHON} -m tox

test-version: venv
	${PYTHON} -m pytest -k livestats_version_checker_test

patch:
	${VENV_ACTIVATE}; bumpversion patch
minor:
	${VENV_ACTIVATE}; bumpversion minor
major:
	${VENV_ACTIVATE};	bumpversion major

git-clean:
	git clean -f -d

md2rst: README.md
	pandoc --from=gfm --to=rst --output=README.rst README.md
	-git commit -m "doc patch" README.rst


