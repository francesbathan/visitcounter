from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'lilly counter'


@app.route('/', methods=['GET'])
def start_counter():
    # session['times'] = 0
    if 'times' in session:
        session['times'] += 1
    else:
        session['times'] = 0
    return render_template('session-index.html', times=session['times'])


@app.route('/two', methods=['GET'])
def plus2_counter():
    # session['times'] = 0
    if 'times' in session:
        session['times'] += 2
    else:
        session['times'] = 0
    return render_template('session-index.html', times=session['times'])


@app.route("/destroy_session")
def reset():
    session.clear()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
