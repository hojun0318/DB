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
