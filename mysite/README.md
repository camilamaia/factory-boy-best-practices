# mysite

This is a demo app built based on top of the [Django's Tutorial][django-tutorial].

## Install

### Requirements:

- [Python 3.9+][python]
- [Poetry][poetry]

### Fork camilamaia/factory-boy-best-practices repository

[Fork][fork] the repo in your github account such as you get
`_yourusername_/factory-boy-best-practices`.

### Clone

Now that you own a copy of the repo, you can easily clone the repo with the command below:

```shell
$ git clone https://github.com/<your username>/factory-boy-best-practices.git
```

### Enter in the mysite folder

```shell
$ cd factory-boy-best-practices/mysite
```

### Create and activate a new virtual environment

```shell
$ poetry shell
```

### Install the dependencies

```shell
$ poetry install
```

### Setup the Database

```shell
$ python manage.py migrate
```

## Run

```shell
$ python manage.py runserver
```

If everything runs smoothly, you should see the polls index page live at
`http://127.0.0.1:8000/polls`. Feel free to create an issue if run into problems while setting up
the project.

## Tests

```shell
$ pytest
```

[django-tutorial]: https://docs.djangoproject.com/en/3.2/intro/tutorial01/
[python]: https://www.python.org/downloads/
[fork]: https://docs.github.com/en/github/getting-started-with-github/quickstart/fork-a-repo
[poetry]: https://python-poetry.org/docs/#installation
