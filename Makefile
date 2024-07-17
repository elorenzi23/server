# Variables
PYTHON = python3
PIP = pip

# Targets and commands
setup:
    python -m venv venv
    venv/bin/pip install -r requirements.txt


test:
    $(PYTHON) -m pytest

clean:
    rm -rf __pycache__

.PHONY: setup test clean
