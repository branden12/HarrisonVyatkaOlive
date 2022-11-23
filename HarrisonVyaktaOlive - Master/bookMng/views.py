from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

#Models
from .models import MainMenu
from .models import Book
from .models import Comment
from .models import Favorite

#Forms
from .forms import BookForm
from .forms import CommentForm
from .forms import FavoriteForm




def index(request):
    return render(request, 'bookMng/index.html',
    {
        'item_list': MainMenu.objects.all()
    })
def postbook(request):

    submitted = False

    if request.method == 'POST':

        form = BookForm(request.POST,request.FILES)

        if form.is_valid():
            # form.save()
            book = form.save(commit=False)
            try:
                book.username=request.user
            except Exception:
                pass
            book.save()
            return HttpResponseRedirect('/postbook?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/postbook.html',
                 {
                    'form': form,
                    'item_list': MainMenu.objects.all(),
                    'submitted': submitted
                 })

def displaybooks(request):
    books = Book.objects.all()

    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request,
                  'bookMng/displaybooks.html',
                 {
                    'item_list': MainMenu.objects.all(),
                    'books': books,
                 })


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    book.pic_path = book.picture.url[14:]

    return render(request,
                  'bookMng/book_detail.html',
                 {
                    'item_list': MainMenu.objects.all(),
                    'book': book,
                 })


def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()

    return render(request,
                  'bookMng/book_delete.html',
                 {
                    'item_list': MainMenu.objects.all(),
                 })


def mybooks(request):
    books = Book.objects.filter(username=request.user)
    for b in books:
        b.pic_path = b.picture.url[14:]
    return render(request,
                  'bookMng/mybooks.html',
                 {
                    'item_list': MainMenu.objects.all(),
                    'books': books,
                 })

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

def comments(request):

    # Creating list of comments
    commentlist = Comment.objects.all()

    return render(request,
                  'bookMng/feature_comments/comments.html',

                  {
                      'item_list': MainMenu.objects.all(),
                      'commentlist': commentlist,
                  })

def postcomment(request, book_id):

    book = Book.objects.get(id=book_id)

    submitted = False

    if request.method == 'POST':

        form = CommentForm(request.POST,request.FILES)

        if form.is_valid():

            # form.save()
            comment = form.save(commit=False)

            try:
                comment.username = request.user
                comment.book = book.name

            except Exception:
                pass
            comment.save()

            return HttpResponseRedirect('/postcommentpost?submitted=True')
    else:
        form = CommentForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/feature_comments/postcomment.html',
                 {
                    'form': form,
                    'item_list': MainMenu.objects.all(),
                    'submitted': submitted,
                    'book': book
                 })
def postcommentpost(request):

    submitted = False
    if request.method == 'POST':

        form = CommentForm(request.POST,request.FILES)

        if form.is_valid():
            # form.save()
            comment = form.save(commit=False)

            try:
                comment.username = request.user
            except Exception:
                pass
            comment.save()

            return HttpResponseRedirect('/postcommentpost?submitted=True')
    else:
        form = CommentForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/feature_comments/postcomment.html',
                 {
                    'form': form,
                    'item_list': MainMenu.objects.all(),
                    'submitted': submitted,
                 })

def comment_detail(request, comment_id):
    comment = Comment.objects.get(id=comment_id)

    return render(request,
                  'bookMng/feature_comments/comment_detail.html',
                 {
                    'item_list': MainMenu.objects.all(),
                    'comment': comment,
                 })

# Favorite Tab
def favorites(request):

    # FavoriteList = Favorite.objects.all()

    return render(request,
                  'bookMng/feature_favorites/favorites.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      #'favorite_list': FavoriteList
                  })

def addfavorites(request, book_id):

    # Getting Book Object
    book = Book.objects.get(id=book_id)

    books = Book.objects.all()
    book.pic_path = book.picture.url[14:]

    # Setting Submitted to False
    submitted = False

    # Check if the (form: method=Post)
    if (request.method == 'POST'):

        form = FavoriteForm(request.POST, request.FILES)

        # Check if form "exist"
        if form.is_valid():

            favorite = form.save(commit=False)

            try:
                favorite.title = book.name
            except Exception:
                pass

            favorite.save()
            return HttpResponseRedirect('/addfavorites?submitted=True')
    else:
        form = FavoriteForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/feature_favorites/addfavorites.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                      'book': book,

                  })


