#!/bin/bash
git status

git add .
git commit -m "Travis build : $TRAVIS_BUILD_NUMBER [$(date)]"
git remote rm origin
git remote add origin https://codernavi18:668e42c4779974bb4141f03e9118647fba0d098d@github.com/codernavi18/codernavi18.github.io.git > /dev/null 2>&1
git push origin master --quiet
exit 0
