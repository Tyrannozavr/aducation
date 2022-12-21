# aducation
service for creating and passing tests.
To get started run: 
git clone https://github.com/Tyrannozavr/aducation
cd aducation
source venv/bin/activate
pip install -r requirements.txt
./manage.py makemigrations && ./manage.py migrate
./manage.py runserver
