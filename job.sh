#!/bin/bash
#clone the repository
echo "Hello World"
pwd
pushd rankings
scrapy crawl codechef -t json -o codechef.json.tmp
ls
