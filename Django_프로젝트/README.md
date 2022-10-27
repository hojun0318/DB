# 05_pjt DB를 활용한 웹 페이지 구현

![index](https://user-images.githubusercontent.com/104968672/194585157-a0284e67-7e38-47af-a27a-c3dd624960d5.png)

![detail](https://user-images.githubusercontent.com/104968672/194585226-23e23879-aef5-444f-8e07-edf03eff54c4.png)

# movies\forms.py
### 새로 구현한 방법
- 04_pjt에서는 edit.html에서 select에 option을 주어서 장르를 선택하게 했는데 이번에는 forms.py에서 Form을 만들어 구현했다.
```
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    genre_1 = '코미디'
    genre_2 = '공포/스릴러'
    genre_3 = '액션'
    genre_4 = '전쟁'
    genre_5 = 'SF'
    genre_6 = '느와르'
    genre_7 = '스포츠'
    genre_8 = '뮤지컬'
    genre_9 = '로맨스'
    genre_10 = '드라마'

    GENRE_CASE = [
        (genre_1, '코미디'),
        (genre_2, '공포/스릴러'),
        (genre_3, '액션'),
        (genre_4, '전쟁'),
        (genre_5, 'SF'),
        (genre_6, '느와르'),
        (genre_7, '스포츠'),
        (genre_8, '뮤지컬'),
        (genre_9, '로맨스'),
        (genre_10, '드라마'),
    ]

    genre = forms.ChoiceField(choices=GENRE_CASE, widget=forms.Select())

    score = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'step': '.1',
                'min': '0',
                'max': '10',
            }
        )
    )

    release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Movie
        fields = '__all__'
```


# movies\views.py
### 느낀점
- decorator를 전부 삭제했다. 굳이 없어도 문제없을 거 같았는데.. 솔직히 아직 개념을 완전히 이해하지 못한 상태다. 복습을 통해서 CRUD 구현하고 나서 decorator 적용 방법을 확실히 이해해야겠다.
```
from movies.models import Movie
from movies.forms import MovieForm
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    movies = Movie.objects.order_by('pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()

    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)

    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    return redirect('movies:detail', movie.pk)
```

# movies\templates\movies\index.html
### 새로 구현한 방법
- 기존 pdf 파일은 영화 제목을 클릭하면 detail로 넘어가는 방법인데 사진을 클릭하면 넘어가는 걸로 적용했다.
### 느낀점
- text를 center로 옮기기거나, style을 적용하거나 margin이나 padding을 얼마나 주느냐 오래돼서 찾아보면서 했다. 복습이 필요하다.
```
{% extends 'base.html' %}

{% block content %}
<br>
<div>
  <h1 class='text-center' style='font-weight: bolder'>INDEX</h1>
  <a href="{% url 'movies:create' %}">
    <button type="button" class="btn btn-primary">CREATE</button>
  </a>
</div>
<br>
<div class='row row-cols-1 row-cols-md-5 g-4'>
  {% for movie in movies %}
    <div class='col'>
      <div class='card h-200'>
        <a href="{% url 'movies:detail' movie.pk %}">
          <img src="{{ movie.poster_url }}" class='card-img-top' alt="그림">
        </a>
        <div class='card-body'>
          <h5 class='text-center' style='font-weight: bold'>{{ movie.title }}</h5>
          <h6 class='text-center' style='font-weight: bold'>{{ movie.genre }} / {{ movie.score }}</h6>
        </div>
      </div>
    </div>
  {% endfor %}
</div>
{% endblock content %}
```

![create](https://user-images.githubusercontent.com/104968672/194585323-0aa11912-ad49-45b4-b2d0-ac94f6ad2733.png)

![update](https://user-images.githubusercontent.com/104968672/194585417-4777ba9e-9042-412d-a024-571df1115536.png)

# movies\templates\movies\update.html
### 느낀점
- 04_pjt에서 사용한 방법을 그대로 일단 썼다. reset 기능을 적용하여 CANCLE 버튼을 누르면 수정 전 원래 상태로 돌아오는데, 텍스트 전체가 백지로 돌아가는 기능이 있는 지 찾아봐야겠다.
```
{% extends 'base.html' %}

{% block content %}
  <br>
  <h1 class='text-center' style='font-weight: bolder'>UPDATE</h1>
  <hr>
  <form action="{% url 'movies:update' movie.pk %}" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="UPDATE">
      <input type="reset" value="CANCLE">
  </form>
  <br>
  <a href="{% url 'movies:detail' movie.pk %}">
    <button type="button" class="btn btn-warning">BACK</button>
  </a>
{% endblock content %}
```