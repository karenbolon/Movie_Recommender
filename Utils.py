import pickle

file = open('movies.bin',mode="rb")
binary = file.read()
file.close()

movie_list = pickle.loads(binary)


#load a pickled model
file = open('nmf_model.bin',mode="rb")
binary = file.read()
file.close()

nmf_model = pickle.loads(binary)


file = open('users.bin',mode="rb")
file.read()
file.close()

users = pickle.loads(binary)

file = open('knn_imputer.bin',mode="rb")
binary = file.read()
file.close()

knn_imputer = pickle.loads(binary)
