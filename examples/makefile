.DEFAULT_GOAL := all

FILES :=                    \
    Hello                   \
    UnitTests3              \
    Coverage1               \
    Coverage2               \
    Coverage3               \
    IsPrime1                \
    IsPrime2                \
    Exceptions              \
    Types                   \
    Operators               \
    Variables               \
    Factorial1              \
    Factorial2              \
    Reduce1                 \
    Reduce2                 \
    Iteration               \
    Comprehensions          \
    Yield                   \
    Map1                    \
    Map2                    \
    Iterables               \
    RangeIterator1          \
    RangeIterator2          \
    Range1                  \
    Range2                  \
    FunctionKeywords        \
    FunctionDefaults        \
    FunctionUnpacking       \
    FunctionTuple           \
    FunctionDict            \
    Select1                 \
    Select2                 \
    Project1                \
    Project2                \
    CrossJoin1              \
    CrossJoin2              \
    ThetaJoin1              \
    ThetaJoin2              \
    NaturalJoin1            \
    NaturalJoin2

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

.pylintrc:
	$(PYLINT) --disable=locally-disabled --reports=no --generate-rcfile > $@

%.pyx: %.py .pylintrc
	-$(MYPY)     $<
	-$(PYLINT)   $<
	-$(COVERAGE) run    --branch $<
	-$(COVERAGE) report -m

all:

clean:
	rm -f  .coverage
	rm -f  .pylintrc
	rm -rf .mypy_cache

docker:
	docker run -it -v $(PWD):/usr/cs373 -w /usr/cs373 gpdowning/gcc

run: $(FILES:=.pyx)

travis:
	make clean
	ls -al
	make run

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
