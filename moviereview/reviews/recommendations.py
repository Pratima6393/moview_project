
from .models import Review, Movie
from collections import defaultdict

def get_recommendations(user):
    user_reviews = Review.objects.filter(user=user)
    movie_ids = user_reviews.values_list('movie_id', flat=True)

    movie_scores = defaultdict(int)
    #----------------who did not saw the movie-------------------------
    for review in Review.objects.exclude(user=user).filter(movie_id__in=movie_ids):
        movie_scores[review.movie_id] += review.rating

    recommended_movies = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)
    recommended_movie_ids = [movie_id for movie_id, _ in recommended_movies[:5]]
    return Movie.objects.filter(id__in=recommended_movie_ids)

