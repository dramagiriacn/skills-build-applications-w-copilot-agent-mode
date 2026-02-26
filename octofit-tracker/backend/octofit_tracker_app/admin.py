from django.contrib import admin
from octofit_tracker_app.models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'created_at')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'date', 'duration', 'created_at')
    search_fields = ('user__username', 'activity_type')
    list_filter = ('activity_type', 'date', 'created_at')
    ordering = ('-date',)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'rank', 'total_points', 'total_activities')
    search_fields = ('user__username', 'team__name')
    list_filter = ('team', 'rank')
    ordering = ('team', 'rank')


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty_level', 'duration', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('difficulty_level', 'created_at')
    ordering = ('-created_at',)
