from django.urls import path
from . import views
from bookMng.views import Register
urlpatterns = [
    path('', views.index, name='index'),

    path('postbook', views.postbook, name='postbook'),
    path('mybooks', views.mybooks, name="mybooks"),
    path('displaybooks', views.displaybooks, name="displaybooks"),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),

    #I Added this
    path('comments',views.comments,name='comments'),
    path('postcommentpost',views.postcommentpost,name="postcommentpost"),

    # Change path due to directory change
    path('book_detail/feature_comments/postcomment/<int:book_id>',views.postcomment,name="postcomment"),
    path('comment_detail/<int:comment_id>', views.comment_detail, name='comment_detail'),

    # Favorites Page
    path('favorites/',views.favorites,name="favorites"),

    # Adding Book to Favorites Page
    path('book_detail/feature_favorites/addfavorites/<int:book_id>',views.addfavorites,name='addfavorites'),

    ]


