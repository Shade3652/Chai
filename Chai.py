#Chai. Copyright Shadewalker3652 (c)2024. All rights reserved. No part of this program or any of the files it uses may be redistributed, however it can be edited for personal use on the Github Respitory.

##########
#TOKENS
##########
lexer_current_char = None
tokens = []
lexer_char_num = 0
global lexer_line
lexer_line = 0

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
            lexer_ln = 0
            Token.lexer_advance()
            

    def tokenize(fn,ln):
        while lexer_current_char != None:
            if lexer_current_char in ' \t':
                Token.lexer_advance()
            elif lexer_current_char in "1234567890":
                tokens.append(Token.make_number())
            elif lexer_current_char == "+":
                tokens.append(TT_PLUS)
                Token.lexer_advance()
            elif lexer_current_char == "-":
                tokens.append(TT_MINUS)
                Token.lexer_advance()
            elif lexer_current_char == "*":
                tokens.append(TT_MUL)
                Token.lexer_advance()
            elif lexer_current_char == "/":
                tokens.append(TT_DIV)
                Token.lexer_advance()
            elif lexer_current_char == "(":
                tokens.append(TT_LPAR)
                Token.lexer_advance()
            elif lexer_current_char == ")":
                tokens.append(TT_RPAR)
                Token.lexer_advance()
            elif lexer_current_char == " ":
                Token.lexer_advance()
            else:
                lexer_char = lexer_current_char  
                Token.lexer_advance()
                Errors.BadCharacter(ln,fn)



        return tokens, None
    
    def make_number(self):
        num_str = ''
        dot_count = 0

        while lexer_current_char in "1234567890.":
            if lexer_current_char   == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += lexer_current_char

            Token.lexer_advance()

    def lexer_advance():
        if lexer_line > len(text):
            lexer_ln += 1; lexer_char_num = -1; lexer_current_char = None
        else:
            lexer_current_char += 1
            lexer_current_char = text[lexer_char_num]


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
        Token.tokenize(text,fn,ln)
