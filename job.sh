#!/bin/bash
#enter the scrapy directory
pushd rankings

#run the spiders
scrapy crawl codechef -t json -o codechef.json
scrapy crawl codeforces -t json -o codeforces.json
scrapy crawl leetcode -t json -o leetcode.json
scrapy crawl atcoder -t json -o atcoder.json
scrapy crawl uva -t json -o uva.json

echo "Done with all the scraping"
ls

git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"
git checkout master

#replace the new files (if any) with the older ones
mv codechef.json ../codechef.json
mv codeforces.json ../codeforces.json
mv leetcode.json ../leetcode.json
mv atcoder.json ../atcoder.json
mv uva.json ../uva.json
