Installation for a unix alike system, run:

```bash
./install.sh
```

Installation for windows, run:

```bash
python -m venv venv
source venv/scripts/activate
pip install -r requirements.txt
```

In the Flask config, fill in the database settings (`src/config/settings.py`), or create and fill `.env` up by constants in a root repository, explained next below:

.env minimal requirements:

```ini
FLASK_APP='manage.py'
FLASK_DEBUG=1
FLASK_ENV='development'
POSTGRES_USER=postgres
POSTGRES_DB=your_db_name
POSTGRES_PASSWORD=your_postgress_password
POSTGRES_HOST=localhost_or_your_host_ip
POSTGRES_PORT=5432
PRODUCTION_SECRET_KEY=your_production_secret_key
DEVELOPMENT_SECRET_KEY=your_development_secret_key
MAIL_SERVER=smtp.your_mail_server
MAIL_PORT=587_or_465
MAIL_USE_TLS=1
MAIL_USE_SSL=0
MAIL_USERNAME=mail_name
MAIL_PASSWORD=mail_password
MAIL_SUPPRESS_SEND=0
```

Go to `src` repository and run `flask db upgrade`, do not forget beforehand create a database.

View the status of the gunicorn daemon:

```bash
sudo systemctl status gunicorn
```

Gunicorn's logs are in `gunicorn/access.log` и `gunicorn/error.log`.

After changing the systemd config, you need to re-read it and then restart the unit:

```bash
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
```
