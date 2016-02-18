import lossless_compress as lc

print("Welcome to the lossless text compressor")
fileInput = input("Please enter thr name of the file you wish to compress: ")
fileOutput = input("What should we name the output file?: ")

lc.compressFromFileToFile(fileInput, fileOutput)
