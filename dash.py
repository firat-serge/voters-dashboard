import requests
from flask import Flask, render_template

# Connect to OpenWeatherMap API
#api_key = 'your_api_key'
city = 'ADMIN_NAME'
url = f'http://127.0.0.1:5000/votes_geojson'

response = requests.get(url)
data = response.json()

# Create Flask app
app = Flask(__name__)

# Create route for dashboard
@app.route('/')
def dashboard():
    # Extract weather information from API response
    vote = {
        'city': data['ADMIN_NAME'],
        'AKP': round(data['main']['AKP_per']),
        'CHP': round(data['main']['CHP_per']),
        'HDP': round(data['main']['HDP_per']),
        'MHP': round(data['main']['MHP_per']),
    }
    return render_template('dashboard.html', vote=vote)

if __name__ == '__main__':
    app.run()
