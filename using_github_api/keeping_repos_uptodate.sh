#!/usr/bin/env bash
REPOPTH='/home/shares/github_backup/'

for d in ${REPOPTH}*.git; do
    if [ -d ${d} ]; then
        # Will not run if no directories are available
        echo updating the repo $d
        # Go in the reop and fetch the update
        cd $d
        git fetch -p origin
        cd ..
    fi
done