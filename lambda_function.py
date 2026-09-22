import json
import boto3
import urllib.parse

s3 = boto3.client("s3")


def lambda_handler(event, context):

    # Get bucket name
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]

    # Get uploaded object's key
    object_key = event["Records"][0]["s3"]["object"]["key"]

    # Decode the S3 object key
    object_key = urllib.parse.unquote_plus(object_key)

    # Get object metadata without downloading the file
    response = s3.head_object(
        Bucket=bucket_name,
        Key=object_key
    )

    # Extract useful metadata
    metadata = {
        "file_name": object_key.split("/")[-1],
        "bucket": bucket_name,
        "key": object_key,
        "size": response["ContentLength"],
        "content_type": response.get("ContentType"),
        "etag": response.get("ETag"),
        "last_modified": response["LastModified"].isoformat()
    }

    # Create a different S3 key for the metadata
    file_name = object_key.split("/")[-1]
    metadata_key = f"metadata/{file_name}.json"

    # Store metadata as JSON in S3
    s3.put_object(
        Bucket=bucket_name,
        Key=metadata_key,
        Body=json.dumps(metadata, indent=4),
        ContentType="application/json"
    )

    return {
        "statusCode": 200,
        "body": json.dumps(metadata)
    }