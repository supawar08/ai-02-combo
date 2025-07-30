from flask import Flask, render_template, request
import pickle

# load the model
with open("./adv-model.pkl", "rb") as file:
    model = pickle.load(file)

# create flask server application
app = Flask(__name__)

# add routes

@app.route("/", methods=["GET"])
def root():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict_sales():
    # get input sent by the client
    tv = float(request.form.get("tv"))
    radio = float(request.form.get("radio"))
    # print(f"tv = {tv}, type = {type(tv)}")
    # print(f"radio = {radio}, type = {type(radio)}")

    # get the sales prediction
    prediction = model.predict([[tv, radio]])
    print(prediction)

    return render_template("prediction.html", 
                tv=tv, radio=radio, sales=f"{prediction[0]:.2f}")



# run the application
app.run(port=4000, host="0.0.0.0", debug=True)