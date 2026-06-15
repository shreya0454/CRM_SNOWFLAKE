from flask import Flask, jsonify
import csv
import io
import requests

app = Flask(__name__)

@app.route('/api/sales-teams', methods=['GET'])
def get_sales_teams():
    url = 'https://raw.githubusercontent.com/shreya0454/CRM_SNOWFLAKE/main/CRM_SALES_TEAMS_D.csv'
    response = requests.get(url)
    reader = csv.DictReader(io.StringIO(response.text))
    teams = [row for row in reader]
    return jsonify(teams)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
