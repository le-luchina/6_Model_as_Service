Simple Most popular recommender with Flask endpoint

Startup instructions:

```    
docker build -t flask-recommender . 
    
docker run -p 8000:8000 flask-recommender
```    

Flask endpoint runs on http://127.0.0.1:8000/predict?user_id=123&k=10

To get valid recommendations, enter user id: int in range 1, 205176

optionally enter k (number of recs, default == 10): int
