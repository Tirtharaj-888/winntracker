from flask import Flask, render_template, url_for
import requests
import pandas as pd
import json
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, date
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')

def lt_refresh_function():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

