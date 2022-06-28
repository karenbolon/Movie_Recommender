import pickle
from Utils import users, nmf_model, movie_list, knn_imputer
import pandas as pd
import numpy as np


Q = pd.DataFrame(data=nmf_model.components_,
                index=['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18','f19','f20'],
                columns=movie_list)


new_user_query = {"Lord of the Rings": 10,
                 "Melancholia":7,
                 "Finding Nemo": 7,
                 "Godfather, The": 6,
                 "From Dusk Till Dawn": 1,
                 "Waterboy, The": 7,
                 "Like Water for Chocolate": 10,
                 "Face Off": 7,
                 "Spice World": 0}

def nmf_model_recommendations(new_user_query, number_of_movies_recommended):
    new_ratings = pd.DataFrame(data=new_user_query,
                                columns=movie_list,
                                index = ["new_user"])

    new_imputed = pd.DataFrame(data=knn_imputer.transform(new_ratings),
                                 columns=movie_list,
                                 index = ["new_user"])
    
    recon_new_ratings = pd.DataFrame(data=np.dot(nmf_model.transform(new_imputed),Q),
                                              columns=movie_list,
                                              index=['new_user'])
    
    recc_new=recon_new_ratings.T
    movies=recc_new.sort_values(by='new_user', ascending=False).index.tolist()

    return movies[:number_of_movies_recommended]


if __name__ == '__main__':
    print(nmf_model_recommendations(new_user_query=new_user_query,number_of_movies_recommended=5))
