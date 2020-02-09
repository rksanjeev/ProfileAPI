from django.contrib import admin
import UserProfile.models
# Register your models here.
admin.site.register(UserProfile.models.ProfileFeed)
admin.site.register(UserProfile.models.UserModel)