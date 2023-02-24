from flask import Flask, render_template
from flask_socketio import *
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("APP_SECRET_KEY")
app.config['SECRET_KEY'] = 'TESTE'

socketio = SocketIO(app, async_handlers=True)

@app.route('/discordJosh',methods=['GET', 'POST'])
def josh():
    return render_template('controladores/joshGudwin.html')



if __name__ == '__main__':
    socketio.run(app, port=5000, debug=True,allow_unsafe_werkzeug=True )
