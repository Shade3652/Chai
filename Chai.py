#Chai. Copyright Shadewalker3652 (c)2024. All rights reserved. No part of this program or any of the files it uses may be redistributed, however it can be edited for personal use on the Github Respitory.

##########
#TOKENS
##########
token_current_char = None
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
    def init(self,text,ln):
        token_current_char = None
        self.ln_space = -1
        self.text = text
        self.ln = 1
        self.advance()

    def advance(self):
        self.ln_space =+ 1
        token_current_char = self.text[self.ln_space]
        if self.ln_space > len(self.text):
            self.ln =+ 1; self.ln_space = -1
            

    def tokenize(self,text,fn,ln):
        while token_current_char != None:
            if token_current_char in ' \t':
                self.advance()
            elif token_current_char in "1234567890":
                tokens.append(self.make_number())
            elif token_current_char == "+":
                tokens.append(TT_PLUS)
                self.advance()
            elif token_current_char == "-":
                tokens.append(TT_MINUS)
                self.advance()
            elif token_current_char == "*":
                tokens.append(TT_MUL)
                self.advance()
            elif token_current_char == "/":
                tokens.append(TT_DIV)
                self.advance()
            elif token_current_char == "(":
                tokens.append(TT_LPAR)
                self.advance()
            elif token_current_char == ")":
                tokens.append(TT_RPAR)
                self.advance()
            elif token_current_char == " ":
                self.advance()
            else:
                self.char = self.current_char
                self.advance()
                Errors.BadCharacter(self.ln_space,fn,ln)



        return tokens, None
    
    def make_number(self):
        num_str = ''
        dot_count = 0

        while token_current_char != None and token_current_char in "1234567890.":
            if token_current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

##########
#ERRORS
##########
    
class Errors():
    class Data():
        def __init__(self,pos_start,pos_end,error_name,error_dets):
            self.pos_start = pos_start
            self.pos_end = pos_end
            self.error_name = error_name
            self.error_dets = error_dets

        def BadCharacter(ln_space,fn,ln):
            print("Error: Bad character. File " + fn + ", line " + ln + ", character" + ln_space)

##########
#LEXER
##########
            
class Lexer():
    def __init__(filen,text,ln):
        fn = filen
        text = text 
        Token.init("Token",text,ln)
        Token.tokenize(text,fn,ln)
