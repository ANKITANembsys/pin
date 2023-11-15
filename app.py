# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 18:25:16 2023

@author: scien
"""

from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Sample DataFrame (replace this with your own data)
df = pd.read_csv('Pincode.csv')

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

if __name__ == '__main__':
    app.run()
