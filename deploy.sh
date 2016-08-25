#!/bin/bash
# ref: https://gist.github.com/domenic/ec8b0fc8ab45f39403dd
set -e # Exit with nonzero exit code if anything fails

SOURCE_BRANCH="source-markup"
TARGET_BRANCH="master"

function doCompile {
  nikola build
}

# Pull requests and commits to other branches shouldn't try to deploy, just build to verify
if [ "$TRAVIS_PULL_REQUEST" != "false" -o "$TRAVIS_BRANCH" != "$SOURCE_BRANCH" ]; then
    echo "Skipping deploy; just doing a build."
    doCompile
    exit 0
fi

# Save some useful information
REPO=`git config remote.origin.url`
HTTPS_REPO=https://nikolabot4abrahamvarricatt:$GITHUB_API_KEY@github.com/note2self-abrahamvarricatt/note2self-abrahamvarricatt.github.io.git
SHA=`git rev-parse --verify HEAD`

# Clone the existing TARGET_BRANCH for this repo into output/
# Create a new empty branch if TARGET_BRANCH doesn't exist yet
git clone $REPO output
cd output
git checkout $TARGET_BRANCH || git checkout --orphan $TARGET_BRANCH
cd ..

# Clean out existing contents
rm -rf output/**/* || exit 0

# Run compile script
doCompile

# Setup git 
cd output
git config user.name "Travis CI"
git config user.email "Travis CI"

## If there are no changes to the compiled out (e.g. this is a README update) then just bail.
#if [ -z `git diff --exit-code` ]; then
#    echo "No changes to the output on this push; exiting."
#    exit 0
#fi

# Commit the 'changes'
# Delta will show diffs between new and old
git add --all .
git commit -m "Deploy to GitHub Pages: ${SHA}"

# push repo using HTTPS
# ref: http://stackoverflow.com/a/33125422/198660
git push -f -q $HTTPS_REPO $TARGET_BRANCH 2>&1

