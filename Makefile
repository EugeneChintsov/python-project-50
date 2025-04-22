install:
	uv sync

installdev:
	uv pip install --editable .[dev]

run:
	uv run gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

lint:
	uv run ruff check

check: test lint

build:
	uv build

package-build:
	python3 -m pip install dist/*.whl

package-install: install build package-build

package-uninstall:
	python3 -m pip uninstall hexlet-code || True

.PHONY: install test lint selfcheck check build package-build package-install package-uninstall