# django-week

docker-compose up -d

docker-compose exec web bash

python manage.py migrate

// Si pas accès a /admin
python manage.py createsuperuser
-> root
-> mdp que tu veux

python manage.py migrate
