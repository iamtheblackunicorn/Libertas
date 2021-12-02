clean: ; rm -rf *.sqlite3
db_sync: ; python3 manage.py migrate --run-syncdb
serve: ; python3 manage.py runserver
