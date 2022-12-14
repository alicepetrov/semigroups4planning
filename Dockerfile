
FROM aiplanning/planutils:latest

# Update the apt package manager
RUN apt-get update

# Install GAP
RUN yes | apt-get install build-essential autoconf libtool libgmp-dev libreadline-dev zlib1g-dev

ENV GAP_VERSION 4.12.1

RUN mkdir -p /home/gap/inst/ \
    && cd /home/gap/inst/ \
    && wget https://github.com/gap-system/gap/releases/download/v${GAP_VERSION}/gap-${GAP_VERSION}.tar.gz \
    && tar xzf gap-${GAP_VERSION}.tar.gz \
    && rm gap-${GAP_VERSION}.tar.gz \
    && cd gap-${GAP_VERSION} \
    && ./configure \
    && make \
    && cp bin/gap.sh bin/gap \
    && cd pkg \
    && ../bin/BuildPackages.sh

# Install and configure JupyterKernel for GAP
RUN yes | pip3 install notebook
RUN yes | pip3 install jupyterlab
RUN git clone https://github.com/gap-packages/JupyterKernel.git /JupyterKernel \
    && cd /JupyterKernel \
    && pip3 install .

RUN jupyter serverextension enable --py jupyterlab --user

ENV PATH /home/gap/inst/gap-${GAP_VERSION}/pkg/JupyterKernel/bin:${PATH}
ENV JUPYTER_GAP_EXECUTABLE /home/gap/inst/gap-${GAP_VERSION}/bin/gap.sh

ENV GAP_HOME /home/gap/inst/gap-${GAP_VERSION}
ENV PATH ${GAP_HOME}/bin:${PATH}

# Install packages
RUN yes | pip3 install networkx
RUN yes | pip3 install graphviz
RUN yes | pip3 install pydot
RUN yes | pip3 install numpy
RUN yes | pip3 install Jinja2

# Install Seerat's macq updates, remove this once they are merged with macq
RUN git clone https://github.com/seeratparmar/macq /MACQ
WORKDIR /MACQ
RUN yes | pip3 install -e .

RUN export PYTHONIOENCODING=utf8

WORKDIR /PROJECT

CMD planutils activate