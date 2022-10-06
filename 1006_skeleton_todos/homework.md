# 1. User Model BooleanField
### Django에서 기본적으로 사용하는 User 모델은 AbstractUser 모델을 상속받아 정의된다.

- 아래의 models.py를 참고하여 User 모델에서 사용할 수 있는 칼럼 중 BooleanField로 정의 된 컬럼을 모두 작성하시오.

https://github.com/django/django/blob/master/django/contrib/auth/models.py

```
is_staff
is_active
is_superuser
```

# ❖ Modeling
### 편의점 상품 관리 프로그램을 제작하기 위해 모델링을 해야 하는 업무가 주어졌다. "모델링"은 개발해야 할 소프트웨어의 밑그림으로써 반드시 먼저 고려해야 할 중요한 요소 중 하나이다.

# ❖ ERD
### 다음 조건을 참고하여 ERD와 models.py를 자유롭게 작성하고, 작성한 모델링에 대한 소개한 작성하게 된 이유에 대해 간략히 작성하고 발표하시오.
1) 지점별 편의점들이 존재한다.
2) 각 상품들은 특정 조건별로 분류 할 수 있다.
3) 단, User는 고려하지 않는다.

# ❖ ERD 작성 TOOL

https://www.erdcloud.com/

https://app.diagrams.net/

![ERD](https://user-images.githubusercontent.com/104968672/194272943-b9bc9229-da2a-453f-8771-7ca1c6d4d5f0.JPG)

```
from django.db import models
from django.conf import settings
# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=20)
    address = models.TextField()
    product_name = models.CharField(max_length=20)
    product_quantity = models.IntegerField()
    product_price = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=10)
    count = models.IntegerField()
```

- 간소하게만 구성했는데 My_store와 My_products 2개의 테이블을 만들고  PK는 각각 store_name과 product_name이다. 상품의 경우 '단일 품목'이면 개수로 입력 받아도 될 거 같고 의류나 종류가 여러가지일 경우 사이즈별 재고가 다를 수 있어서 디테일하게들어가면 테이블을 더욱 세부적으로 나눠야할 거 같다. 