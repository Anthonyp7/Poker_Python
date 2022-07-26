# from crypt import methods
from flask import Flask, render_template, url_for, request, session, redirect
from label import str_TOO_YOUNGER, str_ERROR_MISE, str_ERROR_MISE_ZERO
from module_tirage import premier_tirage, deuxieme_tirage
from module_gain import gain


# app = Flask(__name__)
# app.secret_key = "super_secret_key"







app = Flask(__name__)
app.secret_key = "super_secret_key"




@app.route('/')
def homepage():
    return render_template('start.html')


@app.route('/', methods=['POST'])
def check_age():
    user_age = int(request.form['age'])
    if user_age < 18:
        session['error-form'] = str_TOO_YOUNGER
        return render_template('start.html')
    else:
        session['wallet'] = request.form['wallet']
        return redirect(url_for('board'))




@app.route('/board')
def board():
    return render_template('board.html')



@app.route('/board', methods=['POST'])
def first_draw():
    session['mise'] = int(request.form['mise'])
    if int(session['mise']) > int(session['wallet']):
        session['error'] = str_ERROR_MISE
        return render_template('board.html')
    
    elif int(session['mise']) <= 0:
        session['error'] = str_ERROR_MISE_ZERO
        return render_template('board.html')


    else:
        tirage,newdeck = premier_tirage()
        session['tirage'] = tirage
        session['deck'] = newdeck
        session['wallet'] = int(session['wallet']) - int(session['mise'])
        return redirect(url_for('game'))

@app.route('/a')
def a():
    session.clear()
    return redirect(url_for('homepage'))






@app.route("/game")
def game():
    return render_template('game.html')


@app.route("/game", methods=['POST'])
def second_tirage():
    main = session['tirage']
    for carte in request.form:
        main.remove(carte)
    tirage_final = deuxieme_tirage(main, session['deck'])

    g , result = gain(tirage_final, int(session['mise']))
    session['wallet'] = session['wallet'] + g
    session['message'] = result
    session['second_tirage'] = tirage_final

    if int(session['wallet']) == 0:
        session['message'] = 'vous avez perdue'
    return redirect(url_for('gain_'))
    


@app.route('/gain')
def gain_():
    return render_template('resultat.html')
    
# @app.route('/gain', methods['POST'])
# , second_tirage = tirage_final

if __name__ == '__main__':
    app.run(debug=True)