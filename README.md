# Address Parser

An Address Parser which can be used to parse complex string patterns to find the `street` and `housenumber`

- [API Endpoints](#api-endpoints)
- [Install](#install)
- [Run tests](#run-tests)

## API Endpoints

#### POST `/address/`

User can pass the address here in string format to get the desired output as `street` and `housenumber`

**Request**

```
{
  "address": "Calle Aduana, 29"
}
```

**Example Response**

```
{
  "street": "Calle Aduana",
  "housenumber": "29"
}
```
---

## Install

- A `dockerfile` for backend server added.
- A `docker-compose.yml` file consists `api` service added.

To run the API, go to the root directory and execute the following command:

```

docker compose up

```
After that, check the Swagger API docs here, [localhost](http://localhost/docs)


---

## Run tests

To run tests, go to the root directory and execute the following command,

```

virtualenv venv; source venv/bin/activate; cd app; pip install -r requirements.txt; python -m pytest -v

```

