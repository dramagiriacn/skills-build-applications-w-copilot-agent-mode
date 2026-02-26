from rest_framework import serializers
from octofit_tracker_app.models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)
    
    class Meta:
        model = Team
        fields = ('id', 'name', 'description', 'owner', 'members', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Activity
        fields = ('id', 'user', 'activity_type', 'duration', 'distance', 'calories_burned', 'description', 'date', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    team = TeamSerializer(read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ('id', 'user', 'team', 'total_points', 'total_activities', 'rank', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('id', 'name', 'description', 'difficulty_level', 'duration', 'exercises', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
