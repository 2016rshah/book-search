#-------------------------------------------------------------------------------
# Name:        word-finder
# Purpose:     Make english class easier
#
# Author:      Rushi Shah
#
# Created:     09/11/2014
# Copyright:   (c) Rushi Shah 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def delineate(): #delineates chapters, paragraphs, and lines for quick reference
    chapters = []
    paragraphs = []
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
    return chapters #structured as chapters[chapterIndex][paragraphIndex][lineIndex] and returns line as string to be split into words as needed

def findWords(targets = ['scarlet', 'letter'], chapters = []):
    markers = []
    for c in range(len(chapters)):
        for p in range(len(chapters[c])):
            for l in range(len(chapters[c][p])):
                words = chapters[c][p][l].split(" ")
                for word in words:
                    for target in targets:
                        if(word == target):
                            markers.append([word, c, p, l])
    markers.sort(key = lambda marker: marker[0]) #sort by word, switch "marker[0]" to "marker[1]" to make it chronological by chapter
    return markers


#main function, but global for console access
chapters = delineate()
targets = ['steps', 'door', 'scaffold', 'gold', 'water', 'hair'] #based on keywords you want to search
markers = findWords(targets, chapters)
#markers is an array of list items structured as [word, chapter, paragraph, line]