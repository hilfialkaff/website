"""
This file automatically deploys a Hyde application to the AWS cluster.

Ensure that you have the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
environmental variable setup.
"""

from boto import connect_s3
from boto.s3.key import Key
import os

BUCKET_NAME = "hilfialkaff.com"
SRC_DIR = "./deploy/"

def main():
    conn = connect_s3()
    bucket = conn.get_bucket(BUCKET_NAME)
    k = Key(bucket)

    for path, directory, files in os.walk(SRC_DIR):
        for f in files:
            k.key = os.path.relpath(os.path.join(path, f), SRC_DIR)
            k.set_contents_from_filename(os.path.join(path, f))
            bucket.set_acl('public-read', k.key)

if __name__ == '__main__':
    main()
