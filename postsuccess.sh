#!/bin/bash
git status
echo "github token is this : $GITHUB_TOKEN"

git add .
git commit -m "Travis build : $TRAVIS_BUILD_NUMBER [$(date)]"
git remote rm origin
git remote add origin https://codernavi18:$GITHUB_TOKEN@github.com/codernavi18/codernavi18.github.io.git > /dev/null 2>&1
git push origin master --quiet
exit 0
