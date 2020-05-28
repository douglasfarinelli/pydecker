export DEBUG=1
export PYTHONPATH=src/
export PIPENV_VENV_IN_PROJECT=1

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean:  ## Clean unnecessary files
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -rf .coverage .cache/ .mypy_cache/ .pytest_cache/ htmlcov/ coverage.xml *.log

init:  ## Initialize virtualenv
	@pip install pip pipenv --user --upgrade
	@make dependencies

ci: tests  ## Run CI steps: lint and tests

shell:  ## Run repl (ipython)
	@pipenv run ipython

outdated:  ## Find outdated python dependencies
	@pipenv update --bare --outdated

lock:  ## Update Pipfile.lock
	@pipenv lock

dependencies:  ## Install python dependencies
	@pipenv sync --dev

format:  ## Run decker format
	@pipenv run python -m decker format

tests:  clean ## Run tests with coverage
	@pipenv run pytest -xvv --cov src/decker src/tests \
        --no-cov-on-fail \
        --cov-report=xml \
        --cov-report=term-missing src/decker src/tests

test-matching:  clean  ## Run tests matching, ex.: make test-matching q=<term>
	@pipenv run pytest -xvv src/decker src/tests -k "$(q)"
