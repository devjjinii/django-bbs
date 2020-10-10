## Django Study

##### `PyCharm` 으로 진행 

* 프로젝트 생성
    * 프로젝트 진행할 폴더 생성 후,<br>
    <img width="522" alt="스크린샷 2020-10-10 오후 9 47 20" src="https://user-images.githubusercontent.com/53853730/95655468-6c70a200-0b42-11eb-9612-b050c3b09833.png"> <br>
        * (= django-admin startproject djangoProject)
    * 프로젝트는 다수의 app을 가질 수 있음. // 앱 생성
        * ./manage.py startapp bbs (터미널열고)
    * DB 생성
        * ./manage.py migrate 
    * super user 생성
        * ./manage.py createsuperuser
            * Username, Email address, Password 입력 (관리자 페이지에서 사용할)
    * 서버 실행
        * ./manage.py runserver
    * admin page
        * localhost:8000/admin/
    * settings.py > INSTALLED_APPS > bbs(생성한 app) 추가 
    * setting.py > SECRET_KEY 는 분리해서 push 해야함.
        * 참고사이트 : https://inma.tistory.com/83
---
* bbs > models.py 
    * ./manage.py makemigrations bbs
    * ./manage.py migrate >> db.sqlite3 에 db 생성
--- 
##### `설정`
* settings.py : 프로젝트 환경 설정 파일
    * DEBUG : 디버그 모드 설정 // true, 배포시 : false
    * INSTALLED_APPS : pip로 설치한 앱 또는 본인이 만든 app을 추가
    * MIDDELWARE : request와 response사이의 주요 기능 레이어
    * TEMPLATES : django template관련 설정, 실제 뷰
    * DATABASES : 데이터베이스 연결
    * STATIC_URL : 정적파일(css,js,image...)

* manage.py : 프로젝트 관리 명령어 모음
    * startapp : 앱 생성
    * runserver : 서버 실행
    * createsuperuser : 관리자 생성
    * makemigrations app : app의 모델 변경 사항 체크
    * migrate : 변경사항을 db에 반영
    * shell : 쉘을 통해 데이터 확인
    * collectstatic : static 파일을 한곳에 모음
    * .....

