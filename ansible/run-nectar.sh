#!/bin/bash

. ./unimelb-comp90024-2020-grp-38-openrc.sh; ansible-playbook -i inventory/hosts --ask-become-pass nectar.yaml