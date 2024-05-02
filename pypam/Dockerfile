# syntax=docker/dockerfile:1

FROM ubuntu:22.04


LABEL authors = "Michael C Ryan - spacetime.engineer@gmail.com, michael.c.ryan@noaa.gov"
WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-setuptools \
    python3-venv \
    git \
    && apt-get clean

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pyhydrophone lifewatch-pypam




CMD [ "python3", "app.py" ]


# Docker Run Command : docker run -it --rm -p 5006:5006 pypam-testing

# Docker Build Command : docker build -t pypam-testing .

# Docker Push Command : docker push pypam-testing

# Docker Pull Command : docker pull pypam-testing
