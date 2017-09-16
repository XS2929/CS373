FROM python:3.5.2

RUN apt-get update              && \
    apt-get -y install cmake    && \
    apt-get -y install graphviz && \
    apt-get -y install vim

RUN pip install --upgrade pip && \
    pip --version             && \
    pip install autopep8      && \
    pip install coverage      && \
    pip install mypy          && \
    pip install numpy         && \
    pip install pylint

CMD bash
