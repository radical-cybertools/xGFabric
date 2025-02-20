#!/bin/bash

sudo sh -c "wget -O - https://dl.openfoam.org/gpg.key > /etc/apt/trusted.gpg.d/openfoam.asc"
sudo add-apt-repository http://dl.openfoam.org/ubuntu
sudo add-apt-repository "http://dl.openfoam.org/ubuntu dev"
sudo apt-get update
sudo apt-get -y install openfoam-dev


source /opt/openfoam-dev/etc/bashrc
foamVersion
