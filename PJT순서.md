# 기본 설정

### 가상환경 활성화 - 패키지 설치 - 프로젝트 생성 - 앱 생성
```
python -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt

django-admin startprojects '생성할 프로젝트 이름' .

python manage.py startapp '생성할 앱 이름'
```

### 프로젝트 파일 \ settings.py
```
INSTALLED_APPS에 '생성한 앱 이름' 추가
TEMPLATES에서 DIRS에 [BASE_DIR / 'templates',], 추가
```

### 프로젝트 파일 \ urls.py
```
# '생성한 앱'의 urls를 사용하기 위해 include 추가

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('생성한 앱 이름.url')),
]

# 사이트 urls에서 movies까지는 처리하고 나머지 url은 생성한 앱의 url에서 처리하겠다는 뜻
```

### templates \ base.html
```
생성한 앱의 templates에 상속하기 위해 base.html의 body에 {% block content%} {% endblock content %} 생성

부트스트랩 링크 2개 넣기
1. head 안에
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">

2. bdoy 안에
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
```

![개요](https://user-images.githubusercontent.com/104968672/194698786-8840c7cd-2133-4ed9-a8be-5bf5a7309978.jpg)

# 1. '생성한 앱' \ models.py
### 모델 클래스를 작성하는 것은 데이터베이스 '테이블의 스키마를 정의' 하는 것
- 모델 클래스 == 테이블 스키마
```
# 각각 유형에 맞는 필드 타입 설정, null=True 입력하지 않아도 저장 가능하도록 하기
# models.py 수정/추가 시 migrate 해주기

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField(null=True)
    release_date = models.DateField(null=True)
    genre = models.CharField(max_length=30, null=True)
    score = models.FloatField(null=True)
    poster_url = models.TextField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title

# title : 필드 이름
# models.CharField() : 타입
즉 데이터베이스의 스키마(뼈대)를 만들고 있는 것
```

### null=True vs blank=True의 차이
```
null과 blank는 둘 다 기본값이 False이다. 이 두 설정은 모두 field(열) 수준에서 동작한다.
즉, field(열)를 비워두는 것을 허용할 것인지를 설정한다.

null=True는 field의 값이 NULL(정보 없음)로 저장된느 것을 허용한다. 결국 데이터베이스 열에 관한 설정이다.

blank=True는 field가 Form(입력 양식)에서 빈 채로 저장되는 것을 허용한다.
장고 관리자(admin) 및 직접 정의한 Form에도 반영된다.

null=True 와 blank=True를 모두 지정하면 어떤 조건으로든 값을 비워둘 수 있음을 의미한다.

epic = models.ForeignKey(null=True, blank=True)
# 단, CharFields()와 TextFields()에서는 예외입니다.
# 장고는 이 경우 NULL을 저장하지 않으며, 빈 값을 빈 문자열('')로 저장한다.

또 하나의 예외적인 경우는 BooleanField에 NULL을 입력할 수 있도록 하려면 null=True를 설정하는 것이 아니라, NullBooleanField를 사용해야 한다.

[출처] https://django-orm-cookbook-ko.readthedocs.io/en/latest/null_vs_blank.html
```

## 1-1. Migrations
```
# migrations은 청사진을 만드는 과정
# migrate는 migrations로 만든 설계도를 실제 데이터베이스에 반영하는 과정 (db.sqlite3 파일에 반영)
# 결과적으로 '모델의 변경사항'과 데이터베이스를 동기화

python manage.py makemigrations

python manage.py migrate

# [참고] Migrations 기타 명령어

python manage.py showmigrations
    # migrations 파일들이 migrate 됐는 지 안됐는 지 여부를 확인하는 용도
    # [X] 표시가 있으면 migrate가 완료됐음을 의미

python manage.py sqlmigrate '생성한 앱 이름' 0001
    # 해당 migrations 파일이 SQL 문으로 어떻게 해석 될 지 확인할 수 있음
```

## 1-2. 프로젝트 파일 \ settings.py
```
# 실습의 편의를 위해 외부 라이브러리 추가 설치 및 설정

pip install ipython
pip install django-extensions

pip freeze > requirements.txt
    패키지 목록 업데이트

INSTALLED_APPS에 'django_extensions' 추가
# 이 앱을 등록해야 shell_plus 사용 가능
```

# 2. '생성한 앱' \ urls.py
```
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```

# 3. '생성한 앱' \ views.py
```
from django.shortcuts import render, redirect
from .models import '생성한 Model 이름' (ex. Article, Movie)
# 명시적 상대경로
from movies.forms import '생성한 Form 이름' (ex. ArticleForm, MovieForm)
```
```
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
    # 데이터베이스에 접근하는 핵심 코드들을 POST일때만 따로 빼버리고 
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    # 관련없는 일반적인 코드들은 else문으로 퉁치겠다.
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

# 4. '생성한 앱' \ templates \ '생성한 앱 이름' \ .html
```
{% extends 'base.html' %}
{% block content %}
블락 사이에 작성하기
{% endblock content %}
```

# 5. '생성한 앱' \ forms.py
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
    # widget은 input 요소의 표현만 바꾼다. 유효성 검사와 아무런 관련이 없다.
    # [알아두기] widget=forms.RadioSelect (체크박스)
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

# 결국 사용자의 입력을 받는 부분은 앞으로 form class에서 수정/추가 해야한다.
```

# View Decorators
```
@require_safe
    : GET인 요청에 대해서만 이 View 함수에서 쓸 수 있도록 한다. GET이 아니면 View 함수 실행까지 못가고 응답 상태 코드를 하나 주는데 405 Method Not Allowed 이다.
- 요청 방법이 서버에게 전달 되었으나 사용 불가능한 상태를 뜻한다.
- 4는 Client 잘못을 뜻한다.


@require_http_methods()
    : View 함수가 특정한 요청 method만 허용하도록 하는 데코레이터
    ex) @require_http_method(['GET', 'POST'])
    : GET과 POST를 제외한 다른 요청은 전부다 Cut 된다.

@require_POST
    : View 함수가 POST 요청 method만 허용하도록 하는 데코레이터
- 단순 Cut이 아니라 적절한 응답 상태 코드를 보내주는게 장점이기도 하다.
```