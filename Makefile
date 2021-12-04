clean: ; rm -rf *.sqlite3 media/images/banner_pictures/*.png media/images/banner_pictures/*.jpg media/images/profile_pictures/*.png media/images/profile_pictures/*.jpg media/images/bit_pictures/*.png media/images/bit_pictures/*.jpg
db_sync: ; python3 manage.py migrate --run-syncdb
serve: ; python3 manage.py runserver
