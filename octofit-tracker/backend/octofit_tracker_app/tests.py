from django.test import TestCase
from octofit_tracker_app.models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(
            email='test@example.com',
            username='testuser',
            first_name='Test',
            last_name='User',
            password='password123'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        owner = User.objects.create(
            email='owner@example.com',
            username='owneruser',
            first_name='Owner',
            last_name='User',
            password='password123'
        )
        team = Team.objects.create(
            name='Test Team',
            description='A test team',
            owner=owner
        )
        team.members.add(owner)
        self.assertEqual(team.name, 'Test Team')
        self.assertEqual(team.owner, owner)

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(
            email='activity@example.com',
            username='activityuser',
            first_name='Activity',
            last_name='User',
            password='password123'
        )
        activity = Activity.objects.create(
            user=user,
            activity_type='running',
            duration=30,
            distance=5.0,
            calories_burned=300,
            description='Morning run',
            date='2026-02-26T08:00:00Z'
        )
        self.assertEqual(activity.activity_type, 'running')
        self.assertEqual(activity.user, user)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(
            email='leaderboard@example.com',
            username='leaderboarduser',
            first_name='Leaderboard',
            last_name='User',
            password='password123'
        )
        team = Team.objects.create(
            name='Leaderboard Team',
            description='A leaderboard team',
            owner=user
        )
        leaderboard = Leaderboard.objects.create(
            user=user,
            team=team,
            total_points=100,
            total_activities=5,
            rank=1
        )
        self.assertEqual(leaderboard.user, user)
        self.assertEqual(leaderboard.team, team)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(
            name='Test Workout',
            description='A test workout',
            difficulty_level='beginner',
            duration=45,
            exercises=['Push-ups', 'Squats']
        )
        self.assertEqual(workout.name, 'Test Workout')
        self.assertEqual(workout.difficulty_level, 'beginner')
