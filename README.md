# School-management
### This software will be used by:
1. Parents 
    - *to book classes for their kids, check timetable, check class room numbers*
2. Teachers
    - *view their timetable, list of students in the class, class room number, mark an attendance, teacher assistant information*
3. School administrator
    - *view school timetable and manage it, get information about family or current student and manage it, view current teacher timetable and correct it*
4. System administrator
    - *Database administrator can manage the database - add new tables, add or delete fields, works with logins & passwords file.*

### Logins and passwords are kept in txt file

### Tables in Database:
1. Parent
   
   | Parent ID | Name | Surname | DOB | email | phone number | address |
   
   primary key: Parent ID

2. Student
   
   | Student ID | Parent ID | Name | Surname | DOB | class ID |
   
   primary key: student ID is Parent ID combined with serial number under which the student is registered when parent submitted an application for the family

3. Teacher
   
   | Teacher ID | Name | Surname | DOB | email | phone number | address |
   
   primary key: Teacher ID

4. Class
   
   | Class ID | Name | Time | Room number |
   
   primary key: Class ID
   
