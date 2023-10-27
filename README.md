# Hot Diggety Dog Point-of-Sale System
[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Overview
The "Hot Diggety Dog" app is a Django-based point-of-sale system designed for local hot dog stand merchants. It provides functionality to manage hot dog stand inventory, process sales, apply discounts, track sales by time and location, and notify both customers and mobile inventory-management staff.


### Features
1. Inventory Management: Manage inventory items and associate them with individual hot dog stands. Set thresholds for inventory items to trigger notifications for restocking.
2. Sales Processing: Process sales by adding items, applying discounts, and capturing sales time and location.
Dynamic Discounting: Create and manage a range of discounts applicable to sales.
3. Location-Based Notifications: Notify customers via social media integrations when a hot dog stand is nearby based on geolocation. Notify supply staff when an inventory item's quantity falls below a defined threshold.
4. Django Admin Integration: Leverage the power of Django admin to manage stands, inventory, and sales seamlessly.


### Users
1. Stand Operators: There are approximately 50 hot dog stand operators. They can manage sales and check their inventory.
2. Supply Staff: Mobile inventory-management staff that drive to locations with supplies. They receive notifications for restocking.
3. Customers: Thousands of local area residents. They receive notifications when a hot dog stand is nearby.

## Technical Overview
The application has been designed with Domain-Driven Design principles. It uses Django's Class-Based Views for the front-end logic and integrates seamlessly with Django's admin for back-end management.

### Architecture Diagram

[![](https://mermaid.ink/img/pako:eNpdUF9PwjAQ_yrNPQ-y2a6MPZgwZsweiEaFBzcezrXAdGvJWiJI-O52G5rovdzd718ud4ZSCwkxbFvc78hLUijiapnlSyNbkikr2w2Wck1Go1syT1b5vEZjRgkaKciqkp9mPVgc12sWLq82AzbMPZwmeYoW35zvakiTnnh4WuTpO6qt7sZ_YTPRVOqH7perYPaY5XdHd5zCmjzrsnJtIUWFHTMcu8wG6b3Undq1WpdoK63-asCDRrYNVsK94dx5CrA72cgCYjcKbD8KKNTF6fBg9fNJlRBvsDbSg8NeoJVphe59zS-6R_WqtdttexhWiM9whPgmpOPplFEa0YAxFvDIgxPEgR-MGQsjh3Ma-nzKLx589Qn-eEJ5yPgkZBGd-JQHl28KfoGE?type=png)](https://mermaid.live/edit#pako:eNpdUF9PwjAQ_yrNPQ-y2a6MPZgwZsweiEaFBzcezrXAdGvJWiJI-O52G5rovdzd718ud4ZSCwkxbFvc78hLUijiapnlSyNbkikr2w2Wck1Go1syT1b5vEZjRgkaKciqkp9mPVgc12sWLq82AzbMPZwmeYoW35zvakiTnnh4WuTpO6qt7sZ_YTPRVOqH7perYPaY5XdHd5zCmjzrsnJtIUWFHTMcu8wG6b3Undq1WpdoK63-asCDRrYNVsK94dx5CrA72cgCYjcKbD8KKNTF6fBg9fNJlRBvsDbSg8NeoJVphe59zS-6R_WqtdttexhWiM9whPgmpOPplFEa0YAxFvDIgxPEgR-MGQsjh3Ma-nzKLx589Qn-eEJ5yPgkZBGd-JQHl28KfoGE)
### Database Design

[![](https://mermaid.ink/img/pako:eNqNVMuOmzAU_RXLq1ZNolAek6DRrLLorLqIuqkijTz2BayCzdhmWprm33sDKeAMGZWVfXzu8bkPfKRcC6Ap5SWzdidZblh1UAS_bxYMuf-zXJK9Y0p8rcEwp82bw6auyxYpWdYffdFup_MuhlwHk5Tobgl2lvyoXkEhr0ViwS6cEVwuH8bdo4MKaVwrx6Sa19uzEpBjgGsjLpQOOyudF7Miw8HcfQbK0f6gtZOW60Y5JDCsh4RZ75NaIVFpJzNkkg8yI89Q6p_EFQZsoUvxcS6dh77sV5EKmHluMaAP6RrZE489cv4-EaiYLKcApiFdI8DDtMon4MkX9VvpqdsaOFriBG2VwpIMCfrCtPNik1p4Uq9QSF7OO5jW4-gb55iOVlNMexN7pTQ2xtOR2OTp_qVhCsvUTrGhSe8Ld_PiiStWedWujeQ3Kn2eKy-20E7o_MmeU_fMyOq2xFsL8p-7p__J9LbBYd7fTxAMx-tYPorQBa3A4CwKfHS64AN1BWAcTXEpmPlxoAd1Qh5rnN63itM0Y6WFBW1qgb_e5ZEa0Jqp71rj3pmm39L0SH_R9HMcrrbbKAw3YRBFUZBsFrSlabAOVlEUbxBPwnidbJPTgv7uFNaruzCJo-QuTuJtHGyi8PQXIzeSFA?type=png)](https://mermaid.live/edit#pako:eNqNVMuOmzAU_RXLq1ZNolAek6DRrLLorLqIuqkijTz2BayCzdhmWprm33sDKeAMGZWVfXzu8bkPfKRcC6Ap5SWzdidZblh1UAS_bxYMuf-zXJK9Y0p8rcEwp82bw6auyxYpWdYffdFup_MuhlwHk5Tobgl2lvyoXkEhr0ViwS6cEVwuH8bdo4MKaVwrx6Sa19uzEpBjgGsjLpQOOyudF7Miw8HcfQbK0f6gtZOW60Y5JDCsh4RZ75NaIVFpJzNkkg8yI89Q6p_EFQZsoUvxcS6dh77sV5EKmHluMaAP6RrZE489cv4-EaiYLKcApiFdI8DDtMon4MkX9VvpqdsaOFriBG2VwpIMCfrCtPNik1p4Uq9QSF7OO5jW4-gb55iOVlNMexN7pTQ2xtOR2OTp_qVhCsvUTrGhSe8Ld_PiiStWedWujeQ3Kn2eKy-20E7o_MmeU_fMyOq2xFsL8p-7p__J9LbBYd7fTxAMx-tYPorQBa3A4CwKfHS64AN1BWAcTXEpmPlxoAd1Qh5rnN63itM0Y6WFBW1qgb_e5ZEa0Jqp71rj3pmm39L0SH_R9HMcrrbbKAw3YRBFUZBsFrSlabAOVlEUbxBPwnidbJPTgv7uFNaruzCJo-QuTuJtHGyi8PQXIzeSFA)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy pos

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Celery

This app comes with Celery.

To run a celery worker:

```bash
cd pos
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the same folder with _manage.py_, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the celery beat scheduler service. You can start it as a standalone process:

```bash
cd pos
celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

```bash
cd pos
celery -A config.celery_app worker -B -l info
```

### Email Server

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [Mailpit](https://github.com/axllent/mailpit) with a web interface is available as docker container.

Container mailpit will start automatically when you will run all docker containers.
Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With Mailpit running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

### Custom Bootstrap Compilation

The generated CSS is set up with automatic Bootstrap recompilation with variables of your choice.
Bootstrap v5 is installed using npm and customised by tweaking your variables in `static/sass/custom_bootstrap_vars`.

You can find a list of available variables [in the bootstrap source](https://github.com/twbs/bootstrap/blob/v5.1.3/scss/_variables.scss), or get explanations on them in the [Bootstrap docs](https://getbootstrap.com/docs/5.1/customize/sass/).

Bootstrap's javascript as well as its dependencies are concatenated into a single file: `static/js/vendors.js`.
