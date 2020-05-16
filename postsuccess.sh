#!/bin/bash
git status

git add .
git commit -m "Travis build : $TRAVIS_BUILD_NUMBER [$(date)]"
git remote rm origin
git remote add origin https://codernavi18:ccf1957fea6882e10758ba32113232d4252bc5db@github.com/codernavi18/codernavi18.github.io.git > /dev/null 2>&1
git push origin master --quiet
exit 0
