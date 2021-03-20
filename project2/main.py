from flask import Flask, render_template, request
app = Flask(__name__,template_folder='static')
import pickle


# open a file, where you stored the pickled data
file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        myDict = request.form
        fev = int(myDict['Fever'])
        wn = int(myDict['Weakness'])
        dc = int(myDict['Dry Cough'])
        bd = int(myDict['Breathing Difficulty'])
        st = int(myDict['Sore Throat'])
        pain = int(myDict['Body Pain'])
        nb = int(myDict['Nasal Block'])
        rn = int(myDict['Runny Nose'])
        dia = int(myDict['Diarrhea'])
        age = int(myDict['Age'])
        gender = int(myDict['Gender'])
        inputFeatures = [fev,wn,dc,bd,st,pain,nb,rn,dia,age,gender]
        infProb =clf.predict_proba([inputFeatures])[0][1]
        print(infProb)
        return render_template('show.html', inf=round(infProb*100,3))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)