#!/bin/bash

cat $1 | grep avg | awk -v file=$(basename $1) '{ acc += $4; recall += $5; f1 += $6; count++ } END { print file "\tacc: " acc/count "\trecall: " recall/count "\tF1: " f1/count }'
