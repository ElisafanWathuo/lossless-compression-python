import lossless_compress as lc

textData = "Ask not what your country can do for you ask what you can do for your country"#input("Please enter your sentence: ")
wordToFind = "country"#input("Please enter the word you wish to find: ")

indexes = lc.indexesInSentence(textData, wordToFind)
wordCount = lc.timesInSentence(textData, wordToFind)

indexesStr = str(indexes)
indexesStr = indexesStr[1:len(indexesStr)-1]

print("The sentence contains \"{0}\" {1} time(s) at the indexes {2}".format(wordToFind, wordCount, indexesStr))

lc.compessToFile(textData, "./compressed.txt")

print ("The compressed text has been written to: compressed.txt")

decompressed = lc.decompressFile("./compressed.txt")

fo = open("./decompressed.txt", "w+")
fo.write(decompressed)
fo.close()

print ("The decompressed text has been written to: decompressed.txt")
