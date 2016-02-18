def timesInSentence(sentence, word):
    """Returns how times a word appears in a sentence"""
    return sentence.split(" ").count(word)

def indexesInSentence(sentence, word):
    """Returns the positions of a word in a sentence"""
    wordsArray = sentence.upper().split(" ")
    word = word.upper()
    indexes = []
    for i, w in enumerate(wordsArray):
        if w == word:
            indexes.append(i + 1)
    return indexes

def getCompressionDict(sentence, caseSensitive):
    """Returns a dictionary containing keys needed for lossy compression of the text"""
    if (not caseSensitive):
        sentence = sentence.upper()
    words = {}
    for i, w in enumerate(sentence.split(" ")):
        if not (w in words):
            words[w] = i+1
    return words

def getCompressedConstruction(sentence, caseSensitive):
    """Returns an array of numbers which correlate to a value that represent a letter"""
    if (not caseSensitive):
        sentence = sentence.upper()
    values = getCompressionDict(sentence, caseSensitive)
    compressedSentence = []

    for w in sentence.split(" "):
        compressedSentence.append(values[w])

    return compressedSentence

def lossless_compress(sentence):
    """Returns a tuple of value keys with a sentce compressed using those values"""
    valueMap = getCompressionDict(sentence, True)
    dataMap = getCompressedConstruction(sentence, True)

    return valueMap, dataMap

def compressToFile (sentence, outputPath):
    output = open(outputPath, "w+")
    valueMap, dataMap = lossless_compress(sentence)

    valueMapStr = str(valueMap)
    valueMapStr = valueMapStr[1:len(valueMapStr)-1].replace(", ", ",")

    dataMapStr = str(dataMap)
    dataMapStr = dataMapStr[1:len(dataMapStr)-1].replace(", ", ",")
    output.write(valueMapStr + '\n')
    output.write(dataMapStr)
    output.close()

def compressFromFile (filePath):
    fo = open(filePath, "r+")
    data = fo.read()
    fo.close()
    return lossless_compress(data)

def compressFromFileToFile(inputPath, outputPath):
    fo = open(inputPath, "r+")
    data = fo.read()
    print(data)
    fo.close()
    compressToFile(data, outputPath)

def decompress(valueMapStr, dataMapStr):
    valueMap = {}
    valuesStr = valueMapStr.split(", ")
    data = []

    for keyValuePairStr in valuesStr:
        keyValue = keyValuePairStr.split(": ")
        value = keyValue[0][1:len(keyValue[0])-1]
        key = int(keyValue[1])
        valueMap[key] = value

    output = ""

    for i, d in enumerate(dataMapStr.split(", ")):
        space = "" if i == len(dataMapStr.split(", ")) - 1 else " "
        output += valueMap[int(d)] + space

    return output

def decompressFromFile (filePath):
    fo = open(filePath, "r+")
    valueMapStr = fo.readline()
    dataMapStr = fo.readline()
    fo.close()

    return decompress(valueMapStr, dataMapStr)

def decompressToFile(valueMapStr, dataMapStr, filePath):
    fo = open(filePath, "w+")
    fo.write(decompress(valueMapStr, dataMapStr))
    fo.close()

def decompressToFileFromFile(inputPath, outputPath):
    fo = open(outputPath, "w+")
    fo.write(decompressFromFile(inputPath))
    fo.close()
