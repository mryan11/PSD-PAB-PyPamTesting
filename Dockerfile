# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# Metadata.
LABEL authors = "Michael C Ryan - spacetime.engineer@gmail.com, michael.c.ryan@noaa.gov"
WORKDIR /app


# Install any needed packages specified in requirements.txt
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

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip


# Clone the PSD-PAB-SoundScope repository.
RUN git clone https://github.com/mryan11/PSD-PAB-PyPamTesting.git

# Change directory to the recently cloned PSD-PAB-SoundScope.
RUN cd PSD-PAB-PyPamTesting

# Copy contents of PSD-PAB-SoundScope into WORKDIR
COPY . .



# Install all required libraries. Note: These version numbers were aquired from a $ pip freeze command (FYI).
RUN pip install --no-cache-dir -r requirements.txt

RUN rm -rf PSD-PAB-PyPamTesting

CMD [ "python3", "process_wave.py" ]
