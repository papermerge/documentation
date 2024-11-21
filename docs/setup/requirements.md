# Requirements

## Software

{{ extra.project }} is designed to run on Linux compatible system.

You need to have docker installed, or docker runtime, as {{ extra.project }} is shipped as docker image.
All docker images are stored on <a href="https://hub.docker.com/u/papermerge" class="external-link" target="_blank">docker hub</a>.

Make sure that you have docker available:

        $ docker --version
        Docker version 26.1.3, build b72abbb


## Hardware

It depends on the setup. The hardware requiremnets for k8s cluster setup
will be very different than for lab deployment on one single VM.
It also deplends if you intend to use OCR features.

An absolute minimul requirement, for running just web app, would be 1GB of RAM memory.
In k8s deployment - {{ extra.project }} helm chart describes minimum resource requirement
for each individual web service. See k8s deployment setups for details.
