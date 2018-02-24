# User Logs

# Project Setup

  - virtualenv env_userlogs
  - source env_userlogs/bin/activate
  - pip install -r requirements.txt
  - Create Superuser to access admin: ` ./manage createsuperuser `
  - Run Server: ` ./manage.py runserver`


Create Items and Variants in Admin using url: ` http://localhost:8000/admin/`
Edit the items and Variants to record view it's history

For looking history of a user: ` http://localhost:8000/apiv1/user/1/`
For looking complete Logs: ` http://localhost:8000/apiv1/logs/`