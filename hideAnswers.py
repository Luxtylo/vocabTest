#!/usr/bin/env python3

"""
vocabTest - a test-making and taking program.

Copyright (C) 2013  George Bryant

This program is free software:
    you can redistribute it and/or modify it under the terms of the GNU
    General Public License as published by the Free Software Foundation,
    either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

You should have received a copy of the GNU General Public License along with
    this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import hashlib

testFile = open("tests/test.txt", "r")


def getCutOffMD5(english):
    return hashlib.md5(english).hexdigest()[:8]


def getTranslationTuple():
    wordList = list()

    lineNum = 1

    for line in testFile:
        if lineNum == 1:
            title = line
        elif lineNum == 2:
            dateString = line
        else:
            frenchWord = line.split("|")[0]
            englishWord = line.split("|")[1].lower()
            englishHash = getCutOffMD5(englishWord.encode())
            translationTuple = (frenchWord, englishHash)
            wordList.append(translationTuple)
        lineNum += 1
    return (title, dateString, wordList)

(testTitle, testDateSet, testWordList) = getTranslationTuple()
