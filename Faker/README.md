## Populating Database Reference

* <a href="https://fakerjs.dev/api/" target="_blank">Faker API Reference</a>
<!-- * <a href="" target="_blank">Template</a> -->

## Steps

1. Create ``management\commands`` directory inside of app

2. Create ``populate_db.py`` file inside of ``management\commands`` directory
    ```python
    from django.core.management.base import BaseCommand
    from your_app.models import YourModel
    from faker import Faker

    class Command(BaseCommand):
        help = 'Populates the database with fake data'

        def handle(self, *args, **kwargs):
            fake = Faker()

            for _ in range(100):  # Adjust the range for the number of records you need
                YourModel.objects.create(
                    field1=fake.name(),
                    field2=fake.address(),
                    field3=fake.email(),
                    # Add other fields as needed
                )

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake data.'))

    ```
    
3. Run terminal command
    ```
    py manage.py populate_db
    ```


## Requirements

```
pip install faker
```