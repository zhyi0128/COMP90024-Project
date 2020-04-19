# Docker

## Pull MySQL as an example

`docker pull mysql`

`docker image inspect mysql`

`docker container run -d --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=True mysql`

`docker volume ls`



## named volumes

`docker container run -d --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=True -v mysql-db:/var/lib/mysql mysql`

制定volumes的名字

## Persistent Data: Bind Mounting

* Mapping a host file or directory to a container file or directory
* Two locations pointing to the same files

`docker container run -d --name nginx22 -p 8080:80 -v $(pwd):/usr/share/nginx/test nginx`

`docker container exec -it nginx22 bash`

在本地修改就能修改容器当中的文件


# Git

## Branch merge from master
`git checkout cutome_branch && git rebase master`

This will update custom_branch with changes from master branch.

Don't forget to make sure master is up to date first. git pull

This is also possible with git checkout custom_branch && git merge master

