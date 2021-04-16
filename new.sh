#!/bin/bash

DATE=$(date +%Y%m%d)

if [ $# -eq 2 ]; then
    if [ -d content/articles/$1 ]; then
        FILENAME=${DATE}_$2.md
        echo filename: ${FILENAME}
        FILEPATH=content/articles/$1/${FILENAME}
        if [ -f ${FILEPATH} ]; then
            echo File ${FILENAME} is already existed.
            exit 1
        else
            echo "Title:" >> ${FILEPATH}
            echo ""       >> ${FILEPATH}
            echo "[TOC]"  >> ${FILEPATH}
        fi
    else
        echo Theme $1 is not existed.
        exit 1
    fi
else
    echo Error! invalid arguments.
    exit 1
fi 

exit 0
