from exam_doncho.profiles.models import Profile


def get_profile():
    return Profile.objects.first()