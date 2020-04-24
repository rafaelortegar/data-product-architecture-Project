FROM ubuntu:bionic

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && echo "America/Mexico_City" > /etc/timezone && apt-get install -y tzdata

#noninteractive – You use this mode when you need zero interaction while installing or upgrading
#the system via apt. It accepts the default answer for all questions.

RUN apt-get update && apt-get install -y \
            sudo \
            nano \
            python3-dev \
            python3-pip \
            python3-setuptools \
            postgresql \
            git \
            openssl \
            gnupg \
            libpq-dev && pip3 install --upgrade pip  && pip3 install awscli --upgrade

# Creamos al usuario metro
RUN groupadd metro
RUN useradd metro -g metro -m -s /bin/bash
RUN echo 'metro ALL=(ALL:ALL) NOPASSWD:ALL' | (EDITOR='tee -a' visudo)
RUN echo 'metro:metro' | chpasswd

# Instalamos paquetes necesarios para el proyecto
RUN pip3 install pandas luigi boto3 wget pyarrow requests Psycopg2 datetime

ARG POSTGRESQL_VERSION=12
COPY $POSTGRESQL_VERSION/setup.sh /home/metro/setup.sh
RUN chmod gou+x /home/metro/setup.sh

# Instala diferentes librerias para al proyecto
USER metro
WORKDIR /home/metro/

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
ENTRYPOINT ["/home/metro/setup.sh"]
