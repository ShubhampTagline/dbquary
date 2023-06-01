## Dependencies
python 3
## Installation

1. Clone the repository:

```
git clone https://github.com/ShubhampTagline/dbquary.git
```

2. Create env

```
> Mac Os
python3 -m vnev env

> Window
py -m venv env
```

3. Active env

```
> Mac Os
source env/bin/activate

> Window
env/Scripts/activate
```

4. Install the required packages:

```
pip install -r requirements.txt
```

5. Apply migrations:

```
python manage.py migrate
```

6. Create a superuser:

```
python manage.py createsuperuser
```

7. Run the development server:

```
python manage.py runserver
```

8. Open the project in your web browser:

```
http://localhost:8000/
```



