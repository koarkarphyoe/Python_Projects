import random


fileisNotValid=True
while fileisNotValid:
    try:
        #for 1 and 2
        file_name=input("Enter a file name:")    
        inf=open(file_name,"r")
        length_of_text=inf.read()
        print("The length of text:",len(length_of_text))
        
        #for 3 and 4
        delimiter=input("Enter a delimiter:")
        if delimiter=="":
            delimiter="\n"
        elif delimiter.isspace():
            delimiter=None
        number_of_sentence=length_of_text.split(delimiter)
        print("The number of sentences:",len(number_of_sentence))
        
        
        #for 5
        strip_sentences=[]
        for sentence in number_of_sentence:
            strip_sentences.append(sentence.strip(" "))
        valid_sentences=0
        keys=[]
        values=[]
        for sentence in strip_sentences:
            if sentence!="":
                valid_sentences+=1
                keys.append(valid_sentences)
                values.append(sentence)
        print("The number of valid sentences",valid_sentences)
        
        #for 6        
        print("*"*10,"Sentence Dictionary","*"*10)
        sentence_combined_list=list(zip(keys,values))
        sentence_dict=dict(sentence_combined_list)
        print(sentence_dict)
        
        ## for 7
        isNotDigit=True
        while isNotDigit:
            sentence_number=input("Enter a sentence number to print:")
            if sentence_number.isdigit():
                if int(sentence_number) in range(len(sentence_dict.keys())) and int(sentence_number)!=0:
                    print(sentence_dict[int(sentence_number)])
                    isNotDigit=False
                else:
                    print("Wrong sentence number,it must be between 1 and ",str(len(sentence_dict.keys())))
            else:
                print("not a number")
        ## for 8 
        print("*"*10,"A Quote for you","*"*10)
        sentence_number_list=list(sentence_dict.keys())
        random_sentence_number=random.choice(sentence_number_list)
        print(random_sentence_number," ",sentence_dict[int(random_sentence_number)])
        
        ## for 9
        notHasChar=True
        noSentence=False
        while notHasChar:
            char=input("Enter a character:")
            combined_starting_char_list=[]
            no_sentence=[]
            for sentence in values:
                char_list=list(tuple(sentence))
                if char_list[0]==char:
                    combined_starting_char_list.append(sentence)
                    notHasChar=False
                else:
                    no_sentence=True
            if no_sentence:
                print("There is no sentence starting with ",char)
                
        print("The sentences which start with A are")
        for sentence in combined_starting_char_list:
            print(sentence)
                
        
        fileisNotValid=False
        inf.close()
        break
    except IOError as err:
        print("{0}".format(err))
