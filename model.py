import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from joblib import load




dataset = pd.read_csv('C:\Users\kfiel\DataInternship\Flask_Web_App\Data\ds_salaries.csv')
pipeline = load('C:\Users\kfiel\DataInternship\Flask_Web_App\salary_predictor.joblib')

print(pipeline.predict([0,1,0,0]))
