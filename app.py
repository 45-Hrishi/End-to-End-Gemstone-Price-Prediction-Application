from flask import Flask
from flask import render_template,request,redirect,jsonify
from components.prediction import ModelPrediction
from config.configuration import ConfigurationManager

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template('form.html')
    else:
        carat = float(request.form.get("carat"))
        depth = float(request.form.get("depth"))
        table = float(request.form.get("table"))
        x = float(request.form.get("x"))
        y = float(request.form.get("y"))
        z = float(request.form.get("z"))
        cut = request.form.get("cut")
        color = request.form.get("color")
        clarity = request.form.get("clarity")
        
        input_data_dict = {
            'carat':carat,'depth':depth,'table':table,'x':x,'y':y,'z':z,'cut':cut,
            'color':color,'clarity':clarity
        }
        
        config = ConfigurationManager()
        model_prediction_config = config.get_prediction_config()
        model_predict = ModelPrediction(model_prediction_config)
        result = model_predict.predict(input_data_dict)
        
    return render_template('result.html',result=result)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)