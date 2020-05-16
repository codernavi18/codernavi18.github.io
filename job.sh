#!/bin/bash
#enter the scrapy directory
pushd rankings

#run the spiders
scrapy crawl codechef -t json -o codechef.json.tmp
scrapy crawl codeforces -t json -o codeforces.json.tmp
scrapy crawl leetcode -t json -o leetcode.json.tmp
scrapy crawl atcoder -t json -o atcoder.json.tmp
scrapy crawl uva -t json -o uva.json.tmp

echo "Done with all the scraping"
ls

git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis CI"
git checkout master

#replace the new files (if any) with the older ones
mv codechef.json.tmp codechef.json
mv codeforces.json.tmp codeforces.json
mv leetcode.json.tmp leetcode.json
mv atcoder.json.tmp atcoder.json
mv uva.json.tmp uva.json
