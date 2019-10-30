from behave import *
from features.pages.homePage import homePage
from features.utilities.Data import *

use_step_matcher("re")

@step('Navigate into facebook page') # Si cambio a given funciona.
def step_impl(context):
    homePage_ = homePage()
    homePage_.navigate()
    context.homePage_ = homePage_

@step('Fill all required data woman')
def step_impl(context):
    homePage_ = context.homePage_
    homePage_.setPrincipalUserInfo(womanName,womanLastName,womanEmail,password)
    homePage_.setBirthday(date,month,year)
    homePage_.setFemale()

@step('Fill all required data man')
def step_impl(context):
    homePage_ = context.homePage_
    homePage_.setPrincipalUserInfo(manName,manLastName,manEmail,password)
    homePage_.setBirthday(date,month,year)
    homePage_.setMale()

@step('Click singUp button')
def step_impl(context):
    homePage_ = context.homePage_
    homePage_.singUp() # Falta cerrar la página porque se están quedando abiertas 4 instancias.