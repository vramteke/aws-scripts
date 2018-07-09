# aws-scripts
Purpose
=======
These are scripts to manage and maintain AWS infrastructure.

Assumptions:
============
Project tag is used to tag all resources.If not, the script would return all resources by default.

Pre-reqs:
========

1) This has been tested in pipenv having python3 setup. 

2) Additional modules required in pipenv :
   click

How to execute the script :
===========================
$ pipenv run python awsmm.py <command> [list,start,stop] [--project=<Project tag>] 
  <command> is either instances, volumes or snapshots
  list, start or stop based off the command selected


