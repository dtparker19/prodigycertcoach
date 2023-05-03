# django_multi_tenant
Simple django multi tenant application

Using django-tenant-schemas with django 2.2

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install requirements.txt
```

## Usage

* Use the django shell to run the following command

```bash
python manage.py shell
```

```python
from shared.models import Client

tenant = Client(domain_url='my-domain.com', # don't add your port or www here! on a local server you'll want to use localhost here
                schema_name='public',
                name='Schemas Inc.')
tenant.save()
```

That will create the first tenant (which usually is the base to create new ones)

* Create the super user for the created tenant by running the following command and follow the steps
```bash
python manage.py tenant_command createsuperuser --schema=public
```

**_Note:_** the same command can be used to create admin users on the different tenants that you create, just remember to change the --schema to the one that you define

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

