# § The username can consist only of letters, numbers, and underscore ("_").
# Otherwise, raise a ValidationError with the message: "Ensure this value contains only letters, numbers, and underscore."

def username_validator(value):
    if not value.isalnum() and "_" not in value:
        raise ValueError("Ensure this value contains only letters, numbers, and underscore.")