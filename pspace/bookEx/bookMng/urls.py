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
    # I Added this
    path('comments', views.comments, name='comments'),
    path('postcommentpost', views.postcommentpost, name="postcommentpost"),
    path('book_detail/postcomment/<int:book_id>', views.postcomment, name="postcomment"),
    path('comment_detail/<int:comment_id>', views.comment_detail, name='comment_detail'),
    path('search/', views.search, name="search"),
    path('search.html', views.search, name="search2"),
    # Angy added below
    path('book_detail/postRating/<int:book_id>', views.postrate, name="postRating"),
    path('postRatingpost', views.postcommentpost, name="postRatingpost"),
    path('rate_detail/<int:rate_id>', views.rate_detail, name='rate_detail'),
]
