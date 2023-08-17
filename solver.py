
##using ocr we can capture the words in the text and add them to a list
words_text=["TAB","TEA","BAT","BEAT","ATE","BET","BATE"]


list_letters=["A", "B", "T" ,"E"]

##implementing the backtracking algorithm
solution=[]

def get_chars(input):
    curr=""
    for inp in input:
        curr=curr+inp[1]
    return curr
    


def backtrack(curr,length):
    word=get_chars(curr)
    
    if len(word)==length and word in words_text:
        solution.append(word)
        return

    for val in enumerate(list_letters):
        if val not in curr:
            curr.append(val)
            backtrack(curr,length)
            curr.pop()
        

backtrack([],3)



for length in range(3,len(list_letters)+1):
    backtrack([],length)

print(solution)