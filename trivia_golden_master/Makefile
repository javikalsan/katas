.PHONY: default run coverage golden-master docker-run docker-golden-master tests docker-tests docker-mutation

default:
	@printf "$$HELP"

docker-build:
	@docker build . -t python-coverage

run:
	python trivia/game.py

coverage:
	python -m pytest --cov=trivia tests
	coverage html
	@printf "Please open the report at htmlcov/index.html\n"

tests:
	python -m unittest tests/test*

docker-run:
	docker run --rm -v "${PWD}:/opt/project" -w /opt/project python:3.8 make run

docker-tests:
	@docker run --rm -v "${PWD}:/opt/project" -w /opt/project python-coverage make tests

docker-coverage:
	@docker run --rm -v "${PWD}:/opt/project" -w /opt/project python-coverage make coverage

docker-mutation:
	@docker run -v "${PWD}:/opt/project" -w /opt/project python-coverage make mutation

define HELP
 Local commands
	- make run\tRun locally using Python3
	- make coverage\tRun the test coverage using Python3
	- make golden-master\tRun locally using Python3 the golden master generation and validation
 Docker commands
	- make docker-run\tRun inside docker with Python3
	- make docker-golden-master\tRun inside docker using Python3 the golden master generation and validation
 Please execute "make <command>". Example make help
endef

export HELP
