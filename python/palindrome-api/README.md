# Palindrome API

## Description

* App that return if a word is palindrome

## Getting Started

### Building image and pushing to docker hub

* docker image build --platform=linux/amd64 -t  palindrome-api-amd .
* docker tag palindrome-api-amd lcavanzo/api-palindrome:v1
* docker push lcavanzo/api-palindrome:v1

### Dependencies

* Container environemnt

### Instaling Docker on rhel7

* sudo subscription-manager repos --enable=rhel-7-server-rpms \
  --enable=rhel-7-server-extras-rpms \
  --enable=rhel-7-server-optional-rpms

* sudo yum install -y docker device-mapper-libs device-mapper-event-libs

* sudo systemctl enable --now docker.service

### Running container

* docker run -d --name palindrome -p 80:5000 lcavanzo/api-palindrome:v1

### Testing
* instance-ip:port/palindrome
* 10.10.10.10:80/anitalavalatina
