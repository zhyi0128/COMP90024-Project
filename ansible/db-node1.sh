#!/bin/bash

curl -X POST -H "Content-Type: application/json" http://admin:project@root.ip:5984/_cluster_setup -d '{"action": "enable_cluster", "bind_address":"0.0.0.0", "username": "admin", "password":"project", "port": 5984, "node_count": "2", "remote_node": "172.26.38.15", "remote_current_user": "admin", "remote_current_password": "project" }'
curl -X POST -H "Content-Type: application/json" http://admin:project@root.ip:5984/_cluster_setup -d '{"action": "add_node", "host":"172.26.38.15", "port": 5984, "username": "admin", "password":"peoject"}'