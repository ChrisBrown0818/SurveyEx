from flask import Flask, request, render_template, redirect, flash, session



RESPONSES_KEY = "responses"

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False






@app.route('/')
def show_survey_start():


    return render_template('survey_start.html')


@app.route('/begin', methods = ['POST'])
def create_list():
    """create  and clear empty response list and redirect to survey Ques."""

    session[RESPONSES_KEY] = []

    return redirect('questions.html')


@app.route('/answer', method=['POST'])
def handle_question():

    choice = request.form['answer']

    responses = session[RESPONSES_KEY]
    responses.append(choice)
    session[RESPONSES_KEY] = responses

    if(len(responses) == len(survey.questions)):
        return redirect('/complete')
    
    else:
        return redirect(f'/questions/{(len(responses))}')


@app.route('/questions/<int:qid>')
def show_question(qid):
    """show question"""
responses = session.get[RESPONSES_KEY]

if(responses is None):
    return redirect('/')

if(len(responses) == len(survey.questions)):
        return redirect('/complete')

if(len(responses) != qid):
    flash(f"Wrong page, please do questions in order")
    return redirect(f"/questions/{len(responses)}")

    question = survey.questions[qid]
    # take them to the route above with the question.
    return render_template("question.html", question_num = qid, question = question)


@app.route('/complete')
def show_complete():
    """end survey page"""

    return render_template("completion.html")




