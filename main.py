from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


#URL to the page
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            body{{
                background-color: #5CD2E8;
            }}
            header h1{{
                text-align: center;
                font-family: arial;
            }}
            
        </style>
    </head>
    <body>
        <header>
            <h1>Web Caesar</h1>
        </header>
      <!-- create your form here -->
      <form method='post'>
        <label>
            Rotate by:
            <input type='text' name='rot' value='0' / >
        </label>
        <textarea type='text' name='text'>{0}</textarea>
        <input type='submit' value='Encrypt Message!' />

      </form>
      
    </body>
</html>

"""
@app.route('/', methods=['POST'])
# Process the from
def encrypt():
    rotate_amount = request.form['rot']
    message = request.form['text']

    encrypted_message = rotate_string(str(message), int(rotate_amount))

    return form.format(encrypted_message)

@app.route('/')
# displays message on the screen 
def index():
    return form.format('')
app.run()