from django.contrib import admin

# Register your models here.
from .models import Movie, Review, User 
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active','is_staff','is_superuser')
    # search_fields = ('user__phone_number', 'name')

admin.site.register(Movie)
admin.site.register(Review)   
admin.site.register(User,UserAdmin) 

