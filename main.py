from flask import Flask,render_template,request
from nltk.chat.util import Chat,reflections
from pairs import pairs

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get')
def get():
    usertyped=request.args.get('msg')
    print('that is user input:',usertyped)
    chat=Chat(pairs,reflections)
    resp=chat.respond(usertyped)
    if resp==None:
        return "Sorry I don't understand that.Would you like to buy a tv or laptop?"
    return resp
    
if __name__ == "__main__":
    app.run()