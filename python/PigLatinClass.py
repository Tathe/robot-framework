class Piglatin:
    def __init__(self):
        self.breakLetters="aiouye"


    def translatePiglatinWord(self,wordToConvert):
        startString=""
        for i in range(0, len(wordToConvert)):
            if wordToConvert[i] in self.breakLetters:
                break
            else:
                startString = startString + wordToConvert[i]
        if (len(startString) == len(wordToConvert)):
            startString = wordToConvert + "yay"
        else:
            wordToConvert = wordToConvert[i:]
            startString = wordToConvert + startString + "ay"
        return startString

    def translate(self,lineToTranslate):
        lineToTranslate = lineToTranslate.split()
        convertedLine = ""
        for i in range(0, len(lineToTranslate)):
             convertedLine=convertedLine+ " " +self.translatePiglatinWord(lineToTranslate[i])
        print convertedLine


if __name__=='__main__':
    obj=Piglatin()
    inputLine=raw_input("Enter sentence : ")
    obj.translate(inputLine)