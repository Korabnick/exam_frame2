.PHONY: install test lint run migrate upgrade downgrade clean

install:
	pip install -r requirements.txt

test:
	pytest -v --cov=app --cov-report=term-missing tests/

test-unit:
	pytest -v --cov=app --cov-report=term-missing tests/unit/

test-integration:
	pytest -v --cov=app --cov-report=term-missing tests/integration/

test-html:
	pytest --cov=app --cov-report=html
	start htmlcov/index.html

lint:
	flake8 app/

run:
	flask run

migrate:
	flask db migrate -m "Migration message"

upgrade:
	flask db upgrade

downgrade:
	flask db downgrade

clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -exec rm -rf {} +
	rm -f .coverage

erd:
	python scripts/generate_er_diagram.py