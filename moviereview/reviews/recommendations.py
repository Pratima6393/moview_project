
from .models import Review, Movie
from collections import defaultdict

def get_recommendations(user):
    # Get the reviews made by the user
    user_reviews = Review.objects.filter(user=user)
    # Extract the IDs of the movies the user has reviewed
    user_movie_ids = user_reviews.values_list('movie_id', flat=True)
    
    movie_scores = defaultdict(int)

    # Find reviews of movies by other users who have seen the same movies as the user
    for review in Review.objects.exclude(user=user).filter(movie_id__in=user_movie_ids):
        
        
            movie_scores[review.movie_id] += review.rating

    # Sort movies by their aggregated scores in descending order
    recommended_movies = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)
    # Get the top 5 recommended movie IDs
    recommended_movie_ids = [movie_id for movie_id, _ in recommended_movies[:5]]
    
    # Return the movie objects for the recommended movie IDs
    return Movie.objects.filter(id__in=recommended_movie_ids)

