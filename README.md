# Exoplanet-Detection-Models
References: <br />
- Astronet: https://github.com/google-research/exoplanet-ml/tree/master/exoplanet-ml/astronet <br />
- Kaggle: https://www.kaggle.com/keplersmachines/kepler-labelled-time-series-data <br />
- Research: https://exoplanetmodel.notion.site/4ba2be8c078245d9af80b8394b5e96d7?v=51f032e061094ec2a72b6ebf2956ecfb <br />
- Kepler: https://exoplanetarchive.ipac.caltech.edu/index.html <br />

# Description
A collection of machine learning models that are trained on light curve data provided by NASA's Kepler Space telescope(now defunct). These models parse satelite data of stars in our galaxy and beyond from a format known as fits. Fits files are essentially time series of the target stars' brightness over the lifespan of the satalites mission. Datapoints are taken in periodic 30 minute intervals. Our classification models are trained to analyze these light curves and decide if there is enough evidence of a transiting exoplanet(s) orbiting the target star system. We essentially had a time series classification problem on our hands and tackled it using various strategies.

# How Transits Work
Transits are when exoplanets eclipse the target star, causing us to percieve less starlight as a result.
![Dips in the Lightcurve!](https://www.researchgate.net/profile/Andrew-Mao-2/publication/312524607/figure/fig1/AS:452176024739840@1484818573073/A-light-curve-showing-the-transit-method-of-detecting-exoplanets.png "Transit visual")

# Report
[Click to view our final report which contains an overview of our methodolgies, analysis, and insights.](https://docs.google.com/presentation/d/e/2PACX-1vSZDj6RUvfLAhs4rLWln_Pu5XGSY8vivPdRrZ_f67f7Mu3UeC2SVyEMYo6OAr1PJ_HFRvbIafiGGYdQ/pub?start=true&loop=false&delayms=10000)

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
Navigate [here](https://github.com/bto2442/Exoplanet-Website) to interact with our models

# Notes
- Not recommended to run more than one model at the same time because you may run into memory issues
- Please wait until results show on the website before clicking calculate again

