.PHONY: install lint

install:
	pip install --upgrade pip
	pip install pylint

lint:
	pylint $(shell git ls-files '*.py') --fail-under=8
