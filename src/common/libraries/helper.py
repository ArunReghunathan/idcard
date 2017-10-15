import os
import boto
from boto.s3.key import Key

from project.private_conf import S3_PERMISSION, AWS_STORAGE_BUCKET_NAME, AWS_S3_ACCESS_KEY_ID, AWS_S3_SECRET_ACCESS_KEY, \
    S3_URL


class paramObject():
    pass


def upload_to_s3(path, filename):

    conn = boto.connect_s3(AWS_S3_ACCESS_KEY_ID, AWS_S3_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(AWS_STORAGE_BUCKET_NAME)
    s3_url = os.path.join(S3_URL, path, filename)
    prefix = os.path.join(path)

    k = Key(bucket)
    k.key = os.path.join(prefix, filename)
    # k.set_contents_from_string(filename, policy=S3_PERMISSION)
    k.set_contents_from_filename(filename, policy=S3_PERMISSION)
    os.remove(path+filename)
    return s3_url


def upload_to_s3from_string(path, filename, string_data):

    conn = boto.connect_s3(AWS_S3_ACCESS_KEY_ID, AWS_S3_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(AWS_STORAGE_BUCKET_NAME)
    s3_url = os.path.join(S3_URL, path, filename)
    prefix = os.path.join(path)
    k = Key(bucket)
    k.key = os.path.join(prefix, filename)
    k.set_contents_from_string(string_data, policy=S3_PERMISSION)
    return s3_url