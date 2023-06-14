import sys


    
def tokenize(doc):
    
    tokinzedList=[]
    
    for line in doc:
        
        i=0
        
        while(i < len(line)) :
            
            if line[i].isalpha() :
                
                charLitst = []
                
                while  i < len(line) and line[i].isalpha() :
                    
                    charLitst.append(line[i])
                    i+=1
                    
                word = ''.join(charLitst)
                word = word.lower()
                
                tokinzedList.append(word)
                
            elif line[i].isdigit():
                
                digitList=[]
                
                while  i < len(line) and line[i].isdigit() :
                    
                    digitList.append(line[i])
                    
                    i+=1
                    
                word = ''.join(digitList)
                
                tokinzedList.append(word)
                
            elif line[i].isspace():
                
                i+=1
                
            else:
                
                word = line[i]
                
                tokinzedList.append(word)
                
                i+=1
        
    return tokinzedList

def main():
    
    lines = ['"They had 16 rolls of duct tape, 2 bags of clothes pins',
             ',130 hampsters from the cancer labs down the hall, and',
             'at least 500 pounds of grape jello and unknown amounts of chopped liver"',
             'said the source on a recent Geraldo interview.']
    
    print(tokenize(lines))
    
    
main()

