# PyPamTesting

A PyPam Testing Repository


# Overview

This project was created as part of a nation-wide effort to process acoustic data at scale. The pypam library is a technology which processes hydrophone data.

This project aims to provide docker images for pypam process agents. 

# Purpose

To process a deployment with pypam by operating on a hydrophone-generated-wavefile-directory.

- To build the process-agent instance:

        $ sudo docker build -t pypam-testing .

- To run the process-agent instance:

        $ sudo docker run -it -v <local_path_to_wave_files>:/wave_files pypam-testing

- Eventual running command:

        $ sudo docker run -it -v <local_path_to_wave_files>:/wave_files pypam-testing --output_path /home/Documents/output --model STH600 --serial_number 53426 



