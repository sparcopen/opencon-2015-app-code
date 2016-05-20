# OpenCon-Rating-App

## Migration notes

Deleted files:

* `README.md` (original version of README)
* `etc/nginx/opencon.orion` (not needed anymore: testing configuration for nginx)

Edited files:

* `project/rating/templates/rating/email/invite-round2.message` (redacted link to rating instructions)
* `project/project/settings.py` (redacted: SECRET_KEY, MAILGUN_ACCESS_KEY, edited: ADMINS)

Before deploying a functional instance (re-initializing the project), please remember to adjust project settings as needed.

## Miscellaneous

* This application had its [session at OpenCon 2015](https://opencon2015brussels.sched.org/event/e191f9a35fe044e42fa5cd2cfa7f1765) where future developments were discussed. For OpenCon 2016, it is now being re-designed and will be open sourced as well.
