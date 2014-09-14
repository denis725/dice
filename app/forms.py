from __future__ import division, print_function, absolute_import

from wtforms import Form
from wtforms import BooleanField
from wtforms import TextField

class DiceForm(Form):
    check = TextField('Check')
    dice = TextField('Dice')
    bonus = TextField('Bonus')
    strictly_greater = BooleanField('Strictly greater')
