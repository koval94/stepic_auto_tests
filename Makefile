.MAIN: help
.ONESHELL:
.PHONY: help run docs venv
.SILENT:

VENV := ./venv
DOCKER := podman
PYTHON := python
PYTHON_VENV := $(VENV)/Scripts/python

R=`tput setaf 1 1 1`
G=`tput setaf 2 1 1`
B=`tput bold`
RES=`tput sgr0`

run: venv  ## Run tests (without docker) on Win.
	$(PYTHON_VENV) -m pytest

docs: venv  ## Build project docs on Win.
	$(VENV)/Scripts/sphinx-apidoc -o ./docs/source ./lib
	$(VENV)/Scripts/sphinx-build -E -b html ./docs/source ./build/html

venv: requirments.txt  ## Update existing or create new venv with dependencies on Win.
	printf "${B}INFO${RES}: Starting creating virtual environment.\n"
	test -d $(VENV) || $(PYTHON_VENV) -m venv $(VENV)
	test -f ./pytest.ini || (cp ./pytest.ini.example ./pytest.ini & \
		printf "${B}INFO${RES}: \
		New pytest.ini created from pytest.ini.example.\n")
	printf "${B}INFO${RES}: \
		Start installing python packages according to requirements.txt.\n"
	$(PYTHON_VENV) -m pip install --no-cache-dir -Uqr ./requirments.txt \
		--disable-pip-version-check
	printf "${G}SUCCESS${RES}: Virtual environment successfully created/updated.\n"



