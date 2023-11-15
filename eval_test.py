import pytest

from eval import check, eval, parse, read

def test_parse():
    assert parse("") == ""
    assert parse(" ") == ""
    assert parse(")))((   ))") == ")))(())"   

def test_check():
    assert check("") == True
    assert check("       ") == True
    assert check("((()))")== True
   # assert check("(((((A)))))") == SyntaxError
    # assert check("(😄(((()))))") == SyntaxError

def test_read():
    assert read("   ") == ""
    assert read("(((   )))") == "((()))"
    

def test_eval():

    assert eval('') == 0
    assert eval('(((()') == 3
    assert eval('))(') == -1