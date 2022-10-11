# STATIC_ROOT
```
Default : None
Django 프로젝트에서 사용하는 모든 정적 파일을 한곳에 모아 넣은 경로
collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
- 개발 과정에서 setting.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않음 - 
DEBUG = True 면 상세한 오류 설명(개발 과정이니), 서비스 배포시 False로 변경 필수!

# 작성 예시
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

# STATICFILES_DIRS
```
Default : [] (Empty list)
app/static/ 디렉토리 경로를 사용하는 것(기본 경로) 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트

# 작성 예시
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

# STATIC_URL
```
Default : None
STATIC_ROOT에 있는 정적 파일을 참조 할 때 사용할 URL
개발 단계에서는 실제 정적 파일들이 저장되어 있는 app/static/ 경로(기본 경로) 및 STATICFILES_DIRS에 정의된 추가 경로들을 탐색
- 실제 파일이나 디렉토리가 아니며, URL로만 존재
비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함

# 작성 예시
STATIC_URL = '/static/'
```

# static file을 가져오는 2가지 방법
1. 기본 경로에 있는 static file 가져오기
```
'생성한 앱' / static / '생성한 앱' 경로에 이미지 파일 배치하기
```
2. 추가 경로에 있는 static file 가져오기
```
# settings.py에 작성
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# 최상단에 경로에 static 파일 생성

# 파일에 이미지 넣기

# indext.html에서 extends 아래에 {% load static %} 작성

# img url 작성
1. 기본경로
    <img src="{% static 'movies/sample_img_1.jpg' %}" alt="sample_img">
2. 추가경로
    <img src="{% static 'sample_img_2.jpg' %}" alt="sample_img">
```

# Image Upload
```
Django ImageField를 사용해 사용자가 업로드한 정적 파일(미디어 파일) 관리하기

이미지 업로드에 사용하는 모델 필드

FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능

ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경할 수 있음

FileField(upload_to='', storage=None, max_length=100, **options) - 2개의 선택 인자

# settings.py에 MEDIA_ROOT, MEDIA_URL 설정

# upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정 (선택사항)
```

# MEDIA_ROOT
```
Defalut : '' (Empty string)

사용자가 업로드 한 파일(미디어 파일)들을 보관할 디렉토리의 절대 경로

Django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음
    - 데이터베이스에 저장되는 것은 "파일 경로"

MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야 함

# 작성 예시
settings.py에 MEDIA_ROOT = BASE_DIR / 'media'
```

# MEDIA_URL
```
Defalut : '' (Empty string)

MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL

업로드 된 파일의 주소(URL)를 만들어 주는 역할
    - 웹 서버 사용자가 사용하는 publi URL

비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함

MEDIA_URL은 STATIC_URL과 반드시 다른 경로로 지정해야 함

# 작성 예시
settings.py에 MEDIA_URL = '/media/'
```

## 개발 단계에서 사용자가 업로드한 미디어 파일 제공하기

![개발 단계에서 사용자가 업로드한 미디어 파일 제공하기](https://user-images.githubusercontent.com/104968672/195090871-7b063fa6-77ae-4221-893b-a534daa20296.png)

- 사용자로부터 업로드 된 파일이 프로젝트에 업로드 되고나서, 실제로 사용자에게 제공하기 위해서는 업로드 된 파일의 URL이 필요함
    - 업로드 된 파일의 URL == settings.MEDIA_URL
    - 위 URL을 통해 참조하는 파일의 실제 위치 == settings.py MEDIA_ROOT
```
# '생성한 프로젝트' / urls.py
from django.conf import settings
from django.conf.urls.static import static

+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

# CREATE
```
python -m pip install Pillow

python manage.py makemigrations

python manage.py migrate

pip freeze > requirements.txt

# '생성한 앱' / models.py
image = models.ImageField(blank=True)

하지만 이미지가 업로드 되지 않음

파일 또는 이미지 업로드 시에는 form 태그에 enctype 속성을 다음과 같이 변경해야 함

# create.html의 form 태그에 추가
enctype="multipart/form-data"

# views.py의 create함수에 request.FILES 추가 
form = MovieForm(request.POST, request.FILES)
```

![enctype 추가](https://user-images.githubusercontent.com/104968672/195094941-2d1df665-f740-4e41-bf2c-8f44697ec448.png)

## form 태그의 enctype(인코딩) 속성 값
```
multipart/form-data

파일/ 이미지 업로드 시에 반드시 사용해야 함

전송되는 데이터의 형식을 지정

<inpurt type="file>을 사용할 경우 사용
```

# READ
```
# 작성예시 (파일의 경로, 파일 이름)
<img src="{{movie.image.url}}" alt="{{movie.image}}">

'생성한 앱'.image.url - 업로드 파일의 경로

'생성한 앱'.image - 업로드 파일의 파일 이름
```

# UPDATE
```
이미지는 Binary 데이터이기 때문에 텍스트처럼 일부만 수정 하는 것은 불가능하다. 그래서 새로운 사진으로 대체하는 방식을 사용한다.

# update.html의 form 태그에 추가
enctype="multipart/form-data"

# views.py의 create함수에 request.FILES 추가 
form = MovieForm(request.POST, request.FILES)
```

# Upload_to argument
```
1. 문자열 값이나 경로 지정 방법
    - upload_to 인자에 새로운 이미지 저장 경로를 추가 후 migration 과정 진행
    image = models.ImageField(blank=True, upload_to='images/')

    - 단순 문자열 뿐만 아니라 파이썬 time 모듈의 strftime() 형식도 포함될 수 있으며, 이는 파일 업로드 날짜/시간으로 대체 됨
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')

2. 함수 호출 방법
    - upload_to는 독특하게 함수처리 호출이 가능하며 해당 함수가 호출 되면서 반드시 2개의 인자를 받음

    # 작성방법
    def '생성한 앱'_image_path(instance, filename):
        return f'image/{instance.user.username}/{filename}'
    
    class '대문자 생성한 앱'(models.Model):
        image = models.ImageField(blank=True, upload_to='생성한 앱'_image_path)
```

# Image Resizing
```
실제 원본 이미지를 서버에 그대로 로드 하는 것은 여러 이유로 부담이 큼

HTML <img> 태그에서 직접 사이즈를 조정할 수도 있지만, 업로드 될 때 이미지 자체를 resizing 하는 것을 사용해 볼 것

pip install django-imagekit

pip freeze > requirements.txt

# settings.py에 추가
INSTALLED_APPS = [
    'imagekit',
]

썸네일 만들기
    2가지 방식으로 썸네일 만들기를 진행
        1. 원본 이미지 저장 X
            from imagekit.processors import Thumbnail
            from imagekit.models import ProcessedImageField

            class '대문자 생성한 앱'(modles.Model):
                image = ProcessedImageField(
                    blank=True,
                    upload_to='thumbnails/',
                    processors=[Thumbnail(200,300)],        # https://github.com/matthewwithanm/pilkit 문서에서 찾아 여러 클래스 다양하게 사용
                    format='JPEG',
                    options={'quality':80},
                )
            
python manage.py makemigrations

python manage.py migrate

        2. 원본 이미지 저장 O           # 썸네일 언제 만드냐? 우리가 만들고자 할 때 생성 - 출력 시점
            from imagekit.processors import Thumbnail
            from imagekit.models import ProcessedImageField, ImageSpecField

            class '대문자 생성한 앱'(modles.Model):
                image = models.ImageField(blank=True)
                image_thumbnail = ImageSpecField(
                    source='image',
                    processors=[Thumbnail(200,300)],
                    format='JPEG',
                    options={'quality':80},
                )

python manage.py makemigrations

python manage.py migrate

# '생성한 앱' / detail.html에서
{% block content %}
    {% if '생성한 앱'.image %}
        <img src="{{ '생성한 앱'.image_thumbnail.url }}" alt="{{ ='생성한 앱'.image_thumbnail }}">
    {% endif %}
```
```
django-imagekit
    - 이미지 처리를 위한 Django 앱
        - 썸네일, 해상도, 사이즈, 색깔 등을 조정할 수 있음
```