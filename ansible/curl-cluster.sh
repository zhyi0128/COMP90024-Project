#!/bin/bash

# BEGIN ANSIBLE MANAGED BLOCK
curl -X POST -H "Content-Type:application/json" http://admin:happy@172.26.134.54:5984/_cluster_setup -d '{"action":"enable_cluster", "bind_address":"0.0.0.0", "username":"admin", "password":"happy", "port":5984, "node_count":"3", "remote_node":"172.26.131.230", "remote_current_user":"admin", "remote_current_password":"happy" }'
curl -X POST -H "Content-Type:application/json" http://admin:happy@172.26.134.54:5984/_cluster_setup -d '{"action":"add_node", "host":"172.26.131.230", "port":5984, "username":"admin", "password":"happy"}'
curl -X POST -H "Content-Type:application/json" http://admin:happy@172.26.134.54:5984/_cluster_setup -d '{"action":"enable_cluster", "bind_address":"0.0.0.0", "username":"admin", "password":"happy", "port":5984, "node_count":"3", "remote_node":"172.26.133.121", "remote_current_user":"admin", "remote_current_password":"happy" }'
curl -X POST -H "Content-Type:application/json" http://admin:happy@172.26.134.54:5984/_cluster_setup -d '{"action":"add_node", "host":"172.26.133.121", "port":5984, "username":"admin", "password":"happy"}'
curl -X POST -H "Content-Type:application/json" http://admin:happy@172.26.134.54:5984/_cluster_setup -d '{"action":"finish_cluster"}'
# END ANSIBLE MANAGED BLOCK
