project_dir := .
src_dir := src

# Lint code
.PHONY: lint
lint:
	@poetry run ruff check $(project_dir) --fix
	@poetry run mypy . --config-file ./pyproject.toml

# Check lint without fixing
.PHONY: lint-check
lint-check:
	@poetry run ruff check $(project_dir)
	@poetry run mypy . --config-file ./pyproject.toml

# Format code
.PHONY: format
format:
	@poetry run black $(project_dir)
	@poetry run isort $(project_dir)

# Check format without modifying files
.PHONY: format-check
format-check:
	@poetry run black $(project_dir) --check
	@poetry run isort $(project_dir) --check-only

# Run tests
.PHONY: tests
tests:
	@poetry run pytest

.PHONY: coverage
coverage:
	@poetry run pytest --cov=./src ./tests

# Lint + format + static analyzer + tests
.PHONY: prepare
prepare: format lint tests

# Check formatting and linting without modifications
.PHONY: check-all
check-all: format-check lint-check

# Setup pre-commit hooks
.PHONY: setup-pre-commit
setup-pre-commit:
	@poetry run pre-commit install
	@poetry run pre-commit autoupdate
