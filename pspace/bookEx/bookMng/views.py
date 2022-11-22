from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Models
from .models import MainMenu
from .models import Book
from .models import Comment
# Forms
from .forms import BookForm, RateForm
from .forms import CommentForm
from.models import Rate


def index(request):
    return render(request, 'bookMng/index.html',
                  {
                      'item_list': MainMenu.objects.all()
                  })


def postbook(request):
    submitted = False
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            book = form.save(commit=False)
            try:
                book.username = request.user
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
    ratings = Rate.objects.all()

    for b in books:
        b.pic_path = b.picture.url[14:]

    return render(request,
                  'bookMng/displaybooks.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'books': books,
                      'ratings': ratings
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
    commentlist = Comment.objects.all()

    return render(request,
                  'bookMng/comments.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'commentlist': commentlist,
                  })


def postcomment(request, book_id):
    book = Book.objects.get(id=book_id)
    submitted = False
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
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
                  'bookMng/postcomment.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                      'book': book
                  })


def postcommentpost(request):
    submitted = False
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
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
                  'bookMng/postcomment.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,

                  })


def comment_detail(request, comment_id):
    comment = Comment.objects.get(id=comment_id)

    return render(request,
                  'bookMng/comment_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'comment': comment,
                  })


def search(request):
    submitted = False
    searchmethod = None
    searchvalue = None
    book = None
    books = None
    if request.method == 'POST':
        try:
            # This is how you get those parameters
            searchmethod = request.POST.get("searchmethod")
            searchvalue = request.POST.get("searchvalue")
        except Exception:
            print("Error occurred")

        return HttpResponseRedirect(
            '/search.html?submitted=True&searchmethod=' + searchmethod + '&searchvalue=' + searchvalue)
    else:

        if 'submitted' in request.GET:
            submitted = True
        if 'searchmethod' in request.GET:
            searchmethod = request.GET.get("searchmethod")
        if 'searchvalue' in request.GET:
            searchvalue = request.GET.get("searchvalue")

        try:
            if searchmethod == "book_id":
                books = Book.objects.filter(id=int(searchvalue))
            elif searchmethod == "name":
                books = Book.objects.filter(name=searchvalue)
            elif searchmethod == "user":
                user = User.objects.get(username=searchvalue)

                books = Book.objects.filter(username=user)



        except Exception:
            books = None
            book = None

    return render(request,
                  'bookMng/search.html',
                  {

                      'searchmethod': searchmethod,
                      'searchvalue': searchvalue,
                      "books": books,

                      'submitted': submitted,
                      'item_list': MainMenu.objects.all(),
                  })


# ---------------------------------=--------------------------
def postrate(request, book_id):
    book = Book.objects.get(id=book_id)
    submitted = False
    if request.method == 'POST':
        form = RateForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            rate = form.save(commit=False)
            try:
                rate.username = request.user
                rate.b_id = book.id
            except Exception:
                pass
            rate.save()
            return HttpResponseRedirect('/postRatingpost?submitted=True')
    else:
        form = RateForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/postRating.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                      'book': book
                  })


def postRatingpost(request):
    submitted = False
    if request.method == 'POST':
        form = RateForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            rate = form.save(commit=False)
            try:
                rate.username = request.user
            except Exception:
                pass
            rate.save()
            return HttpResponseRedirect('/postRatingpost?submitted=True')
    else:
        form = RateForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request,
                  'bookMng/postRating.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,

                  })


def rate_detail(request, comment_id):
    rate = Comment.objects.get(id=comment_id)

    return render(request,
                  'bookMng/rate_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'rate': rate,
                  })
