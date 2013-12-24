#!/bin/bash
dev_top='/home/bray/github-projects/developers'
sep='/'
for dev in $( ls $dev_top );
	do
	for i in $( ls $dev );
		do
			echo $dev$sep$i
			cd  $dev$sep$i
			find . -name "*.java" > all_java_files.txt
			cd $dev_top
		done
	done
