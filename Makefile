project_dir := .
src_dir := src

# Lint code
.PHONY: lint
lint:
	@poetry run ruff check $(project_dir) --fix
	@poetry run mypy . --config-file ./pyproject.toml

# Format code
.PHONY: format
format:
	@poetry run black $(project_dir)
	@poetry run isort $(project_dir)

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
