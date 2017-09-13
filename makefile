.DEFAULT_GOAL := all

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3
    PIP      := pip
    MYPY     := mypy
    PYLINT   := pylint
    COVERAGE := coverage
    PYDOC    := pydoc
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip
    MYPY     := mypy
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python3.5
    PIP      := pip3.5
    MYPY     := mypy
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3
    PIP      := pip3
    MYPY     := mypy
    PYLINT   := pylint3
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
endif

all:

clean:
	cd examples; make clean
	@echo
	cd projects/collatz; make clean

config:
	git config -l

docker:
	docker run -it -v $(PWD):/usr/cs373 -w /usr/cs373 gpdowning/python

init:
	touch README
	git init
	git add README
	git commit -m 'first commit'
	git remote add origin git@github.com:gpdowning/cs373.git
	git push -u origin master

pull:
	make clean
	@echo
	git pull
	git status

push:
	make clean
	@echo
	git add .gitignore
	git add .travis.yml
	git add examples
	git add makefile
	git add notes
	git add projects/collatz
	git commit -m "another commit"
	git push
	git status

run:
	cd examples; make run
	@echo
	cd projects/collatz; make run

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

sync:
	@rsync -r -t -u -v --delete              \
    --include "Docker.txt"                   \
    --include "Dockerfile"                   \
    --include "Hello.py"                     \
    --include "Assertions.py"                \
    --include "UnitTests1.py"                \
    --include "UnitTests2.py"                \
    --include "UnitTests3.py"                \
    --include "Coverage1.py"                 \
    --include "Coverage2.py"                 \
    --include "Coverage3.py"                 \
    --include "IsPrime1.py"                  \
    --include "IsPrime2.py"                  \
    --include "Exceptions.py"                \
    --include "Types.py"                     \
    --include "Operators.py"                 \
    --exclude "*"                            \
    ../../examples/python/ examples
	@rsync -r -t -u -v --delete             \
    --include "Collatz.py"                  \
    --include "RunCollatz.py"               \
    --include "RunCollatz.in"               \
    --include "RunCollatz.out"              \
    --include "TestCollatz.py"              \
    --include "TestCollatz.out"             \
    --exclude "*"                           \
    ../../projects/python/collatz/ projects/collatz

travis:
	cd examples; make travis
	@echo
	cd projects/collatz; make travis

versions:
	which cmake
	cmake --version
	@echo
	which make
	make --version
	@echo
	which git
	git --version
	@echo
	which $(PYTHON)
	$(PYTHON) --version
	@echo
	which $(PIP)
	$(PIP) --version
	@echo
	which $(MYPY)
	$(MYPY) --version
	@echo
	which $(PYLINT)
	$(PYLINT) --version
	@echo
	which $(COVERAGE)
	$(COVERAGE) --version
	@echo
	which $(PYDOC)
	-$(PYDOC) --version
	@echo
	which $(AUTOPEP8)
	$(AUTOPEP8) --version
	@echo
	$(PIP) list
