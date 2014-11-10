#-------------------------------------------------------------------------------
# Name:        word-finder
# Purpose:
#
# Author:      Rushi Shah
#
# Created:     09/11/2014
# Copyright:   (c) Rushi Shah 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re
sentences = []
file = ""
lines = ""
paragraphs = []
chapters = []
markers = []

def delineate():
    global file, lines, chapters, paragraphs
    file = open("sl.txt")
    lines = file.readlines()
    currParagraph = []
    for i in range(len(lines)):
        if(lines[i] == "\n"):
            paragraphs.append(currParagraph)
            currParagraph = []
        else:
            currParagraph.append(lines[i])
    currChapter = []
    for paragraph in paragraphs:
        if not paragraph:
            chapters.append(currChapter)
            currChapter = []
        else:
            currChapter.append(paragraph)
    #array cleanup
    chapters = [chapter for chapter in chapters if chapter]
    paragraphs = [paragraph for paragraph in paragraphs if paragraph]

def findWords(targets = ['scarlet', 'letter']):
    global markers
    for c in range(len(chapters)):
        for p in range(len(chapters[c])):
            for l in range(len(chapters[c][p])):
                words = chapters[c][p][l].split(" ")
                for word in words:
                    for target in targets:
                        if(word == target):
                            markers.append([word, c, p, l])
    markers.sort(key = lambda marker: marker[0])
    return markers



delineate()
targets = ['steps', 'door', 'scaffold', 'gold', 'water', 'hair']
markers = findWords(targets)
