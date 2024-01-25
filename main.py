from flask import Flask, request
from flask_cors import CORS
from api import save_data
from flask_restful import Api, Resource, reqparse
from model import pred
import pandas as pd
import modelling
import json


import time

app = Flask(__name__)
CORS(app)
api = Api(app)
api_args = reqparse.RequestParser()

class Predict(Resource):

    modelling.model_making()

    def predict(self, args):

        Administrative = args["Administrative"]
        Administrative_Duration = args["Administrative_Duration"]
        Informational = args["Informational"]
        Informational_Duration = args["Informational_Duration"]
        ProductRelated = args["ProductRelated"]
        ProductRelated_Duration = args["ProductRelated_Duration"]
        BounceRates = args["BounceRates"]
        ExitRates = args["ExitRates"]
        PageValues = args["PageValues"]
        SpecialDay = args["SpecialDay"]
        OperatingSystems = args["OperatingSystems"]
        Browser = args["Browser"]
        Region = args["Region"]
        TrafficType = args["TrafficType"]
        Weekend = args["Weekend"]
        VisitorType_New_Visitor = args["VisitorType_New_Visitor"]
        VisitorType_Other = args["VisitorType_Other"]
        VisitorType_Returning_Visitor = args["VisitorType_Returning_Visitor"]
        Months = [
        args["Month_Aug"],
        args["Month_Dec"],
        args["Month_Feb"],
        args["Month_Jul"],
        args["Month_June"],
        args["Month_Mar"],
        args["Month_May"],
        args["Month_Nov"],
        args["Month_Oct"],
        args["Month_Sep"]]


        X = { "Administrative" : [Administrative],
              "Administrative_Duration": [Administrative_Duration],
              "Informational": [Informational],
              "Informational_Duration": [Informational_Duration],
              "ProductRelated": [ProductRelated],
              "ProductRelated_Duration": [ProductRelated_Duration],
              "BounceRates": [BounceRates],
              "ExitRates": [ExitRates],
              "PageValues": [PageValues],
              "SpecialDay": [SpecialDay],
              "OperatingSystems": [OperatingSystems],
              "Browser": [Browser],
              "Region": [Region],
              "TrafficType": [TrafficType],
              "Weekend": [Weekend],
              "VisitorType_New_Visitor": [VisitorType_New_Visitor],
              "VisitorType_Other": [VisitorType_Other],
              "VisitorType_Returning_Visitor": [VisitorType_Returning_Visitor],
              "Month_Aug": [Months[0]],
              "Month_Dec": [Months[1]],
              "Month_Feb": [Months[2]],
              "Month_Jul": [Months[3]],
              "Month_June":[Months[4]],
              "Month_Mar": [Months[5]],
              "Month_May": [Months[6]],
              "Month_Nov": [Months[7]],
              "Month_Oct": [Months[8]],
              "Month_Sep": [Months[9]]
              }
        count = 18
        for month in Months:
            if month:
                x = list(args)
                args["month"]=x[count]

            count+=1

        X = pd.DataFrame(data=X)

        revenue = pred(X)

        args["revenue"], args["proba"] = revenue["revenue"], revenue["proba"]
        save_data(args)
        return revenue



    def post(self):
        args = api_args.parse_args()
        body = request.get_json()
        predictions = self.predict(body)
        # return predictions
        return f"Revenue is {predictions['revenue']} and Proba: {predictions['proba']}"


api.add_resource(Predict, "/api")
if __name__ =="__main__":
    app.run(debug=True,use_reloader=False)