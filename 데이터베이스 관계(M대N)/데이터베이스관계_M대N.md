# Manay to many relationship
3. M:N
  - 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
  - 양쪽 모두에서 N:1 관계를 가짐(ex. 환자와 의사의 예약 시스템)

### Intro
```
데이터 모델링
    - 주어진 개념으로부터 논리적인 데이터 모데일을 구성하는 작업
    - 물리적인 데이터베이스 모델로 만들어 고객의 요구에 따라 특정 정보 시스템의 데이터베이스에 반영하는 작업

시작 전 용어 정리
    target model (ex. article)
        :  관계 필드를 가지지 않은 모델

    source model (ex. comment)
        : 관계 필드를 가진 모델

 N:1의 한계
    동일한 환자지만 다른 의사에게 예약하기 위해서는 객체를 하나 더 만들어서 예약을 진행해야 함
        - 새로운 환자 객체를 생성할 수 밖에 없음
    외래 키 컬럼에 '1, 2'형태로 참조하는 것은 Integer 타입이 아니기 때문에 불가능

    그렇다면 "예약 테이블을 따로 만들자"

# ManyToManyField

# 'related_name' argument

# 'through' argument
```
```
M:N 관계로 맺어진 두 테이블에는 변화가 없음

Django의 ManyToManyField은 중개 테이블을 자동으로 생성함

Django의 ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
    - 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것

N:1은 완전한 종속 관계였지만 M:N은 의사에게 진찰받느 환자, 환자를 진찰하는 의사의 두 가지 형태로 모두 표현이 가능한 것
```

# ManyToManyField
```
ManyToManyField(to, **options)

다대다 (M:N, many-to-many) 관계 설정 시 사용하는 모델 필드

하나의 필수 위치인자(M:N 관계로 설정할 모델 클래스)가 필요

모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 만들 수 있음
    - add(), remove(), create(), clear() ...

1. related_name
    - target model이 source model을 참조할 때 사용할 manager name
    - ForeignKey의 related_name과 동일

2. through
    - 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델로 지정
    - 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우(extra data with a many-to-many relationship)에 사용됨

3. symmetrical
    - 기본 값 : True
    - ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용
    - 대칭을 원하지 않는 경우 False로 설정

methods
    add()
     - 지정된 객체를 관련 객체 집합에 추가
     - 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
     - 모델 인스턴스, 필드 값(PK)을 인자로 허용
    remove()
     - 관련 객체 집합에서 지정된 모델 개체를 제거
     - 내부적으로 QuerySet.delete()를 사용하여 관계가 삭제됨
     - 모델 인스턴스, 필드 값(PK)을 인자로 허용
```
# M:N (Article-User)
- Article과 User의 M:N 관계 설정을 통한 좋아요 기능 구현하기

## LIKE
```
# articles/models.py
class Article(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

like_users 필드 생성 시 자동으로 역참조에는 .article_set 매니저가 생성됨

그러나 이전 N:1(Article-User) 관계에서 이미 해당 매니저를 사용 중
    - user.article_set.all() -> 해당 유저가 작성한 모든 게시글 조회
    - "user가 작성한 글들(user.article_set)과 user가 좋아요를 누른 글(user.article_set)을 구분할 수 없게 됨"

user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 related_name을 작성해야 함
```
```
모델 관계 설정
- User - Article간 사용 가능한 related manager 정리
    - article.user
        - 게시글을 작성한 유저 - N:1

    - user.article_set
        - 유저가 작성한 게시글(역참조) - N:1

    - article.like_users
        - 게시글을 좋아요한 유저 - M:N

    - user.like_articles
        - 유저가 좋아요한 게시글(역참조) - M:N
```
```
# articles / urls.py

urlpatterns = [
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```
```
# articles / views.py

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        
        # 현재 게시글에 좋아요를 누른 유저중에 현재 좋아요를 요청하는 유저를 검색해서 존재하는지를 확인
        if article.like_users.filter(pk=request.user.pk).exists():

        # 현재 게시글에 좋아요를 누른 유저 목록에 현재 좋아요를 요청하는 유저가 있는지 없는지 확인
        # if request.user in article.like_users.all():
            # 좋아요 취소 (remove)
            article.like_users.remove(request.user)
        else:
            # 좋아요 추가 (add)
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')
```
```
# articles / templates / articles/ index.html

<div>
    <form action="{% url 'articles:likes' article.pk %}" method="POST">
    {% csrf_token %}
    {% if request.user in article.like_users.all %}
        <input type="Submit" valie="좋아요 취소">
    {% else %}
        <input type="Submit" value="좋아요">
    {% endif %}
    </form>
</div>
```
```
# articles / forms.py

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ('user', 'like_users',)
```

# M:N (User-User)
- User 자기 자신과의 M:N 관계 설정을 통한 팔로우 기능 구현하기

## Profile
- 자연스러운 follow 흐름을 위한 프로필 페이지를 먼저 작성
```
# accounts / urls.py
urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
]

```
```
# accounts / views.py

from django.contrib.auth import get_user_model

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```
```
# accounts / templates / accounts / profile.html

{% extends 'base.html' %}

{% block content %}
    <h1>{{ person.username }}님의 프로필</h1>

    <hr>

    <h2>{{ person.username }}'s 게시글</h2>
    {% for article in person.article_set.all %}
        <div>{{ article.title }}</div>
    {% endfor %}

    <hr>

    <h2>{{ person.username }}'s 댓글</h2>
    {% for comment in person.comment_set.all %}
        <div>{{ comment.content }}</div>
    {% endfor %}

    <hr>

    <h2>{{ person.username }}'s 좋아요한 게시글</h2>
    {% for article in person.like_articles.all %}
        <div>{{ article.title }}</div>
    {% endfor %}

    <hr>

    <a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}
```
```
# templates / base.html

<body>
  <div class="container">
    {% if request.user.is_authenticated %}
        <div class="container">
        {% if request.user.is_authenticated %}
            <h3>Hello, {{ user }}</h3>
            <a href="{% url 'accounts:profile' user.username %}">내 프로필</a>

```
```
# articles / templates / articles / index.html

<p>
    <b>작성자: <a herf="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b>
</p>
```

## Follow
```
# accounts / models.py

class User(AbatractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

python manage.py makemigrations
python manage.py migrate
```
```
accounts / ulr.py

urlpatterns = [
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    ]
```
```
# acoounts . views.py

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        person = User.objects.get(pk=user_pk)
        if person != request.user:
            # 너의 팔로우 목록에 나의 pk가 있다면
            if person.followers.filter(pk=request.user.pk).exists():
            # 내가 (request.user)그 사람의 팔로워 목록에 있다면
            #if request.user in person.followers.all():
                person.followers.remove(request.user)
                # 언팔로우
            else:
                person.followers.add(request.user)
                # 팔로우
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')
```

```
# accounts / templates / accounts / profile.html

{% extends 'base.html' %}

{% block content %}
    <h1>{{ person.username }}님의 프로필</h1>
    <div>
        팔로워 : {{ person.followers.all|length }} / 팔로잉 : {{ person.followings.all|length }}
    </div>

    <hr>
    {% if request.user != person %}
    <div>
        <form action="{% url 'accounts:follow' person.pk %}" method="POST">
            {% csrf_token %}
            {% if request.user in person.followers.all %}
                <input type="submit" value="언팔로우">
            {% else %}
                <input type="submit" value="팔로우">
            {% endif %}
        </form>
    </div>
```