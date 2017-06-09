#!/bin/bash
dailytime=`date -I`
ansible-playbook privelist.yml>>/home/jbkj/桌面/ansible/$dailytime.txt
