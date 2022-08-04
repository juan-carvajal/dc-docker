import os
import pickle

def get_model(model_key):
  file_name = f"./{model_key}.pickle"
  if os.path.exists(file_name):
    with open(file_name,"rb") as f:
      return pickle.load(f)
  else:
    return None


def save_model(model_key, model):
  file_name = f"./{model_key}.pickle"
  with open(file_name,"wb") as f:
      pickle.dump(model,f)