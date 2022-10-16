# Database
### 데이터베이스(DB)의 등장
- 파일을 이용한 데이터 관리
    - 우리는 일반적으로 데이터를 '파일'에 저장한다.
    - 장점
        - 운영체제에 관계 없이 어디에서나 쉽게 사용 가능
        - 이메일이나 메신저를 이용해 간편하게 전송 가능
    - 단점
        - 성능과 보안적 측면에서 한계가 명확
        - 대용량 데이터를 다루기에 적합하지 않음
        - 데이터를 구조적으로 정리하기에 어려움
        - 확장이 불가능한 구조

- 스프레드 시트(Spread Sheet)를 이용한 데이터 관리
    - 스프레드 시트(엑셀 시트)을 사용
    - 스프레드 시트는 컬럼(열)을 통해 데이터의 유형을 지정하고 레코드(행)을 통해 구체적인 데이터 값을 포함
    - 스프레드 시트 자체를 데이터베이스라고 부를 수는 없지만, 데이터베이스로 가는 길목 정도로 생각해볼 수 있음

- 스프레드 시트와 달리 프로그래밍 언어를 사용해 작동 시킬 수 있음
- 데이터베이스는 많은 형태가 있지만 실제 가장 많이 쓰이는 유형은 RDB(Relational Database)라고 부르는 '관계형 데이터베이스'
- RDB는 각각의 데이터를 테이블에 기입함(마치 스프레드 시트에 작성하는 것처럼)
- 쉽게 생각하면 스프레드 시트 파일 모음을 관계형 RDB라고 생각하자!

### Database 정의
- 체계화된 데이터의 모임
- 여러 사함이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 검색, 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템
    - 내용을 고도로 구조화 함으로써 검색과 갱신의 효율화를 꾀한 것
    - 즉, 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 구조화하여 기억시켜 놓은 자료의 집합체
- 이러한 Database를 조작하는 프로그램 = DBMS(Database Management System)
    - 한 번쯤 들어봤을 Oracle MySQL, SQLite 등이 모두 DBMS
    - DBMS에서 Database를 조작하기 위해 사용하는 언어를 SQL이라 함
- 웹 개발에서 대부분의 데이터베이스는 '관계형 데이터베이스 관리 시스템(RDBMS')을 사용하여 SQL로 데이터와 프로그래밍을 구성

# RDB
### RDB란
- Relational Database (관게형 데이터베이스)
- 데이터를 테이블, 행, 열 등으로 나누어 구조화 하는 방식
- 자료를 여러 테이블로 나누어서 관리하고, 이 테이블간 관계를 설정해 여러 데이터를 쉽게 조작할 수 있다는 장점이 있음
- SQL을 사용하여 데이터를 조회하고 조작

### 기본 구조
1. 스키마
2. 테이블
    - 필드
    - 레코드
    - 기본 키

### 스키마
- 테이블의 구조(Structure)
- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등 전반적인 명세를 기술한 것

### 테이블
- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
- 관계(Relation)라고도 부름

1. 필드(field)
    - 속성, 컬럼(Column)
2. 레코드(record)
    - 튜플, 행(Row)

### 필드(field)
- 튜플 혹은 행(row)
- 테이블의 데이터는 레코드에 저장됨

### PK(Primary Key)
- 기본 키
- 각 레코드의 고유한 값
    - 각각의 데이터를 구분할 수 있는 고윳값
- 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(unique)
- 데이터베이스 관리 및 테이블

### 관계형 데이터베이스의 이점
- 데이터를 직관적으로 표현할 수 있음
- 관련한 각 데이터에 쉽게 접근할 수 있음
- 대량의 데이터도 효율적으로 관리 가능

### RDBMS
- Relational Database Management System (관계형 데이터베이스 관리 시스템)
- 관계형 데이터베이스를 만들고 업데이트하고 관리하는 데 사용하는 프로그램
- 예시
    - SQLite, MySQL, PostgreSQL, Microsoft SQL Server, Oracle Database 등

### SQLite
- 응용 프로그램에 파일 형식으로 넣어 사용하는 비교적 가벼운 데이터베이스
- 안드로이드, iOS, macOS에 기본적으로 탑재되어 있으며, 임베디드 소프트웨어에서도 많이 활용됨
- 오픈 소스 프로젝트이기 때문에 자유롭게 사용 가능

### SQLite 단점
- 대규모 동시 처리 작업에는 적합하지 않음
- 다른 RDBMS에서 지원하는 SQL 기능을 지원하지 않을 수 있음

### SQLite를 학습하는 이유
- 어떤 환경에서나 실행 가능한 호환성
- 데이터 타입이 비교적 적고 강하지 않기 때문에 유연한 학습 환경을 제공
- Django Framework의 기본 데이터베이스

# SQL
### SQL이란
- "Structured Query Language"
- RDBMS의 데이터를 관리하기 위해 설계된 '특수 목적의 프로그래밍 언어'
- RDBMS에서 데이터베이스 스키마를 생성 및 수정할 수 있으며, 테이블에서의 자료 검색 및 관리도 할 수 있음
- 데이터베이스 객체에 대한 처리를 관리하거나 접근 권한을 설정하여 허가된 사용자만 RDBMS를 관리할 수 있도록 할 수 있음
- 많은 데이터베이스 관련 프로그램들이 SQL을 표준으로 채택하고 있음

### SQL 정리
- SQL은 데이터베이스와 상호작용하는 방법
- 따라서 SQL을 배우면서 데이터베이스의 동작원리 또한 익힐 수 있음

# SQL Commands
### SQL Commands 종류
- 명령어는 특성에 따라 다음 3가지 그룹으로 분류
    1. DDL (Data Definition Language)
    2. DML (Data Manipulation Language)
    3. DCL (Data Control Language)

- DDL (데이터 정의 언어) : 관계형 데이터베이스 구조(테이블, 스키마)를 정의(생성, 수정 및 삭제)하기 위한 명령어
    - CREATE
    - ALTER
    - DROP
    - TRUNCATE

- DML (데이터 조작 언어) : 데이터를 조작(추가, 조회, 변경, 삭제)하기 위한 명령어
    - SELECT
    - INSERT
    - UPDATE
    - DELETE

- DCL (데이터 제어 언어) : 데이터의 보안, 수행 제어, 사용자 권한 부여 등을 정의하기 위한 명령어
    - GRANT
    - REVOKE
    - COMMIT
    - ROLLBACK

# SQL Syntax
### SQL Syntax

- 모든 SQL 문(statement)는 SELECT, INSERT, UPDATE 등과 같은 키워드로 시작하고, 하나의 statement는 세미콜론(;)으로 끝남
- SQL 키워드는 대소문자를 구분하지 않음
    - 즉, SELECT와 select는 SQL 문에서 동일한 의미
    - 하지만 대문자로 작성하는 것을 권장
- SQL에 대한 세부적인 문법 사항들을 이어지는 DDL, DML을 진행하며 익혀볼 것\

### [참고] Statement & Clause
- Statement (문)
    - 독립적으로 실행할 수 있는 완전한 코드 조각
    - statement는 clause로 구성됨
- Clause (절)
    - statement의 하위 단위

- SELECT statement라 부름
- 이 statement는 다음과 같이 2개의 clause로 구성됨
    1. SELECT column_name
    2. FROM table_name

# DDL
```
Data definition

SQL 데이터 정의 언어를 사용하여 테이블 데이터베이스 개체를 만드는 방법을 학습

DDL은 테이블 구조를 관리
    - CREATE, ALTER, DROP
```

# CREATE TABLE
```
CREATE TABLE contacts (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE
);
```

### SQLite Data Types
1. NULL
    - NULL value
    - 정보가 없거나 알 수 없음을 의미(missing informagion or unknown)

2. INTEGER
    - 정수
    - 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트와 같으 가변 크기를 가짐

3. REAL
    - 실수
    - 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수

4. TEXT
    - 문자 데이터

5. BLOB(Binary Large Object)
    - 입력된 그대로 저장된 데이터 덩어리 (대용 타입 없음)
    - 바이너리 등 멀티미디어 파일
    - 예시
        - 이미지 데이터

### Constraints
```
제약조건

입력하는 자료에 대한 제약을 정함

제약에 맞지 않다면 입력이 거부됨

사용자가 원하는 조건의 데이터만 유지하기 위한 즉, 데이터의 무결성을 유지하기 위한 보편적인 방법으로 테이블의 특정 컬럼에 설정하는 제약
```

### 데이터 무결성
```
데이터 베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 두어 데이터의 정확성을 보증하는 것
    - 무결성이란 데이터의 정확성, 일관성을 나타냄

데이터베이스에 저장된 데이터의 무결성을 보장하고 데이터베이스의 상태를 일관되게 유지하는 것이 목적
```

### Contraints 종류
1. NOT NULL
    - 컬럼이 NULL 값을 허용하지 않도록 지정
    - 기본적으로 테이블의 모든 컬럼은 NOT NULL 제약 조건을 명시적으로 사용하는 경우를 제외하고는 NULL 값을 허용함

2. UNIQUE
    - 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함

3. PRIMARY KEY
    - 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼
    - 각 테이블에는 하나의 기본 키만 있음
    - 암시적으로 NOT NULL 제약 조건이 포함되어 있음
```
# 예시

CREATE TABLE table_name (
    id INTEGER PRIMARY KEY,
);

#주의 : INTEGER 타입에만 사용가능 (INT BIGINT 등 불가능)
```

4. AUTOINCREMENT
    - 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
    - INTEGER PRIMARY KEY 다음에 작성하면 해당 rowid를 다시 재사용하지 못하도록 함
```
# 예시

CREATE TABLE table_name (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
);
```

# ALTER TABLE
- 기존 테이블의 구조를 수정(변경)
```
# 1. Rename a table
'ALTER TABLE' table_name 'RENAME TO' new_table_name;

# 2. Rename a column
'ALTER TABLE' table_name 'RENAME COLUMN' column_name 'TO' new_column_name;

# 3. Add a new column to a table
'ALTER TABLE' table_name 'ADD COLUMN' column_definition 'NOT NULL DEFAULT' 'no address';
    이렇게 하면 address 컬럼이 추가되면서 기존에 있던 데이터들의 address 컬럼값은 'no address'가 됨
# 4. Delete a column
'ALTER TABLE' table_name 'DROP COLUMN' column_name;
    단, 삭제하지 못하는 경우가 있음
        - 컬럼이 다른 부분에서 참조되는 경우
            - FOREIGN KEY(외래 키) 제약조건에서 사용되는 경우
        - PRIMARY KEY인 경우
        - UNIQUE 제약 조건이 있는 경우
```

# DROP TABLE
```
# 데이터베이스에서 테이블을 제거
'DROP TABLE' table_name;

# 존재하지 않는 테이블을 제거하면 SQLite에서 오류가 발생
no such table: table_name

한 번에 하나의 테이블만 삭제할 수 있음

여러 테이블을 제거하려면 여러 DROP TABLE 문을 실행해야 함

DROP TABLE 문은 실행 취소하거나 복구할 수 었다. 따라서 각별히 주의하여 수행해야 함
```

# DML
```
DML을 통해 데이터를 조작하기 (CRUD)

INSERT, SELECT, UPDATE, DELETE
```

- 사전 준비
```
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL,
)
```

### Simple query
- SELECT 문을 사용하여 간단하게 단일 테이블에서 데이터를 조회하기
```
# 예시
SELECT column1, column2 FROM table_name;

특정 테이블에서 데이터를 조회하기 위해 사용

문법 규칙
    - SELECT 절에서 컬럼 또는 쉼표로 구분된 컬럼 목록을 지정
    - FROM 절(clause)에서 데이터를 가져올 테이블을 지정

다양한 절과 함께 사용할 수 있으며 하나씩 학습할 예정
    1. ORDER BY
    2. DISTINCT
    3. WHERE
    4. LIMIT
    5. LIKE
    6. GROUP BY
```
```
# 이름과 나이 조회하기
SELECT first_name, age FROM users;

# 전체 데이터 조회하기
SELECT * FROM users;

# rowid 컬럼은 다음과 같이 조회할 수 있음
SELECT rowid, first_name FROM users;
```

### Sorting rows
- ORDER BY 절을 사용하여 쿼리의 결과를 정렬하기
```
# 예시
SELECT select_list FROM table_name ORDER BY column_1 ASC, column_2 DESC;

SELECT 문에 추가하여 결과를 정렬

ORDER BY 절은 FROM 절 뒤에 위치함

하나 이상의 컬럼을 기준으로 결과를 오름차순, 내림차순으로 정렬할 수 있음

이를 위해 ORDER BY 절 다음에 'ASC' 또는 'DESC' 키워드를 사용
    - ASC : 오름차순 (기본 값)
    - DESE : 내림차순

```
```
# 이름과 나이를 나이가 어린 순서대로 조회하기
SELECT first_name, age FROM users ORDER BY age ASC;

SELECT first_name, age FROM users ORDER BY age;

# 이름과 나이를 나이가 많은 순서대로 조회하기
SELECT first_name, age FROM users ORDER BY age DESC;

# 이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회하기
SELECT first_name, age, balance FROM users OREDR BY age ASC, balance DESC;

정렬과 관려하여 SQLite는 NULL을 다른 값보다 작은 것으로 간주

즉, ASC를 사용하는 경우 결과의 시작 부분에 NULL이 표시되고, DESC를 사용하는 경우 결과의 끝에 NULL이 표시됨
```

### Filtering data
- 데이터를 필터링하여 중복 제거, 조건 설정 등 쿼리를 제어하기
- Clause
    - SELECT DISTINCT
    - WHERE
    - LIMIT

- Operator
    - LIKE
    - IN
    - BETWEEN

**SELECT DISTINCT clause**
```
# 조회 결과에서 중복된 행을 제거
SELECT DISTINCT select_list FROM table_name;

DISTINCT 절은 SELECT에서 선택적으로 사용할 수 있는 절

문법 규칙
    - DISTINCT 절은 SELECT 키워드 바로 뒤에 나타나야 함
    - DISTINCT 키워드 뒤에 컬럼 또는 컬럼 목록을 작성
```
```
# 모든 지역 조회하기
SELECT country FROM users;

# 중복없이 보든 지역 조회하기
SELECT DISTINCT country FROM users;

# 지역 순으로 오름차순 정렬하여 중복없이 모든 지역 조회하기
SELECT DISTINCT country FROM users ORDER BY country;

# 이름과 지역이 중복 없이 모든 이름과 지역 조회하기
SELECT DISTINCT first_name, country FROM users;
    각 컬럼의 중복을 따로 계산하는 것이 아니라 두 컬럼을 하나의 집합으로 보고 중복을 제거

# 이름과 지역 중복 없이 지역 순으로 오름차순 정렬하여 모든 이름과 지역 조회하기
SELECT DISTINCT first_name, country FROM users OREDR BY country;

SQLite는 NULL 값을 중복으로 간주

NULL 값이 있는 컬럼에 DISTINCT 절을 사용하면 SQLite는 NULL 값의 한 행을 유지
```

**WHERE clause**
```
# 조회 시 특정 검색 조건을 지정
SELECT column_list FROM users WHERE search_condition;

WHERE 절은 SELECT 문에서 선택적으로 사용할 수 있는 절
    - SELECT 문 외에도 UPDATE 및 DELETE 문에서 WHERE 절을 사용할 수 있음
FROM 절 뒤에 작성
```
```
# 작성 예시
WHERE column_1 = 10

WHERE column_2 LIKE 'Ko%'

WHERE column_3 IN (1, 2)

WHERE column_4 BETWEEN 10 AND 20
```
```
# 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT first_name, age, balance FROM users WHERE age >= 30;

# 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT first_name, age, balance FROM users WHERE age >= 30 AND balanve > 500000;
```

**LIKE operator**
```
패턴 일치를 기반으로 데이터를 조회

SELECT, DELETE, UPDATE 문의 WHERE 절에서 사용

기본적으로 대소문자를 구분하지 않음
    - 'A' LIKE 'a' 는 true

SQLite는 패턴 구성을 위한 두 개의 와일드 카드(wildcards)를 제공

1. % (percent)
    - 0개 이상의 문자가 올 수 있음을 의미

# '%' wildcard 예시
    - '영%' 패턴은 영으로 시작하는 모든 문자열과 일치 (영, 영미, 영미리 등)
    - '%도' 패턴은 도로 끝나는 모든 문자열과 일치 (도, 수도, 경기도 등)
    - '%강원%' 패턴은 강원을 포함하는 모든 문자열과 일치 (강원, 강원도, 강원도에 살아요 등)

2. _ (underscore)
    - 단일(1개) 문자가 있음을 의미

# '_' wildcard 예시
    - '영_' 패턴은 영으로 시작하고 총 2자리인 문자열과 일치 (영미, 영수, 영호 등)
    - '_도' 패턴은 도로 끝나고 총 2자라인 문자열과 일치 (수도, 과도 등)
```
```
Wildcard 종합 예시
2%              2로 시작하는 패턴
%2              2로 끝나는 패턴
%2%             2를 포함하는 패턴
_2%             첫번째 자리에 아무 값이 하나 있고 두 번째가 2로 시작하는 패턴 (최소 2자리)
1___            1로 시작하는 4자리 패턴 (반드시 4자리)
2_%_% or 2__%   2로 시작하고 최소 3자리인 패턴 (3자리 이상)

파일을 지정할 때, 구체적인 이름 대신에 여러 파일을 동시에 지정할 목적으로 사용하는 특수 기호
    *, ? 등

주로 특정한 패턴이 있는 문자열 혹은 파일을 찾거나, 긴 이름을 생략할 때 쓰임

텍스트 값에서 알 수 없는 문자를 사용할 수 있는 특수 문자로, 유사하지만 동일한 데이터가 아닌 여러 항목을 찾기에 매우 편리한 문자

지정된 패턴 일치를 기반으로 데이터를 수집하는 데도 도움이 될 수 있음
```
```
# 이름에 '호'가 포함되는 사람들의 이름과 성 조회하기
SELECT first_name, last_name FROM users WHERE first_name LIKE '%호%';

# 이름이 '준'으로 끝나는 사람들의 이름 조회하기
SELECT first_name FROM users WHERE first_name LIKE '%준';

# 서울 지역 전화번호를 가진 사람들의 이름과 전화번호 조회하기
SELECT first_name, phone FROM users WHERE phone LIKE '02-%';

# 나이가 20대인 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users WHERE age LIKE '2_%';

# 전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화번호 조회하기
SELECT first_name, phone FROM users WHERE phone LIKE '%-51__-%';
```

**IN operator**
```
값이 값 목록 결과에 있는 값과 일치하는 지 확인

표현식이 값 목록의 값과 일치하는지 여부에 따라 true 또는 false를 반환

IN 연산자의 결과를 부정하려면 NOT IN 연산자를 사용
```
```
# 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회하기
SELECT first_name, country FROM users WHERE country IN ('경기도', '강원도');

SELECT first_name, country FROM users WHERE country = '경기도' OR country = '강원도';
    - IN 연산자 대신 OR 연산자를 사용하여 동일한 결과를 반환할 수 있음

# 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회하기
SELECT first_name, country FROM users WHERE country NOT IN ('경기도', '강원도');
```

**BETWEEN operator**
```
값이 값 범위에 있는지 테스트

값이 지정된 범위에 있으면 true를 반환

SELECT, DELETE 및 UPDATE 문의 WHERE 절에서 사용할 수 있음

BETWEEN 연산자의 결과를 부정하려면 NOT BETWEEN 연산자를 사용
```
```
# 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users WHERE age BETWEEN 20 AND 30;

SELECT first_name, age FROM users WHERE age >= 20 AND age <= 30;
    - AND 연산자를 사용하여 이전 쿼리와 동일한 결과를 반환할 수 있음

# 나이가 20살 이상, 30살 이하가 아닌 사람들의 이름과 나이 조회하기
SELECT frist_name, age FROM users WHERE age NOT BETWEEN 20 AND 30;

SELECT first_name, age FROM users WHERE age < 20 OR age > 30;
    - OR 연산자를 사용하여 이전 쿼리와 동일한 결과를 반환할 수 있음
```

**LIMIT clause**
```
쿼리에서 반환되는 행 수를 제한

SELECT 문에서 선택적으로 사용할 수 있는 절

row_count는 반환되는 행 수를 지정하는 양의 정수를 의미
```
```
# 첫 번째부터 열 번째 데이터까지 rowid와 이름 조회하기
SELECT rowid, first_name FROM users LIMIT 10;

# 계좌 잔고가 가장 많은 10명의 이름과 계좌 잔고 조회하기
SELECT first_name, balance FROM users ORDER BY balance DESC LIMIT 10;
    - ORDER BY 절과 함께 사용하여 지정된 순서로 여러 행을 가져 올 수도 있음
    - LIMIT 절에 지정된 행 수를 가져오기 전에 결과를 정렬하기 때문

# 나이가 가장 어린 5명의 이름과 나이 조회하기
SELECT first_name, age FROM users ORDER BY age LIMIT 5;
```

**OFFSET keyword**
```
LIMIT 절을 사용하면 첫 번째 데이터로부터 지정한 수 만큼의 데이터를 받아올 수 있지만, OFFSET과 함께 사용하면 특정 지정된 위치에서부터 데이터를 조회할 수 있음

# 11번째부터 20번째 데이터의 rowid와 이름 조회하기
SELECT rowid, first_name FROM users LIMIT 10 OFFSET 10;
```

### Grouping data
- 특정 그룹으로 묶인 결과를 생성

- 선택된 컬럼 값을 기준으로 데이터(행)들의 공통 값을 묶어서 결과로 나타냄

- SELECT 문에서 선택적으로 사용가능한 절

- SELECT 문의 FROM 절 뒤에 작성
    - WHERE 절이 포함된 경우 WHERE 절 뒤에 작성해야 함

- 각 그룹에 대해 MIN, MAX, SUM, COUNT 또는 AVG와 같은 집계 함수(aggregate function)를 적용하여 각 그룹에 대한 추가적인 정보를 제공할 수 있음
```
# 예시
SELECT column_1, aggregate_function(column_2) FROM table_name GROUP BY column_1, column_2
```

**Aggregate function**
```
집계 함수

값 집합의 최대값, 최소값, 평균, 합계 및 개수를 계산

값 집합에 대한 계산을 수행하고 단일 값을 반환
    - 여러 행으로부터 하나의 결과값을 반환하는 함수

SELECT 문의 GROUP BY 절과 함께 종종 사용됨

제공하는 함수 목록
    - AVE(), COUNT(), MAX(), MIN(), SUM()

AVG(), MAX(), MIN(), SUM()는 숫자를 기준으로 계산이 되어져야 하기 때문에 반드시 컬럼의 데이터 타입이 숫자(INTEGER)일 때만 사용 가능
```
```
# users 테이블의 전체 행 수 조회하기
SELECT COUNT(*) FROM users;

# 나이가 30살 이상인 사람들의 평균 나이 조회하기
SELECT AVG(age) FROM users WHERE age >= 30;
```
```
GROUP BY 사용해보기

# 각 지역별로 몇 명씩 살고 있는지 조회하기
SELECT country FROM users GROUP BY country;
    - '각 지역별'은 지역 별로 그룹을 나눌 필요가 있음을 의미함
    - country 컬럼으로 그룹화

# 몇 명씩 사는지 계산하기 위해서 그룹별로 포함되는 데이터의 수를 구함
SELECT country, COUNT(*) FROM users GROUP BY country;
    - Aggregation Function의 COUNT를 사용
    - 각 지역별로 그룹이 나뉘어졌기 때문에  COUNT(*)는 지역별 데이터 개수를 세게 됨


COUNT 참고 사항
    - 이전 쿼리에서 COUNT(), COUNT(age), COUNT(last_name) 등 어떤 컬럼을 넣어도 결과는 같음
    - 현재 쿼리에서 그룹화된 country를 기준으로 카운트 하는 것이기 때문에 어떤 컬럼을 카운트해도 전체 개수는 동일하기 때문
```
```
# 각 성씨가 몇명씩 있는지 조회하기
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;

SELECT last_name, COUNT(*) AS number_of_name FROM users GROUP BY last_name;
    - AS 키워드를 사용해 컬럼명을 임시로 변경하여 조회할 수 있음

# 인원이 가장 많은 성씨 순으로 조회하기
SELECT last_name, COUNT(*) FROM users GROUP BY last_name ORDER BY COUNT(*) DESC;

# 각 지역별 평균 나이 조회하기
SELECT country, AVG(age) FROM users GROUP BY country;
```

### Changing data
- 데이터를 삽입, 수정, 삭제하기
    - INSERT
    - UPDATE
    - DELETE
```
# 사전 준비
CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);
```

**INSERT statement**
```
새 행을 테이블에 삽입

문법 규칙
    1. 먼저 INSERT INTO 키워드 뒤에 데이터를 삽입할 테이블의 이름을 지정
    2. 테이블 이름 뒤에 쉼표로 구분된 컬럼 목록을 추가
        - 컬럼 목록은 선택 사항이지만 컬럼 목록을 포함하는 것이 권장됨
    3. VALUES 키워드 뒤에 쉼표로 구분된 값 목록을 추가
        - "만약 컬럼 목록을 생략할 경우 값 목록의 모든 컬럼에 대한 값을 지정해야 함"
        - 값 목록의 값 개수는 컬럼 목록의 컬럼 개수와 같야야 함
```
```
# 단일 행 삽입하기
'INSERT INTO' classmates (name, age, address) 'VALUES' ('홍길동', 23, '서울');

'INSERT INTO' classmates 'VALUES' ('홍길동', 23, '서울');
    - 다음과 같이 작성할 수도 있음

# 여러 행 삽입하기
'INSERT INTO' classmates 'VALUES' ('김철수', 30, '경기', '이영미', 33, '강원', '박진성', 26, '전라', '최지수', 12, '충청', '정요한', 28, '경상');
```

**UPDATE statement**
```
테이블에 있는 기존 행의 데이터를 업데이트 한다.

문법 규칙
    1. UPDATE 절 이후에 업데이트할 테이블을 지정
    2. SET 절에서 테이블의 각 컬럼에 대해 새 값을 설정
    3. WHERE 절의 조건을 사용하여 업데이트할 행을 지정
        - WHERE 절은 선택 사항이며, 생략하면 UPDATE 문은 테이블의 모든 행에 있는 데이터를 업데이트 함
    4. 선택적으로 ORDER BY 및 LIMIT 절을 사용하여 업데이트할 행 수를 지정할 수도 있음
```
```
# 2번 데이터의 이름을 '김철수한무두루미', 주소를 '제주도'로 수정하기
'UPDATE classmates 'SET' name='김철수한무두루미', address='제주도' WHERE rowid = 2;
```

**DELETE statement**
```
테이블에서 행을 제거

테이블의 한 행, 여러 행 및 모든 행을 삭제할 수 있음

문법 규칙
    1. DELETE FROM 키워드 뒤에 행을 제거하려는 테이블의 이름을 지정
    2. WHERE 절에 검색 조건을 추가하여 제거할 행을 식별
        - WHERE 절은 선택 사항이며, 생략하면 DELETE 문은 테이블의 모든 행을 삭제
    3. 선택적으로 ORDER BY 및 LIMIT 절을 사용하여 삭제할 행 수를 지정할 수도 있음
```
```
# 5번 데이터 삭제하기
'DELETE FROM' classmates WHERE rowid = '5';

# 삭제된 것 확인하기
'SELECT' rowid, * 'FROM' classmates;

# 이름에 '영'이 포함되는 데이터 삭제하기
DELETE FROM classmates WHERE name LIKE '%영%';

# 테이블의 모든 데이터 삭제하기
DELETE FROM classmates;
```

# 마무리
- Database
    - RDB

- SQL

- DDL
    - CREATE TABLE
        - Data Type
        - Constraints
    - ALTER TABLE
    - DROP TABLE

- DML
    - SELECT
        - SELECT DISTINCT
    - ORDER BY
    - WHERE
        - LIKE, IN, BETWEEN
    - LIMIT, OFFSET
    - GROUP BY
        - Aggregate Function
    - INSERT / UPDATE / DELETE

### 데이터  구조화의 중요성
- 다루고자 하는 데이터를 구조화해서 저장하면 데이터의 가공 및 확장이 용이
- 모든 서비스는 데이터를 효율적으로 다루는 것이 필수적
    - 예를 들어 빅데이터, 인공지능과 같은 대규모 데이터로부터 의미있는 분석 결과를 뽑아낼 수 있음