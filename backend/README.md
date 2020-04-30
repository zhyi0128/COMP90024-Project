# flask_docker

## git pull from master into the development branch

```bash
git checkout dmgr2      # gets you "on branch dmgr2"
git fetch origin        # gets you up to date with origin
git merge origin/master
```

## How to use

`sudo docker-compose build`

`sudo docker-compose up`

# Prerequisites

## 1. Install Docker on Ubuntu

`curl -fsSL https://get.docker.com -o get-docker.sh`

`sh get-docker.sh`

## 2. Install docker-compose

[official site](https://docs.docker.com/compose/install/)

1. Run this command to download the current stable release of Docker Compose:

`sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`

> To install a different version of Compose, substitute 1.25.5 with the version of Compose you want to use.

2. Apply executable permissions to the binary:

`sudo chmod +x /usr/local/bin/docker-compose`

3. Test the installation

`docker-compose --version`

[Docker-Compose Reference](https://docs.docker.com/compose/compose-file/#command)
