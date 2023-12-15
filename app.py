# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 18:25:16 2023

@author: scien
"""

from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS  # Import the CORS extension


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
# Sample DataFrame (replace this with your own data)
df = pd.read_csv('Pincode.csv', encoding='ISO-8859-1')

#df = pd.DataFrame(data)

@app.route('/filter', methods=['POST'])
def filter_dataframe():
    try:
        # Get inputs from the request JSON
        name_filter = request.json.get('Pincode', None)
        #age_filter = request.json.get('age', None)

        # Apply filters to the DataFrame
        filtered_df = df[df['Pincode'] == name_filter]

        # Convert filtered DataFrame to JSON
        result = filtered_df.to_json(orient='records')

        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/filter_city', methods=['POST'])
def filter_dataframe():
    try:
        # Get inputs from the request JSON
        name_filter = request.json.get('city', None)
        #age_filter = request.json.get('age', None)

        # Apply filters to the DataFrame
        filtered_df = df[df['District'] == name_filter]

        # Convert filtered DataFrame to JSON
        result = filtered_df.to_json(orient='records')

        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/all_city', methods=['GET'])
def get_unique_city():
    column_name = 'District'  # Replace with your column name

    unique_values = df[column_name].unique()
    result = {column_name: list(unique_values)}

    return jsonify(result)

@app.route('/all_state', methods=['GET'])
def get_unique_state():
    column_name = 'StateName'  # Replace with your column name

    unique_values = df[column_name].unique()
    result = {column_name: list(unique_values)}

    return jsonify(result)

@app.route('/all_pin', methods=['GET'])
def get_unique_pin():
    column_name = 'Pincode'  # Replace with your column name

    unique_values = df[column_name].unique()
    result = {column_name: list(unique_values)}

    return jsonify(result)


@app.route('/post_by_city', methods=['POST'])
def post_by_city():
    try:
        # Get inputs from the request JSON
        name_filter = request.json.get('District', None)
        #age_filter = request.json.get('age', None)

        # Apply filters to the DataFrame
        filtered_df = df[df['District'] == name_filter]
        unique_values = df["Pincode"].unique()

        # Convert filtered DataFrame to JSON
        result = filtered_df.to_json(orient='records')

        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run()
