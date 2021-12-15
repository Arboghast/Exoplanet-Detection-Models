import numpy as np
from tensorflow import keras
import pickle
from numpy import exp
import lightkurve
from sklearn import preprocessing
import pandas as pd
import os
import json
import inputlightcurve
from tsfresh import extract_features
from tsfresh.feature_extraction import MinimalFCParameters, EfficientFCParameters
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def tobool(probs, path):
    if(np.any(probs >= .5)): #potential bug
        return "true"
    else:
        return "false"

def logistic_layer(y):
    y = np.array(y)
    y = 1 / (1 + exp(-y))
    y = y.ravel()
    return y

def normalize(data):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    data = (data - mean) / std
    return data

def light_curve_to_matrix_kaggle_lightkurve(lc):
    inputLC = inputlightcurve.downloadLC_kaggle(lc)
    flux_copy = np.array(inputLC[0])
    amt_pad = 3197-(len(inputLC[0])%3197)                                              #amount of medians to pad the last row of dataframe
    flux_median = np.full(shape=amt_pad, fill_value=np.median(np.array(inputLC[0])))   #array of medians to pad the last row to reach a factor of 3197
    flux_copy = np.append(flux_copy, flux_median)
    final_matrix = np.reshape(flux_copy, (len(flux_copy)//3197,3197))
    normalized_matrix = normalize(final_matrix)
    return normalized_matrix

def lightcurve_to_kaggle_tsfresh(lc):
    matrix = pd.DataFrame({
        "id" : np.zeros(len(lc), dtype=int),
        "time" : list(range(0, len(lc))),
        "flux" : lc})
    
    extracted_features = extract_features(matrix, column_id= "id", column_sort= "time", 
                                      column_value= "flux", 
                                      default_fc_parameters= EfficientFCParameters())
    extracted_features.dropna(axis=1, inplace=True)  #dropped the nan column
    normalized_matrix = preprocessing.normalize(extracted_features,norm='max', axis=0)
    return normalized_matrix

def lightcurve_to_kepler_tsfresh(lc):
    matrix = pd.DataFrame({
        "id" : np.zeros(len(lc), dtype=int),
        "time" : list(range(0, len(lc))),
        "FLUX" : lc})
    
    extracted_features = extract_features(matrix, column_id= "id", column_sort= "time", 
                                      column_value= "FLUX", 
                                      default_fc_parameters= EfficientFCParameters())
    with open("../Kepler/TSFresh/nanlist.txt") as file:
        for readline in file: 
            line_strip = readline.strip()
            extracted_features.drop(line_strip, axis=1, inplace=True)
    normalized_matrix = preprocessing.normalize(extracted_features,norm='max', axis=0)
    return normalized_matrix

def getPredictions(inputLC, models, path):
    inputLC_keras = np.expand_dims(inputLC, -1)
    predictions = {}
    
    if "rnn" in models:
        reconstructed_model = keras.models.load_model(path + "/keras-models/KerasRNN")
        probability = reconstructed_model.predict(inputLC_keras)
        predictions["RNN"] = {"Probability" : str(np.max(probability)), "Classification" : tobool(probability, path)}

    if "lstm" in models:
        reconstructed_model = keras.models.load_model(path + "/keras-models/KerasLSTM")
        probability = reconstructed_model.predict(inputLC_keras)
        predictions["LSTM"] = {"Probability" : str(np.max(probability)), "Classification" : tobool(probability, path)}
            
    if "gru" in models:
        reconstructed_model = keras.models.load_model(path + "/keras-models/KerasGRU")
        probability = reconstructed_model.predict(inputLC_keras)
        predictions["GRU"] = {"Probability" : str(np.max(probability)), "Classification" : tobool(probability, path)}

    #Logistic Regression
    if "lr" in models:
        with open(path + "/tf-models/multi-lr.npy", 'rb') as f:
            W = np.load(f)
            b = np.load(f)
        predicted_y = W * inputLC + b
        predicted_y = logistic_layer(predicted_y)
        probability = np.max(predicted_y)
        predictions["LR"] = {"Probability" : str(np.max(probability)), "Classification" : tobool(np.array(predicted_y), path)}

            
    #Decision Tree & Random Forest
    if "rf" in models:
        with open(path + "/tf-models/decision-tree.pkl", 'rb') as f:
            dt = pickle.load(f)
        probability = dt.predict_proba(inputLC)
        predictions["DT"] = {"Probability" : str(np.max(probability)), "Classification" : tobool(probability, path)}

        with open(path + "/tf-models/random-forest.pkl", 'rb') as f:
            rf = pickle.load(f)
        probability = rf.predict_proba(inputLC)
        predictions["RF"] = {"Probability" : str(np.max(probability)), "Classification" : tobool(probability, path)}
    
    return predictions
             
def predict(target_name, training_data, processing, models):
    
    if training_data == "kaggle" and processing == "tsfresh":
            inputLC = inputlightcurve.downloadLC_kaggle(target_name)[0]
            inputLC_kaggle_tsfresh = lightcurve_to_kaggle_tsfresh(inputLC)
            return getPredictions(inputLC_kaggle_tsfresh, models, "../Kaggle/TSFresh")
                
    if training_data == "kaggle" and processing == "lightkurve":
            inputLC_kaggle_lightkurve = light_curve_to_matrix_kaggle_lightkurve(target_name)
            return getPredictions(inputLC_kaggle_lightkurve, models, "../Kaggle/Regular")
    
    if training_data == "kepler" and processing == "tsfresh":
            inputLC = inputlightcurve.downloadLC_kepler(target_name)[0]
            inputLC_kepler_tsfresh = lightcurve_to_kepler_tsfresh(inputLC)
            return getPredictions(inputLC_kepler_tsfresh, models, "../Kepler/TSFresh")
        
    if training_data == "kepler" and processing == "lightkurve":
            inputLC_kepler_lightkurve = inputlightcurve.downloadLC_kepler(target_name)
            return getPredictions(inputLC_kepler_lightkurve, models, "../Kepler/Regular")    
    return {"error"}