#Chai. Copyright Shadewalker3652 (c)2024. All rights reserved. No part of this program or any of the files it uses may be redistributed, however it can be edited for personal use on the Github Respitory.

##########
#TOKENS
##########
lexer_char_num = -1
lexer_current_cha = ""
tokens = []

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
            Token.lexer_advance()
            

    def tokenize(fn,ln):
        global tokens
        while lexer_current_cha != None:
            if lexer_current_cha in ' \t':
                tokens.append(f"{TT_INT}:{lexer_current_cha}")
                Token.lexer_advance()
            elif lexer_current_cha in "1234567890":
                print(Token.make_number())
                Token.lexer_advance()
            elif lexer_current_cha == "+":
                Token.lexer_advance()
            elif lexer_current_cha == "-":
                Token.lexer_advance()
            elif lexer_current_cha == "*":
                Token.lexer_advance()
            elif lexer_current_cha == "/":
                Token.lexer_advance()
            elif lexer_current_cha == "(":
                Token.lexer_advance()
            elif lexer_current_cha == ")":
                Token.lexer_advance()
            elif lexer_current_cha == " ":
                pass
                #Token.lexer_advance()
            else:
                Token.lexer_advance()
                Errors.BadCharacter(ln,fn)



        return tokens, None
    
    def make_number():
        num_str = ''
        dot_count = 0

        while lexer_current_cha in "1234567890":
            if lexer_current_cha   == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += lexer_current_cha

            Token.lexer_advance()

    def lexer_advance():
        global lexer_char_num, lexer_current_cha, text

        lexer_char_num = lexer_char_num + 1

        if  lexer_char_num < len(text):
            lexer_current_cha = text[lexer_char_num]
            print(lexer_current_cha)
            if lexer_current_cha in "+-*/()":
                Token.lexer_advance()
        #else:
           # lexer_char_num = 0
            #lexer_current_cha = None

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
    def __init__(filen,ln):
        global fn
        fn = filen
        Token.init()
        Token.tokenize(filen,ln)
        print(tokens)









##########
#RUN
##########
        
while True:
  text = input("Chai > ")
  Lexer.__init__("File",1)