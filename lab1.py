import sys

def tokenize(doc):
    
    ss=[]
    
    tokenzidList=[]
    numList = []
    charList = []
    
    i=0

    for line in doc:
    # Read lines in the file
        words=line.split()
    #print(line)
    
    #print(words)
        for word in words:
        
            # Read the words in the current line and add spaces to the speical characters
            word = word.replace('"',' " ').replace(',',' , ').replace('.',' . ').replace('!',' ! ')
        
             # Convert the words to lowercase 
            word=word.lower()
            #print(word)
        
            ss.append(word)
            #print(ss)
        
            str= ss[i].split()
            #print(str)
            j=0
            if(str[0][j].isdigit()):
                
                while(j < len(str[0]) and str[0][j].isdigit()):
                        
                    numList.append(str[0][j])
                            
                    j+=1
                        
                tokenzidList.append(''.join(numList))
                numList=[]
                            
                while(j < len(str[0]) and str[0][j].isalpha()):
                        
                    charList.append(str[0][j])
                            
                    j+=1
                    
                if(len(charList) > 0):
                    
                    tokenzidList.append(''.join(charList))
            
                charList=[]
                
            else:
            
                tokenzidList.append(str[0])
                
            j=0
        
            if len(str) > 1:
            
                if(str[0][j].isdigit()):
                   
                    while(j < len(str[1]) and str[1][j].isdigit()):
                            
                        if(str[1][j].isdigit()):
                                
                            numList.append(str[1][j])
                        j+=1   
                            
                    numList.append(' ')
                        
                    tokenzidList.append(''.join(numList))
                        
                    numList = []
                        
                                
                    while(j < len(str[1]) and str[0][j].isalpha()):
                                    
                        if(str[1][j].isdigit()):
                                    
                            charList.append(str[0][j])
                        j+=1
                                    
                    charList.append(' ')
                    
                    if(len(charList) > 0 ):   
                        
                        tokenzidList.append(''.join(charList))
                                
                    charList=[]
                else:     
                    tokenzidList.append(str[1])
            
            i+=1
            
    return tokenzidList



def main():
    
    doc=['"They had 16 rolls of duct tape, 2 bags of clothes pins,',
        '130 hampsters from the cancer labs down the hall, and',
        'at least 500 pounds of grape jello and unknown amounts of chopped liver"',
        'said the source on a recent Geraldo interview.']
    
    
    print(tokenize(doc))
    

main()
