from django.contrib import admin

# Register your models here.
from .models import Movie, Review, User 
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active','is_staff','is_superuser')
    
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description','release_date','genre','poster')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie','rating','comment')
admin.site.register(Movie,MovieAdmin)
admin.site.register(Review,ReviewAdmin)   
admin.site.register(User,UserAdmin) 

