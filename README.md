# IBM Capstone project

This repo holds the .ipynb and other required files to complete all the
labs in the Capstone project for
IBM Coursera data science certification.

## Notebooks in this repo

+ **Data Collection**  
    *Notebook name* : `Data Collection API Lab.ipynb`  
    Used to demonstrate the SpaceX API usage
    (i.e. how to extract data by means of an exisiting API)

    *Notebook name* : `Data Collection Webscrapping.ipynb`  
    Used to collect SpaceX records from the wikipedia page.

+ **Data Wrangling**  
    *Notebook name* : `Data Wrangling exercise.ipynb`  
    Used to purge the datasets to be used later for EDA and modeling.

+ **EDA by SQL**  
    *Notebook name* : `EDS-sql-coursera_sqllite.ipynb`  
    Shows the usage of sqlite to pass SQL
    queries through a jupyter notebook.

+ **EDA by graphical approach**  
    *Notebook name* : `EDA with visualization.ipynb`  
    Used to study correlation between variables and the
    landing success rate by visual means (***matplotlib*** and ***seaborn***)

+ **Dashboard**  
    *Notebook name* : `DashPLotly_lab_DSCapstone.ipynb`  
    Dash-plotly dashboard creation in a jupyter notebook.

+ **Geographical visual information**  
    *Notebook name* : `lab_jupyter_launch_site_location.ipynb`  
    Used to visualize through ***Folium*** information about the
    launch sites for SpaceX.

+ **Machine Learning predictive analysis**  
    *Notebook name* : `SpaceX_Machine Learning Prediction_Part_5.ipynb`  
    Used to train and test several different machine learning
    algorithms and their predictive capabilities.

* * *

## Extra dahsboard

And extra app is included in this repo, under the folder dash_app.  
The idea was to create the required plotly dashboard by scripting
in python, instead of realying completely in a JupyterNotebook
(which is somewhat of a buggy solution for plotly-dash).  

This also granted the opportunity to play with bootstrap components,
improving the visualization quality and expanding the required number of graphs.

To run the app, install the required libraries, and on the dash_app directory
run the main.py file

```bash
>> python main.py
```
