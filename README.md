# Team Member API

HTTP API to support a team-member management
application. The team member data is persisted in a MySQL database. The application supports listing team members, adding a new team member, editing a team member,
and deleting a team member.


## Installation

Dependencies:

* djangorestframework
* Django
* mysql-server and mysql-client [See here](https://docs.djangoproject.com/en/2.1/ref/databases/#mysql-db-api-drivers)




## Usage

* Install the dependencies.
* Run ```python manage.py runserver```


### API Endpoints
> ```/api/``` - TeamMember list

> ```/api/<id>/``` - TeamMember Detail- id: Unique team member id

## Test
Example: To add a new user:

``` 
curl -X POST -H "Content-Type:application/json"
http://127.0.0.1:9000/api/ -d '{"first_name": "David",
"last_name": "Jones", "phone_number": "+15101234567", "email":
"test@test.com", "role": 0}'
```
