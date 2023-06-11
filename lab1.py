import sys

def tokenize(doc):
    
    tokinzedList=[]
    
    for line in doc:
        
        i=0
        
        while(i < len(line)):
            
            if line[i].isalpha():
                
                charLitst = []
                
                while line[i].isalpha() and i < len(line):
                    
                    charLitst.append(line[i])
                    i+=1
                    
                word = ''.join(charLitst)
                
                tokinzedList.append(word)
                
            elif line[i].isdigit():
                
                digitList=[]
                
                while line[i].isdigit() and i < len(line):
                    
                    digitList.append(line[i])
                    
                    i+=1
                    
                word = ''.join(digitList)
                
                tokinzedList.append(word)
                
            elif line[i].isspace():
                
                word = line[i]
                
                tokinzedList.append(word)
                
            else:
                
                word = line[i]
                
                tokinzedList.append(word)
                
            i+=1
        
    return tokinzedList



def main():
    
    doc=['"They had 16 rolls of duct tape, 2 bags of clothes pins,',
        '130 hampsters from the cancer labs down the hall, and',
        'at least 500 pounds of grape jello and unknown amounts of chopped liver"',
        'said the source on a recent Geraldo interview.']
 
    print(tokenize(doc))
    

main()
