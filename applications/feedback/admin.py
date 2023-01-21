from django.contrib import admin

from applications.feedback.models import Comment, Favourite, Like, Rating

admin.site.register(Comment)
admin.site.register(Favourite)
admin.site.register(Like)
admin.site.register(Rating)