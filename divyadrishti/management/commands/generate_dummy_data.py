from django.core.management import BaseCommand
from django.contrib.auth.models import User
from divyadrishti.models import SymptomsAndPatientName
import random


class Command(BaseCommand):
    help = 'Generate dummy patient data for testing'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of dummy patients to create (default: 10)',
        )

    def handle(self, *args, **options):
        count = options['count']
        
        self.stdout.write(self.style.WARNING(f'Generating {count} dummy patient records...'))
        
        # Common symptoms to randomly assign
        symptoms_list = [
            'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever',
            'yellow_urine', 'yellowing_of_eyes', 'headache', 'cough', 'runny_nose',
            'chest_pain', 'weakness', 'dizziness', 'nausea', 'vomiting',
            'neck_pain', 'muscle_pain', 'joint_pain', 'fatigue', 'fever'
        ]
        
        # Patient name prefixes
        first_names = ['John', 'Jane', 'Michael', 'Sarah', 'David', 'Emily', 'Robert', 'Lisa',
                       'William', 'Mary', 'James', 'Patricia', 'Richard', 'Jennifer', 'Thomas']
        last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller',
                      'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez']
        
        created_count = 0
        for i in range(count):
            # Generate random patient name
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            patient_name = f"{first_name} {last_name}"
            
            # Select 5 random symptoms
            selected_symptoms = random.sample(symptoms_list, 5)
            
            try:
                # Create patient record
                patient = SymptomsAndPatientName.objects.create(
                    patient_name=patient_name,
                    symptom_one=selected_symptoms[0],
                    symptom_two=selected_symptoms[1],
                    symptom_three=selected_symptoms[2],
                    symptom_four=selected_symptoms[3],
                    symptom_five=selected_symptoms[4],
                )
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Created patient: {patient_name}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Failed to create patient {patient_name}: {str(e)}'))
        
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('\n✓ Created superuser: admin / admin123'))
        else:
            self.stdout.write(self.style.WARNING('\n⚠ Superuser "admin" already exists'))
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Successfully generated {created_count} patient records!'))
        self.stdout.write(self.style.SUCCESS('You can now run the application with: python manage.py runserver'))
