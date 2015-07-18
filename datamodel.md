User:
    - name
    - email
    - phone
    - zipcode
    - address
    - gender

Student:
    - User
    + Skills

Teacher:
    - User
    + Classes

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
    - Enum ClassType

Skill:
    - name
    - is_leader
    - is_follower
    - level
        - 1
        - 2
        - 3

Session:
    + Staff
    + Volunteer
    + Classes
    + Band
    - date

Series
    + Session
    - start_date
    - end_date
