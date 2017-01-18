#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import argparse

import cpLib.conceptDB as db

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='build a random list of word')
    parser.add_argument("vocFilePath", help='voc file')
    parser.add_argument("size", help='number of word to extract')
    args = parser.parse_args()

    vocFilePath = args.vocFilePath

    d = db.DB('../data/voc/npy/wikiEn-skipgram.npy', False)
    conceptList = d.getSample(int(args.size))

    for concept in conceptList:
        print concept
