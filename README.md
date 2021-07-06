Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```python
git clone https://github.com/Asp1nn/api_final_yatube.git
```
```python
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
```python
python3 -m venv env
```
```python
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```python
pip install -r requirements.txt
```
Выполнить миграции:
```python
python3 manage.py migrate
```
Запустить проект:
```python
python3 manage.py runserver
```
Посмотреть документацию по проекту:
```python
http://localhost:8000/redoc/
```
