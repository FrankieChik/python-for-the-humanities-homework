s="Barack Hussein Obama II is an American attorney and politician who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, he was the first African-American president of the United States. He previously served as a U.S. senator from Illinois from 2005 to 2008 and an Illinois state senator from 1997 to 2004."
lst_of_words=s.split("")
prefixs={"im", "un", "non", "pre", "exta", "over", "auto", "de", "anti", "in", "mis", "Africian"}
def prefix_word (prefixs, print_text):
    prefix_word=input("Enter a prefix: ")
    print(lst_of_words)
while True:
    word=input("what prefix you are goint to choose?")
    if word in prefixs:
        print(lst_of_words)
    elif not lst_of_words in prefixs:
        print("no such a word.")
    elif choice=="exit":
        break
    
