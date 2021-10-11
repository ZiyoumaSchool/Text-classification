# projet_text_classification


## Presentation

In the main goal to identify Gender Base Violence(GBV) on tweets to protect women from more violence we introduce this project. Practically it consists to classify the tweets on 5 classes which are : Sexual violence, physical violence, economic violence, emotional violence and traditional harmful pratices. To perform thos task we trained a ML model.


## Prerequisites

- A GPU
- Pytroch 1.7

The GPU and librairies in rights versions area available on Google Colab. It's the reason why we use it.
In following part, we will show you how to download dataset and code on Colab.


## Usage

1) Clone the repository
2) Open Colab interface in your browser and upload the notebook from your local repository.
3) Upload your dataset on the drive.
4) Give the right values for **data_path** and **models_folder** variables discribe like follow:
*data_path* : concerns the path of the .csv file used as training set
*models_folder* : referes to the folder where the models obtain after each epochs will store.
You can eventually set the N_EPOCHS variable which represents the number of iterations.
5) Activate the GPU execusion type().
6) Run all the notebook test().