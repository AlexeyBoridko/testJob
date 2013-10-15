test:
	python testTickets/manage.py test testTicketsApp

run:
	python testTickets/manage.py runserver 0.0.0.0:8000

syncdb:	
	python testTickets/manage.py syncdb --noinput
	python testTickets/manage.py migrate testTicketsApp
