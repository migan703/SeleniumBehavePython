from behave import *
from features.steps.register import *
from features.steps.logIn import *

@given("I am in Facebook page")
def step_impl(context):
    context.execute_steps('''Given Navigate into facebook page''') # funciona si coloco alguna de las palabras reservadas (given,when,then)

@when("I create a new user for a woman")
def step_impl(context):
    context.execute_steps('''
    When Fill all required data woman
    When Click singUp button
    ''')

@when("I create a new user for a man")
def step_impl(context):
    context.execute_steps('''
    When Fill all required data man
    When Click singUp button
    ''')

@then("I can log into Facebook as a woman")
def step_impl(context):
    context.execute_steps('''Then LogIn into facebook as a woman''')

@then("I can log into Facebook as a man")
def step_impl(context):
    context.execute_steps('''Then LogIn into facebook as a man''')