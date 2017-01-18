#!/bin/bash

rootFolder=$1

for f in $rootFolder/*.log
do
    bin/summarizeFromSkReport.sh $f
done
