import sys


    
def tokenize(doc):
    
    tokenizedList=[]
    
    for row in doc:
        
        row=row.rstrip()
        
        i=0
        
        while(i < len(row)) :
            
            if row[i].isalpha() :
                
                charLitst = []
                
                while  i < len(row) and row[i].isalpha() :
                    
                    charLitst.append(row[i])
                    
                    i+=1
                    
                word = ''.join(charLitst)
                word = word.lower()
                
                tokenizedList.append(word)
                
            elif row[i].isdigit():
                
                digitList=[]
                
                while  i < len(row) and row[i].isdigit() :
                    
                    digitList.append(row[i])
                    
                    i+=1
                    
                word = ''.join(digitList)
                
                tokenizedList.append(word)
                
            elif row[i].isspace():
                
                i+=1
                
            else:
                
                word = row[i]
                
                tokenizedList.append(word)
                
                i+=1
        
    return tokenizedList


def countWords(words : list, stopWords : list) -> dict:
    
    dictionary = {}
    
    for word in words:
    
        if word not in stopWords:
            
            if word in dictionary:
                
                dictionary[word] += 1
                
            else:
                
                dictionary[word]=1
                
    return dictionary
                

def readStopWord():
    
    path = './eng_stopwords.txt'
    
    file = open(path,'r') 
    
    fileContent = file.read()
    
    return fileContent


def printTopMost(dictionary : dict[str,int] , n : int) -> None :
    
     i = 0
     
     sortedDcit = dict(sorted(dictionary.items(), key = lambda x:-x[1] ))
     
     for word,freq in sortedDcit.items():
         
         if i == n:
             
             break
         
         else:
             
             print(word.ljust(20) + str(freq).rjust(5))
             
             i+=1


""" def main():
    
    lines = ['"They had 16 rolls of duct tape, 2 bags of clothes pins',
             ',130 hampsters from the cancer labs down the hall, and',
             'at least 500 pounds of grape jello and unknown amounts of chopped liver"',
             'said the source on a recent Geraldo interview.']
    
   # print(tokenize(lines))
    
    stopWords = readStopWord()
    
    stringToCount = ['it','is','a','book','and','a','second','book','cover']
    
    wordCount = countWords(stringToCount,stopWords)
    
    #print(wordCount)
    
    printTopMost({'text': 9, 'word': 30, 'fiction': 6, 'count': 11, 'counting': 7, 'novel': 6},3)
    
    
    
    
main()
 """
