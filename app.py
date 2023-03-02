# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

import pickle
import numpy as numpy

# Create application
app = Flask(__name__)

# Load ML model
#model1 = pickle.load(open("final.pkl", "rb"))
#modell = pickle.load(open('model.pkl', 'rb'))
model = pickle.load(open('new.pkl', 'rb'))

# Bind home function to URL


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

# Bind predict function to URL


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":

        Item_Weight = request.form['Item_Weight']
        Item_Fat_Content = request.form['Item_Fat_Content']
        if Item_Fat_Content == "Low Fat":
            Low_Fat = 1
            Regular = 0
        else:
            Regular = 1
            Low_Fat = 0

        Item_Visibility = request.form['Item_Visibility']
        #Item_Visibility = np.sqrt(Item_Visibility)

        Item_Type = request.form['Item_Type']
        if (Item_Type == "Diary"):
            Diary = 1
            snacks_food = 0
            soft_drinks = 0
            meat = 0
            fruits_and_vegetables = 0
            household = 0
            frozen_food = 0
            breakfast = 0
            health_hygine = 0
            hard_drinks = 0
            canned = 0
            starchy_food = 0
            seafood = 0
            baking_good = 0
            others = 0
            bread = 0
        elif(Item_Type == "snacks_food"):
            Diary = 0
            snacks_food = 1
            soft_drinks = 0
            meat = 0
            fruits_and_vegetables = 0
            household = 0
            frozen_food = 0
            breakfast = 0
            health_hygine = 0
            hard_drinks = 0
            canned = 0
            starchy_food = 0
            seafood = 0
            baking_good = 0
            others = 0
            bread = 0
        elif(Item_Type == "soft_drinks"):
            Diary = 0
            snacks_food = 0
            soft_drinks = 1
            meat = 0
            fruits_and_vegetables = 0
            household = 0
            frozen_food = 0
            breakfast = 0
            health_hygine = 0
            hard_drinks = 0
            canned = 0
            starchy_food = 0
            seafood = 0
            baking_good = 0
            others = 0
            bread = 0
        elif(Item_Type == "meat"):
            Diary = 0
            snacks_food = 0
            soft_drinks = 0
            meat = 1
            fruits_and_vegetables = 0
            household = 0
            frozen_food = 0
            breakfast = 0
            health_hygine = 0
            hard_drinks = 0
            canned = 0
            starchy_food = 0
            seafood = 0
            baking_good = 0
            others = 0
            bread = 0
        elif(Item_Type == "fruits_and_vegetables"):
            Diary = 0
            snacks_food = 0
            soft_drinks = 0
            meat = 0
            fruits_and_vegetables = 1
            household = 0
            frozen_food = 0
            breakfast = 0
            health_hygine = 0
            hard_drinks = 0
            canned = 0
            starchy_food = 0
            seafood = 0
            baking_good = 0
            others = 0
            bread = 0
        elif(Item_Type == "household"):
            Diary = 0
            snacks_food = 0
            soft_drinks = 0
            meat = 0
            fruits_and_vegetables = 0
            household = 1
            frozen_food = 0
            breakfast = 0
            health_hygine = 0
            hard_drinks = 0
            canned = 0
            starchy_food = 0
            seafood = 0
            baking_good = 0
            others = 0
            bread = 0
        elif(Item_Type == "frozen_food"):
            Diary = 0
            snacks_food = 0
            soft_drinks = 0
            meat = 0
            fruits_and_vegetables = 0
            household = 0
            frozen_food = 1
            breakfast = 0
            health_hygine = 0
            hard_drinks = 0
            canned = 0
            starchy_food = 0
            seafood = 0
            baking_good = 0
            others = 0
            bread = 0
        elif(Item_Type == "breakfast"):
            Diary = 0
            snacks_food = 0
            soft_drinks = 0
            meat = 0
            fruits_and_vegetables = 0
            household = 0
            frozen_food = 0
            breakfast = 1
            health_hygine = 0
            hard_drinks = 0
            canned = 0
            starchy_food = 0
            seafood = 0
            baking_good = 0
            others = 0
            bread = 0
        elif(Item_Type == "health_hygine"):
            Diary = 0
            snacks_food = 0
            soft_drinks = 0
            meat = 0
            fruits_and_vegetables = 0
            household = 0
            frozen_food = 0
            breakfast = 0
            health_hygine = 1
            hard_drinks = 0
            canned = 0
            starchy_food = 0
            seafood = 0
            baking_good = 0
            others = 0
            bread = 0
        elif(Item_Type == "hard_drinks"):
            Diary = 0
            snacks_food = 0
            soft_drinks = 0
            meat = 0
            fruits_and_vegetables = 0
            household = 0
            frozen_food = 0
            breakfast = 0
            health_hygine = 0
            hard_drinks = 1
            canned = 0
            starchy_food = 0
            seafood = 0
            baking_good = 0
            others = 0
            bread = 0
        elif(Item_Type == "canned"):
            Diary = 0
            snacks_food = 0
            soft_drinks = 0
            meat = 0
            fruits_and_vegetables = 0
            household = 0
            frozen_food = 0
            breakfast = 0
            health_hygine = 0
            hard_drinks = 0
            canned = 1
            starchy_food = 0
            seafood = 0
            baking_good = 0
            others = 0
            bread = 0
        elif(Item_Type == "starchy_food"):
            Diary = 0
            snacks_food = 0
            soft_drinks = 0
            meat = 0
            fruits_and_vegetables = 0
            household = 0
            frozen_food = 0
            breakfast = 0
            health_hygine = 0
            hard_drinks = 0
            canned = 0
            starchy_food = 1
            seafood = 0
            baking_good = 0
            others = 0
            bread = 0
        elif(Item_Type == "seafood"):
            Diary = 0
            snacks_food = 0
            soft_drinks = 0
            meat = 0
            fruits_and_vegetables = 0
            household = 0
            frozen_food = 0
            breakfast = 0
            health_hygine = 0
            hard_drinks = 0
            canned = 0
            starchy_food = 0
            seafood = 1
            baking_good = 0
            others = 0
            bread = 0
        elif(Item_Type == "baking_good"):
            Diary = 0
            snacks_food = 0
            soft_drinks = 0
            meat = 0
            fruits_and_vegetables = 0
            household = 0
            frozen_food = 0
            breakfast = 0
            health_hygine = 0
            hard_drinks = 0
            canned = 0
            starchy_food = 0
            seafood = 0
            baking_good = 1
            others = 0
            bread = 0
        elif(Item_Type == "bread"):
            Diary = 0
            snacks_food = 0
            soft_drinks = 0
            meat = 0
            fruits_and_vegetables = 0
            household = 0
            frozen_food = 0
            breakfast = 0
            health_hygine = 0
            hard_drinks = 0
            canned = 0
            starchy_food = 0
            seafood = 0
            baking_good = 0
            others = 0
            bread = 1
        else:
            Diary = 0
            snacks_food = 0
            soft_drinks = 0
            meat = 0
            fruits_and_vegetables = 0
            household = 0
            frozen_food = 0
            breakfast = 0
            health_hygine = 0
            hard_drinks = 0
            canned = 0
            starchy_food = 0
            seafood = 0
            baking_good = 0
            others = 1
            bread = 0

        Item_MRP = request.form['Item_MRP']
        Outlet_Establishment_Year = request.form['Outlet_Establishment_Year']
        Outlet_Location_Type = request.form['Outlet_Location_Type']
        if Outlet_Location_Type == "Tier 1":
            Tier2 = 0
            Tier3 = 0
        elif Outlet_Location_Type == "Tier 2":
            Tier2 = 1
            Tier3 = 0
        else:
            Tier2 = 0
            Tier3 = 1

        Outlet_Size = request.form['Outlet_Size']
        if Outlet_Size == "Small":
            value = 2
        elif Outlet_Size == "Medium":
            value = 1
        else:
            value = 0

        Outlet_Type = request.form['Outlet_Type']
        if Outlet_Type == "Supermarket Type1":
            SupermarketType1 = 1
            SupermarketType2 = 0
            SupermarketType3 = 0
        elif Outlet_Type == "Supermarket Type2":
            SupermarketType1 = 0
            SupermarketType2 = 1
            SupermarketType3 = 0
        elif Outlet_Type == "Supermarket Type3":
            SupermarketType1 = 0
            SupermarketType2 = 0
            SupermarketType3 = 1
        else:
            SupermarketType1 = 0
            SupermarketType2 = 0
            SupermarketType3 = 0

        prediction = model.predict([[Item_Weight, Item_Visibility, Item_MRP, Outlet_Establishment_Year, value, Regular, breakfast, canned, Diary, frozen_food, fruits_and_vegetables,
                                     hard_drinks, health_hygine, household, meat, others, bread, snacks_food, soft_drinks, starchy_food, Tier2, Tier3, SupermarketType1, SupermarketType2, SupermarketType3]])
        return render_template("index.html", Price=prediction)
    else:
        return render_template("index.html")


###
if __name__ == "__main__":
    # Run the application
    app.run(debug=True)
