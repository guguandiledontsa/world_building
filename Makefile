.PHONY: install lint test format all

PY_FILES := $(shell git ls-files '*.py')

## Install all required tools
install:
	pip install --upgrade pip
	pip install -r requirements.txt || true  # optional
	pip install pylint black

## Run linting
lint:
	pylint $(PY_FILES) --fail-under=8

## Run unit tests
test:
	python -m unittest discover -s src/tests -t src

## Format code using Black
format:
	black $(PY_FILES)

## Run everything
all: install lint test
