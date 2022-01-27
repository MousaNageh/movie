## installation
### 1) get a clone from repo or just download it 
### 2) create virtual environment :
  - run the follow commands to create virtual environment : <br/>
    - for windows 
      ```python 
        $ python -m venv env
      ```
    - for linux <br/>
      ```python 
        $ sudo python3 -m venv env
      ```
### 2) activate virtual environment :
  - open cmd and in the repo root (where ```manage.py``` file is exists) : <br/>
  - then run the following command :
    - for windows 
    ```python 
        $ .\env\Scripts\activate
    ```
    - for linux 
    ```python 
        $ sudo .\env\bin\activate
    ```
### 3) install packages and dependencies :
  - after activate virtual environment (env) , run the following command :
    - for windows 
    ```python 
        $ pip install -r requirements.txt
    ```
    - for linux 
    ```python 
        $ pip install -r requirements.txt
    ```

### 4) make migrations :
  - after installing packages and dependencies , run the following command :
    - for windows 
    ```python 
        $ python manage.py makemigrations
    ```
    ```python 
        $ python manage.py migrate
    ```
    - for linux 
    ```python 
        $ python3 manage.py makemigrations
    ```
    ```python 
        $ python3 manage.py migrate
    ```

### 5) run django server :
  - after making migrations , run the following command :
    - for windows 
    ```python 
        $ python manage.py runserver
    ```
    - for linux 
    ```python 
        $ python3 manage.py runserver
    ```
## How to use app 
### 1) open your browser to url ``` http://127.0.0.1:8000/ ```
  - you will get a filter page whish is : 
    - we will see this page <br />
    ![alt text](https://raw.githubusercontent.com/MousaNageh/movie/master/static/images/1.PNG?row=True)
  - you can filter movies by `` title `` or by `` release date `` or by `` overview  ``   or by any both of then or by all of them 
  - after that clinic on search button

  - you will get the results like this : 
    ![alt text](https://raw.githubusercontent.com/MousaNageh/movie/master/static/images/2.PNG?row=True)

### 2) if you want to get the api data outside of this app 
  - you can send get request from any platform you want just use this url 
    - to filter by title<br />
     ``` http://127.0.0.1:8000/api/search?title=ourData```<br />
    - to filter by release date<br />
     ``` http://127.0.0.1:8000/api/search?date=ourData```<br />
    - to filter by release overview<br />
     ``` http://127.0.0.1:8000/api/search?overview=ourData```<br />
    - you can combine any two of them or all of them like this <br />
    ``` http://127.0.0.1:8000/api/search?overview=ourData&overview=ourData&title=ourData```

### 3) you can find the most popular movies 
  - click on popular movies link 
    ![alt text](https://raw.githubusercontent.com/MousaNageh/movie/master/static/images/3.PNG?row=True)

### 4) you can run test cases by the following commands :
  - for windows 
    ```python 
        $ python manage.py test
    ```
  - for linux 
    ```python 
        $ python3 manage.py test
    ```