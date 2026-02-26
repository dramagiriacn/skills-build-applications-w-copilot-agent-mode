from django.core.management.base import BaseCommand
from octofit_tracker_app.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        """Populate the database with superhero and team data"""
        
        # Clear existing data
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Database cleared successfully'))
        
        # Create Marvel Team users
        marvel_users = [
            {'email': 'tony@marvel.com', 'username': 'iron_man', 'first_name': 'Tony', 'last_name': 'Stark'},
            {'email': 'steve@marvel.com', 'username': 'captain_america', 'first_name': 'Steve', 'last_name': 'Rogers'},
            {'email': 'natasha@marvel.com', 'username': 'black_widow', 'first_name': 'Natasha', 'last_name': 'Romanoff'},
            {'email': 'bruce@marvel.com', 'username': 'hulk', 'first_name': 'Bruce', 'last_name': 'Banner'},
            {'email': 'thor@marvel.com', 'username': 'thor', 'first_name': 'Thor', 'last_name': 'Odinson'},
        ]
        
        # Create DC Team users
        dc_users = [
            {'email': 'clark@dc.com', 'username': 'superman', 'first_name': 'Clark', 'last_name': 'Kent'},
            {'email': 'diana@dc.com', 'username': 'wonder_woman', 'first_name': 'Diana', 'last_name': 'Prince'},
            {'email': 'bruce_wayne@dc.com', 'username': 'batman', 'first_name': 'Bruce', 'last_name': 'Wayne'},
            {'email': 'barry@dc.com', 'username': 'flash', 'first_name': 'Barry', 'last_name': 'Allen'},
            {'email': 'arthur@dc.com', 'username': 'aquaman', 'first_name': 'Arthur', 'last_name': 'Curry'},
        ]
        
        # Create users
        self.stdout.write(self.style.SUCCESS('Creating users...'))
        marvel_user_objects = []
        for user_data in marvel_users:
            user = User.objects.create(
                email=user_data['email'],
                username=user_data['username'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                password='hashed_password_123'  # In reality, this should be hashed
            )
            marvel_user_objects.append(user)
        
        dc_user_objects = []
        for user_data in dc_users:
            user = User.objects.create(
                email=user_data['email'],
                username=user_data['username'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                password='hashed_password_123'
            )
            dc_user_objects.append(user)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(marvel_user_objects) + len(dc_user_objects)} users'))
        
        # Create teams
        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel_team = Team.objects.create(
            name='Team Marvel',
            description='The Mighty Avengers from Marvel Universe',
            owner=marvel_user_objects[0]
        )
        marvel_team.members.set(marvel_user_objects)
        
        dc_team = Team.objects.create(
            name='Team DC',
            description='The Justice League from DC Universe',
            owner=dc_user_objects[0]
        )
        dc_team.members.set(dc_user_objects)
        
        self.stdout.write(self.style.SUCCESS('Created 2 teams'))
        
        # Create activities
        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        activity_types = ['running', 'cycling', 'swimming', 'gym', 'yoga']
        now = datetime.now()
        
        for i, user in enumerate(marvel_user_objects + dc_user_objects):
            for j in range(3):  # 3 activities per user
                activity = Activity.objects.create(
                    user=user,
                    activity_type=activity_types[j % len(activity_types)],
                    duration=45 + (j * 15),
                    distance=5.0 + (j * 1.5),
                    calories_burned=300 + (j * 100),
                    description=f"Awesome {activity_types[j % len(activity_types)]} session by {user.username}",
                    date=now - timedelta(days=j)
                )
        
        self.stdout.write(self.style.SUCCESS('Created activities for all users'))
        
        # Create leaderboard entries
        self.stdout.write(self.style.SUCCESS('Creating leaderboard entries...'))
        rank = 1
        for user in marvel_user_objects:
            leaderboard = Leaderboard.objects.create(
                user=user,
                team=marvel_team,
                total_points=1000 - (rank * 50),
                total_activities=3,
                rank=rank
            )
            rank += 1
        
        rank = 1
        for user in dc_user_objects:
            leaderboard = Leaderboard.objects.create(
                user=user,
                team=dc_team,
                total_points=950 - (rank * 50),
                total_activities=3,
                rank=rank
            )
            rank += 1
        
        self.stdout.write(self.style.SUCCESS('Created leaderboard entries'))
        
        # Create workouts
        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        workouts_data = [
            {
                'name': 'Full Body Workout',
                'description': 'A complete full body workout for all levels',
                'difficulty_level': 'beginner',
                'duration': 60,
                'exercises': ['Push-ups', 'Squats', 'Planks', 'Lunges']
            },
            {
                'name': 'Advanced HIIT Training',
                'description': 'High intensity interval training for advanced users',
                'difficulty_level': 'advanced',
                'duration': 45,
                'exercises': ['Burpees', 'Mountain Climbers', 'Jump Squats', 'High Knees']
            },
            {
                'name': 'Yoga for Beginners',
                'description': 'Relaxing yoga session perfect for beginners',
                'difficulty_level': 'beginner',
                'duration': 30,
                'exercises': ['Child\'s Pose', 'Downward Dog', 'Tree Pose', 'Savasana']
            },
            {
                'name': 'Core Strengthening',
                'description': 'Focus on core muscles and stability',
                'difficulty_level': 'intermediate',
                'duration': 40,
                'exercises': ['Planks', 'V-ups', 'Russian Twists', 'Bicycle Crunches']
            },
            {
                'name': 'Cardio Blast',
                'description': 'Intense cardio workout to boost your endurance',
                'difficulty_level': 'intermediate',
                'duration': 30,
                'exercises': ['Jumping Jacks', 'Rope Skipping', 'High Knees', 'Butt Kicks']
            },
        ]
        
        for workout_data in workouts_data:
            workout = Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS('Created 5 workouts'))
        
        self.stdout.write(self.style.SUCCESS('✅ Database population completed successfully!'))
        self.stdout.write(f'Total users created: {User.objects.count()}')
        self.stdout.write(f'Total teams created: {Team.objects.count()}')
        self.stdout.write(f'Total activities created: {Activity.objects.count()}')
        self.stdout.write(f'Total leaderboard entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'Total workouts created: {Workout.objects.count()}')
