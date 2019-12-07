# WTTD Eventex Project

A study project for following along **WTTD** class.

[![Build Status](https://travis-ci.org/danielgoncalves/eventex.svg?branch=master)](https://travis-ci.org/danielgoncalves/eventex)
[![CodeFactor](https://www.codefactor.io/repository/github/danielgoncalves/eventex/badge)](https://www.codefactor.io/repository/github/danielgoncalves/eventex)

## How to start coding?

1. Clone repository
2. Create a virtual environment targeting Python 3.6+
3. Activate virtual environment
4. Install dependencies
5. Configure your development session with `.env` file
6. Run tests

```console
git clone git@github.com:danielgoncalves/eventex.git
cd eventex
python -m venv .eventex_venv
source .eventex_venv/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Deployment to Heroku

1. Create a Heroku instance
2. Send all config
3. Create a strong secure `SECRET_KEY` for the instance
4. Set `DEBUG` to false
5. Configure mail service
6. Push code

```console
heroku create youreventexinstance
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configure mail service (depends on the service you are planning to use)
git push heroku master --force
```
