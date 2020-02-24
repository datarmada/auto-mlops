import re

EMAIL_REGEX = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


def check_email(email: str):
    return email and (re.search(EMAIL_REGEX, email))
