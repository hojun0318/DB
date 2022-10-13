# 초기 데이터의 필요성
```
Django에서는 fixtures를 사용해 앱에 초기 데이터(initial data)를 제공할 수 있다.
즉, migrations와 fixtures를 사용하여 data와 구조를 공유하게 된다.
```

# Fixtures
```
Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음
    -가져오는 방법을 알고 있다?
        -> Django가 직접 만들기 때문에 데이터베이스 구조에 맞추어 작성 되어 있음

app_name/fixtures/ (기본경로)

- 생성 (추출)
    - dumpdata

- 로드 (불러오기)
    - loaddata
```

## dumpdata
```
응용 프로그램과 관련된 데이터베이스의 모든 데이터를 표준 출력으로 출력

여러 모델을 하나의 json 파일로 만들 수 있음

# 작성 예시
python manage.py dumpdata 앱이름.모델이름 > 앱이름.json

- 인코딩 문제 해결
    python -Xutf8 manage.py dumpdata > test2.json

manage.py와 동일한 위치에 data가 담긴 articles.json 파일이 생성됨

dumpdata의 출력 결과물은 loaddata의 입력으로 사용됨

Ex) python manage.py dumpdata --indent 4 articles.article > articles.json

    python manage.py dumpdata --indent 4 movies.movie > movies.json
    python -Xutf8 manage.py dumpdata movies.comment > comments.json
    python manage.py dumpdata --indent 4 accounts.user > users.json
```

## loaddata
```
fixtures의 내용을 검색하여 데이터베이스로 로드

# 작성 예시
python manage.py loaddata article/articles.json

하나씩 loaddata를 할 경우 User -> Article -> Comments 순으로 아니면 한방에 하기

python manage.py loaddata articles.json comments.json users.json
```