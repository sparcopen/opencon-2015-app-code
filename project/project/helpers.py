"""
Application helper methods.
"""
import hashlib


def get_fingerprint(timestamp, email):
    """
    Return unique fingerprint based on application timestamp and email.
    """
    fingerprint = hashlib.md5()
    fingerprint.update(timestamp)
    fingerprint.update(email)
    return fingerprint.hexdigest()
