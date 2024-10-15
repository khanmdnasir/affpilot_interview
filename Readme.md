To run this project, 
At first create a virtual environment on project directory and
 run command `pip install -r requirements.txt`
after that run `python manage.py migrate`
 then, `python manage.py runserver`

For running background task,
 run `celery -A affpilot worker -l info `