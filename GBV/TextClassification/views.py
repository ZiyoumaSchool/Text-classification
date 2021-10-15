import os
from django.shortcuts import render
import spacy
import torch
from .utils import classifier as cl
import pandas as pd

# CONSTANTS
FOLDER = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(FOLDER, 'Ressources/Model/model.pt')
COLLECTED_DATA_PATH = os.path.join(FOLDER, 'Ressources/DataSet/CollectedDataTrain.csv')
VOCAB = torch.load(os.path.join(FOLDER,'Ressources/Vocabulary/vocab_obj.pth'))
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  
CLASS = ["sexual_violence", "Physical_violence", "emotional_violence", "economic_violence", "Harmful_Traditional_practice"]

# HYPERPARAMETERS
size_of_vocab = len(VOCAB)
embedding_dim = 100
num_hidden_nodes = 32
num_output_nodes = 5
num_layers = 2
bidirection = True
dropout = 0.2

# Create your views here.
def index(request):
    return render(request, 'TextClassification/index.html')


def run(request):	

	if request.method == "POST":
 
		nlp = spacy.load("fr_core_news_sm")

		# Load weights
		model = cl.classifier(size_of_vocab, embedding_dim, num_hidden_nodes,num_output_nodes, num_layers, 
				bidirectional = True, dropout = dropout)
		model.load_state_dict(torch.load(MODEL_PATH))
		model.eval();

		# Inference
		def inference(sentence):

			tokenized = [tok.text for tok in nlp.tokenizer(sentence)]  #tokenize the sentence 
			indexed = [VOCAB.stoi[t] for t in tokenized]          #convert to integer sequence

			length = len(indexed)
			length_tensor = torch.LongTensor([length]).to('cpu')

			my_tensor = torch.LongTensor(indexed).to(DEVICE)           #convert to tensor
			my_tensor = torch.reshape(my_tensor, (1, length))          #reshape in form of batch,no. of words

			prediction = model(my_tensor, length_tensor)               #prediction 
			i = prediction.argmax().to('cpu').numpy()

			data = pd.read_csv(COLLECTED_DATA_PATH)

			if data["tweet"].str.contains(sentence).sum() == 0:
			    data = data.append({"tweet": sentence, "type": CLASS[i]}, ignore_index=True)
			    data.to_csv(COLLECTED_DATA_PATH)

			return CLASS[i]

		context = {
			"class": inference(request.POST["text"]),
			"text" : request.POST["text"]
		}
		return render(request, 'TextClassification/index.html', context)
	else:
		return render(request, 'TextClassification/index.html')