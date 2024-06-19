
## About

#### Classroom Clone 

This project is an ambitious undertaking to create a Classroom application similar to google classroom, with a strong focus on most of the functionalities.
# Getting Started
## Clone the Repository:

```bash
$ https://github.com/aceiny/classroom
```

## Install Dependencies:

```bash
$ pip install -r requirements.txt
```
## Api docs

```bash
/docs
or
/redoc
```

## Database schema

```bash
https://dbdiagram.io/d/classroom-666d0b00a179551be6f10daa
```

## Run the App

### Development
```bash
fastapi dev main.py
```
### Production Mode

```bash
fastapi run 
```

## SECURITY MEASURES
- **Strong authentication:** using Passport.js and guards to control access based on authentication
- **Encryption:** Encrypting and hashing passwords 
- **Vulnerability Prevention::** Leverage security features built into NestJS like Helmet, which helps configure secure HTTP headers to mitigate common attacks.
- **Input Validation:** Validate all user-provided data to prevent unexpected inputs or malicious code injection
- **Rate Limiting:**  Implement rate limiting to prevent brute-force attacks or denial-of-service attempts.

## Technologies Used
- python
- fastapi
- postgres 
- prisma 
- JWT
## Contributors
- ahmed yassine zeraibi
- yzeraibi2000@gmail.com
