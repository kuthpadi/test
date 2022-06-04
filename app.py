from flask import Flask, render_template, request 
import joblib

# create an instance of flask
app = Flask(__name__)

loaded_model = joblib.load('dib_75.pkl')


@app.route('/') #decorator 
def homepage(): 
    return render_template('homepage.html') 
    #return('Hello World')



@app.route('/predict', methods =['POST']) #decorator 
def predict(): 
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age  = request.form.get('age')
    #print(preg,plas,pres,skin,test,mass,pedi,age)
    prediction = loaded_model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])

    if prediction[0]==1:
        result = 'Diabetic'
    else :
        result = 'Not Diabetic'


    return render_template('result.html', value = result)
    


# run the application debug = True ensures, the changes that you make reflects automatically 
if __name__ == '__main__' :
    app.run(debug=True)
