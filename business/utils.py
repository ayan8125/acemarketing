from .models import Goals


def generate_unique_id():
    most_Recent_goal = Goals.objects.all().order_by('-created_at')
    if len(most_Recent_goal) > 0:
        return most_Recent_goal[0]._id + 1
    return 1
