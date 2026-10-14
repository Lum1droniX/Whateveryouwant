with open("Week9Lab/TextFile.txt", "r") as File:
    FileContents = File.read()
    print(FileContents)

with open("Week9Lab/TextFile.txt", "a") as File:
    File.write("\n")
    File.write("\n")

with open("Week9Lab/TextFile.txt", "r") as File:
    AppendedFile = File.read()
    print(AppendedFile)