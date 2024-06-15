
## About

#### Classroom Clone 

This project is an ambitious undertaking to create a Classroom application similar to google classroom, with a strong focus on most of the functionalities.
# Getting Started
## Clone the Repository:

```bash
$ git clone https://github.com/aceiny/aceiny
```

## Install Dependencies:

```bash
Client : $ npm install
Server : $ npm install
```
## Api docs

```bash
##
```

## Database schema

```bash
https://dbdiagram.io/d/classroom-666d0b00a179551be6f10daa
```

## Run the App

### Development
```bash
Server : $ npm run start
Client : $ npm run dev
```

### Watch Mode
```bash
Server : $ npm run start:dev
Client : $ npm run dev
```
### Production Mode

```bash
Server : $ npm run start:prod
Client : $ npm run build
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
- Multer
- JWT
- NextJs
## Contributors
- ahmed yassine zeraibi
- yzeraibi2000@gmail.com
