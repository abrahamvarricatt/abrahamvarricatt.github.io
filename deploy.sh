#!/bin/bash
# ref: https://gist.github.com/domenic/ec8b0fc8ab45f39403dd
set -e # Exit with nonzero exit code if anything fails

function doCompile {
  nikola build
}

# Run compile script
doCompile


