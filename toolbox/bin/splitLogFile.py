#!/usr/bin/env python
# encoding: utf-8

import __init__

import argparse
from path import path

def extractSummaryLine(line):
    s = line.split()
    return s[0][:-4].split('_') + s[-5::2]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split a long log file into several')
    parser.add_argument('logFile', help='log file')
    args = parser.parse_args()


    logFilePath = args.logFile
    rootLogPath = path(logFilePath).parent
    with open(logFilePath, 'r') as logFile:
        subLogList = logFile.read().split('&&&&&&&&&&')
        for subLog in subLogList[1:]:
            lines = subLog.split('\n')[1:]

            with open(rootLogPath / path(lines[0] + '.log'), 'w') as subLogFile:
                subLogFile.writelines('\n'.join(lines[2:]))
