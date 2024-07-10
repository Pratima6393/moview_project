from django.shortcuts import render

# Create your views here.
# reviews/views.py
from django.contrib.auth import authenticate
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from .models import Movie,User
from .serializers import MovieSerializer
from .models import Review
from .serializers import ReviewSerializer
from rest_framework import generics, permissions,filters
from .recommendations import get_recommendations
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

# ---------------------------registration class-----------------
class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


#----------------------Login class---------------------------------
class Login(APIView):
    permission_classes = [AllowAny]  # ----------Allow unauthenticated access----------------

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        
        # ----------------Authenticate the user--------------------
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid Credentials'}, status=400)



#-----------------------ovie create and list-------------------------------
class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genre', 'release_date']
    search_fields = ['title', 'description']
    ordering_fields = ['release_date', 'title']
    pagination_class = PageNumberPagination

#--------------------------movie update and delete------------------------------------
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
#------------------------------review create and get list-------------------------------------
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['movie', 'rating']
    search_fields = ['comment']
    ordering_fields = ['rating']
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#----------------------------------review update and dalete class-------------------------

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


#-------------------- recomendation function---------------------------
# class Recommendation(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         recommended_movies = get_recommendations(request.user)
#         serializer = MovieSerializer(recommended_movies, many=True)
#         return Response(serializer.data)

class Recommendation(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        recommended_movies = get_recommendations(request.user)
        serializer = MovieSerializer(recommended_movies, many=True)
        return Response(serializer.data)