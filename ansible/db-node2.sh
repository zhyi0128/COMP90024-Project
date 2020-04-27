#!/bin/bash


curl -X POST -H "Content-Type: application/json" http://admin:project@172.26.38.189:5984/_cluster_setup -d '{"action": "enable_cluster", "bind_address":"0.0.0.0", "username": "admin", "password":"project", "port": 5984, "node_count": "3", "remote_node": "172.26.37.223", "remote_current_user": "admin", "remote_current_password": "project" }'
curl -X POST -H "Content-Type: application/json" http://admin:project@172.26.38.189:5984/_cluster_setup -d '{"action": "add_node", "host":"172.26.37.223", "port": 5984, "username": "admin", "password":"project"}'
curl -X POST -H "Content-Type: application/json" http://admin:project@172.26.38.189:5984/_cluster_setup -d '{"action": "finish_cluster"}'