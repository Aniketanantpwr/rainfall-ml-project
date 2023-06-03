from flask import Flask, render_template, request
import pickle


with open("random_forest_model_2.pkl",'rb') as f:
    model = pickle.load(f)
app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello, World!'

@app.route('submit',methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        Location = request.form["location"]
        Date = request.form["date"]
        mintemp = float(request.form["mintemp"])
        maxtemp = float(request.form["maxtemp"])
        Rainfall = float(request.form["Rainfall"])
        Evaporation = float(request.form["Evaporation"])
        Sunshine = float(request.form["Sunshine"])
        WindGuestSpeed = float(request.form["WindGuestSpeed"])
        WindSpeed9am = float(request.form["WindSpeed9am"])
        WindSpeed3am = float(request.form["WindSpeed3am"])
        Humidity9am = float(request.form["Humidity9am"])
        Humidity3am = float(request.form["Humidity3am"])
        Pressure9am = float(request.form["Pressure9am"])
        Pressure3am = float(request.form["Pressure3am"])
        Cloud9am = float(request.form["Cloud9am"])
        Cloud3am = float(request.form["Cloud3am"])
        Temperature9am = float(request.form["Temperature9am"])
        Temperature3am = float(request.form["Temperature3am"])
        raintoday = request.form["raintoday"]
        if raintoday == "Yes":
            raintoday = 1
        elif raintoday == "No":
            raintoday = 0
        
#   single_obs = [[7.4,25.1,0.0,4.8,8.4,44.0,4.0,22.0,44.0,25.0,1010.6,1007.8,5.0,5.0,17.2,24.3,0.0]]
    single_obs = [[mintemp,maxtemp,Rainfall,Evaporation,Sunshine,WindGuestSpeed,WindSpeed9am,WindSpeed3am,
              Humidity9am,Humidity3am,Pressure9am,Pressure3am,Cloud9am,Cloud3am,
              Temperature9am,Temperature3am,raintoday]]
    temp = model.predict(single_obs)
    if temp[0] == 1:
        return render_template("rainy.html", location = Location, date = Date)
    elif temp[0] == 0:
        return render_template("sunny.html",location = Location, date = Date)
        
        









