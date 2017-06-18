from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True


#URL to the page
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            h1{
                text-align: center;
            }
            body{
                background-color: #539BE8;

            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <h1>Web Caesar</h1>
      <form method='post'>
        <label>
            Rotate by:
            <input type='text' name='rot' / >
        </label>
        <input type='textarea' name='text' />
        <input type='submit' value='Encrypt!' />

      </form>
      
    </body>
</html>

"""
@app.route("/")
#displays message on the screen 
def index():
    return form


app.run()