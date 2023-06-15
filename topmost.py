import wordfreq
import sys
import urllib.request

def main():
    
    if(sys.argv[2].startswith("http://") or sys.argv[2].startswith("https://")):
        
        response = urllib.request.urlopen(sys.argv[2])
    
        lines = response.read().decode("utf8").splitlines()
        
        toknezidText = wordfreq.tokenize(lines)
        
        response.close()
        
    else:
        
        textFile = open(sys.argv[2],'r')
    
        toknezidText = wordfreq.tokenize(textFile)
    
        textFile.close()
    
    wordsNum = int(sys.argv[3])
    
    
    stopWordsFile = open(sys.argv[1],'r')
    
    stopWords = stopWordsFile.read()
    
    wordDict = wordfreq.countWords(toknezidText , stopWords)
    
    stopWordsFile.close()
     
    wordfreq.printTopMost(wordDict,wordsNum)
    






main()

