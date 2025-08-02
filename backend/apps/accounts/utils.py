from django.contrib.auth.tokens import PasswordResetTokenGenerator

class UserPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    pass

user_password_reset_token = UserPasswordResetTokenGenerator()
