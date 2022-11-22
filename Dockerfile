
FROM aiplanning/planutils:latest

# Update the apt package manager
RUN apt-get update

# Install packages
RUN yes | pip3 install networkx
RUN yes | pip3 install graphviz
RUN yes | pip3 install libgraphviz-dev
RUN yes | pip3 install pydot
RUN yes | pip3 install pygraphviz

# Install Seerat's macq updates, remove this once they are merged with macq
RUN git clone https://github.com/seeratparmar/macq /MACQ
WORKDIR /MACQ
RUN yes | pip3 install -e .

RUN export PYTHONIOENCODING=utf8

WORKDIR /PROJECT

CMD planutils activate