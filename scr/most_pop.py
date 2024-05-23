import pandas as pd
import pickle
import os

path_train = os.path.join(os.path.dirname(__file__), '../data/user_product_train.csv')
path_test = os.path.join(os.path.dirname(__file__), '../data/user_product_test.csv')

user_product_train = pd.read_csv(path_train)
user_product_test = pd.read_csv(path_test)

# calculate recomendaions
def most_popular_recommender(df, num_recommendations):
    popular_products = df['product_id'].value_counts().reset_index()
    recommendations = popular_products.head(num_recommendations)
    recommendations = recommendations['product_id'].tolist()

    return recommendations

recs_pop = most_popular_recommender(user_product_train, 300)

model_path = os.path.join(os.path.dirname(__file__), 'recommendations.pkl')

# Save the recommendations to a pickle file
with open(model_path, 'wb') as file:
    pickle.dump(recs_pop, file)
