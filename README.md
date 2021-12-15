# Exoplanet-Detection-Models
References:
Astronet: https://github.com/google-research/exoplanet-ml/tree/master/exoplanet-ml/astronet <br />
Kaggle: https://www.kaggle.com/keplersmachines/kepler-labelled-time-series-data <br />
Research: https://exoplanetmodel.notion.site/4ba2be8c078245d9af80b8394b5e96d7?v=51f032e061094ec2a72b6ebf2956ecfb <br />
Kepler: https://exoplanetarchive.ipac.caltech.edu/index.html <br />

# Description
A collection of machine learning models that are trained on light curve data and are able to predict whether or not a given set of light curve data contains an exoplanet.

# Steps: 
1. [Download exoTrain.csv, exoTest.csv, and ProcessData](https://drive.google.com/file/d/1XiAFNGtGoHeqnP566WfQ9gig9--9IvNs/view?usp=sharing)
2. Upload files: exoTrain.csv, exoTest.csv, and ProcessData into the Kaggle/archive directory
3. Install modules: 
```
pip install -r requirements.txt
```

4. Retrain any of the models in Kaggle/ or Kepler/ if desired

# Server:
Navigate to the server folder in terminal and run
```
python server.py
```
to set up the server

# Website:
Navigate [here](https://github.com/bto2442/Exoplanet-Website) for the website

# Notes
- Not recommended to run more than one model at the same time because you may run into memory issues
- Please wait until results show on the website before clicking calculate again

