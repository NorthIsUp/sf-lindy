
User:
    - name
    - email
    - phone
    - zipcode
    - address
    - gender

Student:
    - User

Teacher:
    - User

Staff:
    - User
    - role
        - mc
        - setup
        - dj

Volunteer:
    - User
    - role
        - setup
        - teardown

Band:
    - name
    - email
    - phone

Class:
    + Teachers
    + Student


    Enum ClassType:

Skill:
    - name
    - is_leader
    - is_follower
    - level
        - 1
        - 2
        - 3

Event:
    + Staff
    + Volunteer
    + Classes
    + Band
