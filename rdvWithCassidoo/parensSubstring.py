# from issue #261 of rendezvous with cassidoo
# Given a string s consisting of various parenthesis ( and ),
# find the length of the longest valid parenthesis substring.
# 
# Example:
# 
# > parensSubstring('(()(')
# > 2
# 
# > parensSubstring(')()(()))')
# > 6

def parensSubstring(s):
    l = 0 # length of the most recent complete chain
    # ex : complete: (), (()) ; incomplete : ((), (()(
    l_p = 0 # potential additional length: length of the yet incomplete current chain 
    max = 0 # longest complete length recorded
    open = 0 # tracks opened parentheses (to mark completeness)
    
    for c in s:
        if c == '(':
            open +=1 
        elif c == ')':
            open -=1
        
        if open <0:
            open = 0
            if l > max:
                max = l
            l = 0
        elif open == 0:
            l += 1 + l_p
            l_p = 0
        else :
            l_p +=1
    
    if l_p -  open > l:
        l = l_p - open 
        
    if l >  max:
        max = l
    return max - (max % 2)

#unit tests
print(parensSubstring(')()(()))'), 6)
print(parensSubstring('()()(()(((('), 4)
print(parensSubstring('(()('), 2)
print(parensSubstring('))('), 0)
print(parensSubstring('())()()())()'), 6)
print(parensSubstring('()()((((()()()((('), 6)

# why Python? Because I'm doing it from a phone: less characters to write than in JS! 
