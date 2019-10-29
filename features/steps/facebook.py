from behave import *
from features.steps.register import *
from features.steps.logIn import *

@given("Given I am in Facebook page")
def step_impl(context):
    context.execute_steps('''Navigate into facebook page''')

@when("I create a new user for a woman")
def step_impl(context):
    context.execute_steps('''
    Fill all required data woman
    Click singUp button
    ''')

@when("I create a new user for a man")
def step_impl(context):
    context.execute_steps('''
    Fill all required data man
    Click singUp button
    ''')

@then("I can log into Facebook as a woman")
def step_impl(context):
    context.execute_steps('''LogIn into facebook as a woman''')

@then("I can log into Facebook as a man")
def step_impl(context):
    context.execute_steps('''LogIn into facebook as a man''')