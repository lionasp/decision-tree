check-fmt:
	@echo "Checking formatting..."
	poetry run black --check --diff ./decision_tree

lint:
	@echo "Linting..."
	poetry run mypy ./decision_tree

fmt:
	poetry run black ./decision_tree

ci:
	poetry install
	make check-fmt
	make lint