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
	@rsync -r -t -u -v --delete            \
    --include "Docker.txt"                 \
    --include "Dockerfile"                 \
    --include "Hello.py"                   \
    --include "Assertions.py"              \
    --include "UnitTests1.py"              \
    --include "UnitTests2.py"              \
    --include "UnitTests3.py"              \
    --include "Coverage1.py"               \
    --include "Coverage2.py"               \
    --include "Coverage3.py"               \
    --include "IsPrime1.py"                \
    --include "IsPrime2.py"                \
    --include "Exceptions.py"              \
    --include "Types.py"                   \
    --include "Operators.py"               \
    --include "Variables.py"               \
    --include "Factorial1.py"              \
    --include "Factorial2.py"              \
    --include "Reduce1.py"                 \
    --include "Reduce2.py"                 \
    --include "Iteration.py"               \
    --include "Comprehensions.py"          \
    --include "Yield.py"                   \
    --include "Map1.py"                    \
    --include "Map2.py"                    \
    --include "Iterables.py"               \
    --include "RangeIterator1.py"          \
    --include "RangeIterator2.py"          \
    --include "Range1.py"                  \
    --include "Range2.py"                  \
    --include "FunctionKeywords.py"        \
    --include "FunctionDefaults.py"        \
    --include "FunctionUnpacking.py"       \
    --include "FunctionTuple.py"           \
    --include "FunctionDict.py"            \
    --include "Select1.py"                 \
    --include "Select2.py"                 \
    --include "Project1.py"                \
    --include "Project2.py"                \
    --include "CrossJoin1.py"              \
    --include "CrossJoin2.py"              \
    --include "ThetaJoin1.py"              \
    --include "ThetaJoin2.py"              \
    --include "NaturalJoin1.py"            \
    --include "NaturalJoin2.py"            \
    --include "SQLite.py"                  \
    --include "With.py"                    \
    --include "RegExps.py"                 \
    --include "Strings.py"                 \
    --include "Reflection.py"              \
    --include "StrategyPattern10.py"       \
    --exclude "*"                          \
    ../../examples/python/ examples
	@rsync -r -t -u -v --delete            \
    --include "ShowDatabases.sql"          \
    --include "ShowEngines.sql"            \
    --include "Create.sql"                 \
    --include "Select.sql"                 \
    --include "Join.sql"                   \
    --include "Joins.sql"                  \
    --include "Subqueries.sql"             \
    --include "Sets.sql"                   \
    --include "Aggregation.sql"            \
    --include "Insert.sql"                 \
    --include "Update.sql"                 \
    --include "Delete.sql"                 \
    --exclude "*"                          \
    ../../examples/sql/ examples
	@rsync -r -t -u -v --delete            \
    --include "Stack1.uml"                 \
    --include "Stack2.uml"                 \
    --include "SAC.uml"                    \
    --include "StrategyPattern1.uml"       \
    --include "StrategyPattern2.uml"       \
    --include "StrategyPattern3.uml"       \
    --include "StrategyPattern4.uml"       \
    --include "StrategyPattern5.uml"       \
    --include "StrategyPattern6.uml"       \
    --exclude "*"                          \
    ../../examples/uml/ examples
	@rsync -r -t -u -v --delete            \
    --include "StrategyPattern1.java"      \
    --include "StrategyPattern2.java"      \
    --include "StrategyPattern3.java"      \
    --include "StrategyPattern4.java"      \
    --include "StrategyPattern5.java"      \
    --include "StrategyPattern6.java"      \
    --include "MethodOverriding1.java"     \
    --include "DynamicBinding.java"        \
    --include "SingletonPattern1.java"     \
    --include "SingletonPattern2.java"     \
    --include "MethodOverriding2.java"     \
    --include "StrategyPattern7.java"      \
    --include "Reflection.java"            \
    --include "StrategyPattern8.java"      \
    --include "StrategyPattern9.java"      \
    --include "StrategyPattern10.java"     \
    --exclude "*"                          \
    ../../examples/java/ examples
	@rsync -r -t -u -v --delete            \
    --include "Collatz.py"                 \
    --include "RunCollatz.py"              \
    --include "RunCollatz.in"              \
    --include "RunCollatz.out"             \
    --include "TestCollatz.py"             \
    --include "TestCollatz.out"            \
    --exclude "*"                          \
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
