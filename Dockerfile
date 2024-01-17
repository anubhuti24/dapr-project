FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

RUN wget -q https://raw.githubusercontent.com/dapr/cli/master/install/install.sh -O - | /bin/bash

# Install daprd
ARG DAPR_BUILD_DIR
COPY $DAPR_BUILD_DIR /opt/dapr
ENV PATH="/opt/dapr/:${PATH}"
RUN dapr init --slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /dapr-project

#Set poetry version
ENV POETRY_VERSION=1.7.1

#Install poetry
RUN pip install "poetry==$POETRY_VERSION"

# Install any needed packages specified in requirements.txt
RUN pip install -r /dapr-project/requirements.txt

ENTRYPOINT ["dapr"]

# Multo file run
CMD ["dapr", "run", "-f", "."]

