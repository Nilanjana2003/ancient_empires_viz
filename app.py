from flask import Flask
from flask import Flask,jsonify,request
from flask_cors import CORS
import pandas as pd
app = Flask(__name__)
CORS(app)
@app.route("/empires")
def get_empires():
    df = pd.read_csv("C:/Users/Nila/Desktop/pythonprojects/ancient_empires_viz/data/clean_empire_data.csv")
    year = request.args.get("year",type = int)
    if year is not None:
        df = df[
            (df["start_year_bce"]>= year) &
            (df["end_year_bce"]<=year)
            
        ]
    return jsonify(df.to_dict(orient = "records"))
if __name__ == "__main__":
    app.run(debug = True)
    