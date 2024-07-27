from flask import Flask, render_template, request, redirect

app = Flask(__name__)
polls = {'Favorite Color': ['Red', 'Blue', 'Green']}
votes = {'Favorite Color': [0, 0, 0]}

@app.route('/')
def home():
    return render_template('index.html', polls=polls, votes=votes)

@app.route('/vote', methods=['POST'])
def vote():
    poll = request.form.get('poll')
    option = request.form.get('option')
    votes[poll][polls[poll].index(option)] += 1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
