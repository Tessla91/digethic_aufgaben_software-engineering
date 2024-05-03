from flask import Flask, Response
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
