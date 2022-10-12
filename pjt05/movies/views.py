from movies.models import Movie, Comment
from movies.forms import MovieForm, CommentForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST, require_safe


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.order_by('pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comment_form': comment_form,
        'comments' : comments,        
    }
    return render(request, 'movies/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user:
        if request.method == "POST":
            form = MovieForm(request.POST, request.FILES, instance=movie)
            if form.is_valid():
                movie = form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
    else:
        return redirect('movies:index')
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)


@require_POST
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == movie.user:
            movie.delete()
            return redirect('movies:index')
    return redirect('movies:detail', movie.pk)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
        return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')


def comments_delete(request, movie_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:detail', movie_pk)


@require_POST
def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        
        # 현재 게시글에 좋아요를 누른 유저중에 현재 좋아요를 요청하는 유저를 검색해서 존재하는지를 확인
        if movie.like_users.filter(pk=request.user.pk).exists():

        # 현재 게시글에 좋아요를 누른 유저 목록에 현재 좋아요를 요청하는 유저가 있는지 없는지 확인
        # if request.user in movie.like_users.all():
            # 좋아요 취소 (remove)
            movie.like_users.remove(request.user)
        else:
            # 좋아요 추가 (add)
            movie.like_users.add(request.user)
        return redirect('movies:index')
    return redirect('accounts:login')