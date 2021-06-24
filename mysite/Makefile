format:
	@black -l 80 . --exclude=.venv

install:
	@poetry install
	@pre-commit install

.PHONY: test format check install sh run
