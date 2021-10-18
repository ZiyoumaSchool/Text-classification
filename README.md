# projet_text_classification


## Presentation

In the main goal to identify Gender Base Violence(GBV) on tweets to protect women from more violence we introduce this project. Practically it consists to classify the tweets on 5 classes which are : Sexual violence, physical violence, economic violence, emotional violence and traditional harmful pratices. To perform thos task we trained a ML model.


## Prerequisites

- A GPU
- Pytroch 1.7
- Python 3.6
- Django 3.0.5

The GPU and librairies in rights versions area available on Google Colab. It's the reason why we use it.
In following part, we will show you how to download dataset and code on Colab.

Others library are not present in right version. It's the reason why we install them for you. These additional librairies are necessary to torch hub librairy and spacy libraiy.

## Repository organization.

This repository content 3 folders which are:
- GBV containing the web project called GBV(Gender Base Violence), this porject get a web app named TextClassification runnable with "python3 manage.py runserver" command taped from prompt in the TextClassification folder.
- Modeling have the notebook and the dataset folder.
- Models get the model pytorch used in the web app.

## Usage 

### For Data scientist to build model

1) Clone the repository
2) Open Colab interface in your browser and upload the notebook text-classification.ipynb contained in the Modeling folder from your local repository.
3) Upload your dataset on the drive.
4) Give the right values for **data_path**, **models_folder** and **main_folder** variables discribe like follow:
*data_path* : concerns the path of the .csv file used as training set
*models_folder* : referes to the folder where the models obtain after each epochs will store.
*main_folder* : refers to folder containing your Train.csv file, the of Dataset folder that you have previously upload on your drive.
You can eventually set the N_EPOCHS variable which represents the number of iterations.
5) Activate the GPU execusion type().
6) Run all the notebook test().

After that, the CollectedDataTrain.csv file will be update by new sentences and text labels predicted by the model. So to get all the dataset collected, i just have to download th CollectedDataTrain.csv file

### For developper to improve the app(user experience and so one).

The GBV folder at the root directory contains the code for the django project. To set the existing project, you just have to access to the TextClassification folder and add your codes.