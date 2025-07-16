import pickle

with open("rfc.pkl","rb") as file :
   model = pickle.load(file)


env = [[23.223974 , 81.604873 , 6.980401 , 263.964248]]
print(model.predict(env))   