from flask import Flask , render_template , request
# import ur main file 

app = Flask ( __name__ )

@app.route ( '/' , methods=[ 'GET' , 'POST' ])
def index ():
    return render_template ( 'index.html' )

def Summarize():
    # call ur main file here
    return "done"
if __name__ == '__main__':
    app.run ( debug = True )    