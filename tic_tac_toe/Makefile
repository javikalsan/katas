.PHONY: default coverage tests mutation docker-tests docker-coverage docker-mutation

default:
	@printf "$$HELP"

coverage:
	python -m pytest --cov=src tests
	coverage html
	@printf "Please open the report at htmlcov/index.html\n"

tests:
	python -m unittest tests/test*

mutation:
	mutmut run --paths-to-mutate tic_tac_toe || true
	mutmut results

docker-build:
	@docker build . -t python-coverage

docker-tests:
	@docker run --rm -v "${PWD}:/opt/project" -w /opt/project python-coverage make tests

docker-coverage:
	@docker run --rm -v "${PWD}:/opt/project" -w /opt/project python-coverage make coverage

docker-mutation:
	@docker run -v "${PWD}:/opt/project" -w /opt/project python-coverage make mutation

