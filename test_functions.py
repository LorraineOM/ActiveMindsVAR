"""A collection of test functions for my project"""

from functions import introduction, var_info, var_scenario, active_minds_plug

def test_introduction():
    assert callable (introduction)
    name = "Ellen"
    assert isinstance(name, str)
    assert "Hello, it's nice to meet you", name == "Hello, it's nice to meet you, Ellen" 
    
def test_var_info():
    assert callable (var_info)
    response = "yes"
    assert isinstance (response, str)
    response_statement_test = "'R' stands for Refer and you're refering someone to skills and support."
    assert response_statement_test == "'R' stands for Refer and you're refering someone to skills and support."
    
def test_var_scenario():
    assert callable (var_scenario)
    response = "A"
    assert isinstance(response, str)
    else_statement = "Sorry but I don't quite understand."
    assert else_statement == "Sorry but I don't quite understand."
    
def test_active_minds_plug():
    assert callable (active_minds_plug)
    learn_more = "A"
    assert isinstance(learn_more, str)
    print_statement_test = "The mission of Active Minds is to change the conversation about mental health. "
    assert isinstance(print_statement_test, str)
    
    



                 
    