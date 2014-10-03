from __future__ import division, print_function, absolute_import

from flask import redirect
from flask import render_template
from flask import request

from app.utils import make_check
from app.utils import rolls
from app import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    if not request.form['check'] or not request.form['dice']:
        return redirect('/index')
    outcome = False
    check = int(request.form['check'])
    dice = map(int, request.form['dice'].strip().split(' '))
    num_dice = len(dice)
    bonus = int(request.form['bonus'])
    roll_for_me = request.form.get('roll_for_me', False)
    sums, totals, percent = make_check(check, dice, bonus)
    if roll_for_me:
        outcome = rolls(dice)
        outcome_sum = sum(outcome)
        if len(outcome) > 1:
            outcome = sorted(outcome)
            outcome = ', '.join(map(str, outcome))
        else:
            outcome = str(outcome[0])
    else:
        outcome = 0
        outcome_sum = 0
    
    dice_str = "d" + ", d".join(map(str, sorted(dice)))

    return render_template('index.html',
                           dice_str=dice_str,
                           check=check,
                           required_check=check - bonus,
                           num_dice=num_dice,
                           sums=sums,
                           totals=totals, 
                           percent=percent,
                           outcome=outcome,
                           bonus=bonus,
                           outcome_sum=outcome_sum)
