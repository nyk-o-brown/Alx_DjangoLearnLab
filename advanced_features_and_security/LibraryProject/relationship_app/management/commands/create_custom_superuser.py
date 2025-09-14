from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a custom superuser with additional fields'

    def add_arguments(self, parser):
        parser.add_argument('--email', type=str, help='Email address')
        parser.add_argument('--username', type=str, help='Username')
        parser.add_argument('--password', type=str, help='Password')
        parser.add_argument('--first-name', type=str, help='First name')
        parser.add_argument('--last-name', type=str, help='Last name')
        parser.add_argument('--date-of-birth', type=str, help='Date of birth (YYYY-MM-DD)')

    def handle(self, *args, **options):
        email = options['email'] or input('Email: ')
        username = options['username'] or input('Username: ')
        password = options['password'] or input('Password: ')
        first_name = options['first_name'] or input('First name: ')
        last_name = options['last_name'] or input('Last name: ')
        date_of_birth = options['date_of_birth'] or input('Date of birth (YYYY-MM-DD) [optional]: ')

        if date_of_birth:
            try:
                date_of_birth = date.fromisoformat(date_of_birth)
            except ValueError:
                self.stdout.write(
                    self.style.ERROR('Invalid date format. Use YYYY-MM-DD')
                )
                return

        try:
            user = User.objects.create_superuser(
                email=email,
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created superuser: {user.email}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating superuser: {str(e)}')
            )
