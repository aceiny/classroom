## Setup virtual environment

```sh
python -m venv .venv
source .venv/bin/activate
```

## Install requirements

```sh
pip install -r requirements.txt
```

## Setup environment
1. cp `.env.sample` `.env`
2. Include `DATABASE_URL and JWT_SECRET`
   ```
   JWT_SECRET=very_secret_key
   DATABASE_URL="postgresql://<user>:<password>@<url>:5432/postgres?schema=<scheme>"
   ```
   > Note that you should change appropriate values in `user`, `password`, `url`, `scheme` fields. Or you can even use other database. More about [connection urls](https://www.prisma.io/docs/reference/database-connectors/connection-urls)

## Generate Prisma Client and Nexus

```sh
python3 -m prisma generate
or 
npx prisma@5.11.0 generate
```

## Start server

```sh
uvicorn main:app --reload
```

## Notes

> After installing packages

```sh
pip freeze > requirements.txt
```
