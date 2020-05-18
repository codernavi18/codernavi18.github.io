#!/bin/bash

set -e

git status
echo "github token is this : $GITHUB_TOKEN"

git add .
#add skip-ci else this will again trigger a travis build creating an infinite loop
git commit -m "Travis update: $dateAndMonth (Build $TRAVIS_BUILD_NUMBER)" -m "[skip ci]"
git remote rm origin
git remote add origin https://codernavi18:$GITHUB_TOKEN@github.com/codernavi18/codernavi18.github.io.git > /dev/null 2>&1
git push origin master --quiet
exit 0
