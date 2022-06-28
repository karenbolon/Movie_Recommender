from flask import Flask
from my_recommender import nmf_model_recommendations
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html', title='In need of a movie recommendation?')

@app.route('/recommender')
def recommender():
    user_query = dict(request.args)
    print(user_query)
    # a python dictionary consisting of
    # "name"-value pairs from the HTML form!

    recs = nmf_model_recommendations(new_user_query=user_query, number_of_movies_recommended=5)




    return render_template('recommendations.html',
                            movies = recs)

#    recs = nmf_model_recommendations(new_user_query, number_of_movies_recommended=5)
#    return render_template('recommendations.html',
#                            movies = recs)

if __name__ == "__main__":
    app.run(debug=True, port=5000)