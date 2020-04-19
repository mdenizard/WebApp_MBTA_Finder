from flask import Flask, render_template, request, redirect, url_for

from mbta_finder import find_stop_near

app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def find():
    # modify this function so it renders different templates for POST and GET method.
    # aka. it displays the form when the method is 'GET'; it displays the results when
    # the method is 'POST' and the data is correctly processed.
    if request.method == 'POST':
        return redirect(url_for('nearest'))
    else:
        return render_template('index.html')
        
@app.route('/nearest', methods=['POST', 'GET'])
def nearest():
    placeName = request.form['Pname']
    try: 
        nearestStop = find_stop_near(placeName)
    except IndexError:
        return render_template('errorPage.html')
    return nearestStop
        
    

@app.route('/project')
def project():
    return render_template('project.html')

if __name__ == "__main__":
    app.run(debug=True)