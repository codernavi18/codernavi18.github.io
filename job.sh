#!/bin/bash
#enter the scrapy directory
pushd rankings

#run the spiders
scrapy crawl codechef -t json -o codechef.json.tmp
scrapy crawl codeforces -t json -o codeforces.json.tmp
scrapy crawl leetcode -t json -o leetcode.json.tmp
scrapy crawl atcoder -t json -o atcoder.json.tmp
scrapy crawl uva -t json -o uva.json.tmp

#replace the new files (if any) with the older ones
mv codechef.json.tmp codechef.json
mv codeforces.json.tmp codeforces.json
mv leetcode.json.tmp leetcode.json
mv atcoder.json.tmp atcoder.json
mv uva.json.tmp uva.json

git config user.email "travis@travis-ci.org"
git config user.name "Travis CI"
git add .
git commit -m "Travis build : $TRAVIS_BUILD_NUMBER [$(date)]"
git remote add origin-pages https://${GH_TOKEN}@github.com/codernavi18/codernavi18.github.io.git > /dev/null 2>&1
git push --quiet --set-upstream origin-pages master
exit 0
