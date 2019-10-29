from behave import *
from features.pages.homePage import homePage
from features.utilities.Data import *

use_step_matcher("re")

@step("LogIn into facebook as a woman")
def step_impl(context):
    homePage_ = homePage()
    homePage_.navigate()
    homePage_.singIn()
    homePage_.setEmail(womanEmail)
    homePage_.setPassword(password)
    homePage_.logIn()

@step("LogIn into facebook as a man")
def step_impl(context):
    homePage_ = homePage()
    homePage_.navigate()
    homePage_.singIn()
    homePage_.setEmail(manEmail)
    homePage_.setPassword(password)
    homePage_.logIn()