import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def upload_resume_to_s3(file_path, bucket_name, s3_file_name):
    """
    Uploads a resume file to AWS S3.

    AWS credentials are managed using IAM Role (EC2)
    or environment variables (local setup).
    """

    try:
        s3 = boto3.client("s3")
        s3.upload_file(file_path, bucket_name, s3_file_name)
        return True

    except FileNotFoundError:
        print("File not found")
        return False

    except NoCredentialsError:
        print("AWS credentials not available")
        return False

    except ClientError as e:
        print(f"AWS Client Error: {e}")
        return False
