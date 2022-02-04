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
	@docker build . -t python-testing

docker-tests:
	@docker run --rm -v "${PWD}:/opt/project" -w /opt/project python-testing make tests

docker-coverage:
	@docker run --rm -v "${PWD}:/opt/project" -w /opt/project python-testing make coverage

docker-mutation:
	@docker run -v "${PWD}:/opt/project" -w /opt/project python-testing make mutation

define HELP
 Local commands
        - make test\tRun tests locally using Python3
        - make coverage\tRun tests coverage using Python3
        - make mutation\tRun mutation tests locally using Python3
 Docker commands
        - make docker-build\tBuild docker image to execute dockerized testing tools
        - make docker-test\tRun inside docker with Python3
        - make docker-coverage\tRun inside docker using Python3
        - make docker-mutation\tRun mutation tests inside docker using Python3
 \nPlease execute "make <command>". Example: make docker-build\n
endef

export HELP