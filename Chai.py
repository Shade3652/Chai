#Chai. Copyright Shadewalker3652 (c)2024. All rights reserved. No part of this program or any of the files it uses may be redistributed, however it can be edited for personal use on the Github Respitory.

##########
#TOKENS
##########
global lexer_current_cha; lexer_current_cha = None
tokens = []
lexer_char_num = 0

TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_LPAR = "LPAR"
TT_RPAR = "RPAR"

class Token():
    def init():
            lexer_advance()
            

    def tokenize(fn,ln):
        while lexer_current_cha != None:
            if lexer_current_cha in ' \t':
                lexer_advance()
            elif lexer_current_cha in "1234567890":
                tokens.append(Token.make_number())
            elif lexer_current_cha == "+":
                tokens.append(TT_PLUS)
                lexer_advance()
            elif lexer_current_cha == "-":
                tokens.append(TT_MINUS)
                lexer_advance()
            elif lexer_current_cha == "*":
                #tokens.append(TT_MUL)
                lexer_advance()
            elif lexer_current_cha == "/":
                #tokens.append(TT_DIV)
                lexer_advance()
            elif lexer_current_cha == "(":
                #tokens.append(TT_LPAR)
                lexer_advance()
            elif lexer_current_cha == ")":
                #tokens.append(TT_RPAR)
                lexer_advance()
            elif lexer_current_cha == " ":
                pass
                #lexer_advance()
            else:
                #lexer_char = lexer_current_cha  
                lexer_advance()
                Errors.BadCharacter(ln,fn)



        return tokens, None
    
    def make_number(self):
        num_str = ''
        dot_count = 0

        while lexer_current_cha in "1234567890.":
            if lexer_current_cha   == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += lexer_char_num

            lexer_advance()

def lexer_advance():
    if lexer_char_num < len(text):
        lexer_current_cha = text[lexer_char_num]
    else:
        lexer_current_cha = None

##########
#ERRORS
##########
    
class Errors():

    def BadCharacter(ln_space,ln,fn):
        print("Error: Bad character. File " + fn + ", line " + ln + ", character" + ln_space)

##########
#LEXER
##########
            
class Lexer():
    def __init__(filen,txt,ln):
        global fn
        fn = filen
        global text
        text = txt
        Token.init()
        Token.tokenize(fn,ln)
        print(tokens)









##########
#RUN
##########
        
while True:
  text = input("Chai > ")
  Lexer.__init__("File",text,1)