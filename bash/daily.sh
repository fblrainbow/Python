#!/bin/bash
dailytime=`date -I`
ansible-playbook ~/桌面/ansible/privelist.yml>>/home/jbkj/桌面/ansible/$dailytime.txt
