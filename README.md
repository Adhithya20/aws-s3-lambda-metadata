# AWS S3 Lambda Metadata Extractor

A serverless AWS project that automatically extracts metadata from files uploaded to an Amazon S3 bucket using AWS Lambda.

## 📌 Project Overview

This project uses an **Amazon S3 ObjectCreated event** to trigger an AWS Lambda function whenever a file is uploaded to the `uploads/` folder.

The Lambda function retrieves the uploaded file's metadata using the S3 `HeadObject` API and stores the extracted information as a JSON file in the `metadata/` folder.

## 🏗️ Architecture

```text
User
  │
  │ Upload File
  ▼
Amazon S3
uploads/
  │
  │ ObjectCreated Event
  ▼
AWS Lambda
s3-metadata-extractor
  │
  │ head_object()
  ▼
Extract File Metadata
  │
  │ JSON
  ▼
Amazon S3
metadata/
  └── filename.json
```

## 🚀 Technologies Used

* AWS Lambda
* Amazon S3
* Python
* Boto3
* JSON
* AWS IAM

## ⚙️ How It Works

1. A file is uploaded to the `uploads/` folder in the S3 bucket.
2. Amazon S3 generates an ObjectCreated event.
3. The event triggers the Lambda function.
4. Lambda identifies the bucket and uploaded file.
5. The `head_object()` API retrieves the file metadata without downloading the complete file.
6. The Lambda function extracts information such as:

   * File name
   * Bucket name
   * Object key
   * File size
   * Content type
   * ETag
   * Last modified time
7. The metadata is converted into JSON format.
8. The JSON metadata is stored in the `metadata/` folder using a different S3 key.

## 📂 Project Structure

```text
aws-s3-lambda-metadata/
│
├── lambda_function.py
├── README.md
└── .gitignore
```

## 📝 Example

If the following file is uploaded:

```text
uploads/hello.txt
```

Lambda generates:

```text
metadata/hello.txt.json
```

Example metadata:

```json
{
    "file_name": "hello.txt",
    "bucket": "your-s3-bucket",
    "key": "uploads/hello.txt",
    "size": 22,
    "content_type": "text/plain",
    "etag": "example-etag",
    "last_modified": "2026-09-22T17:15:45+00:00"
}
```

## 📦 Handling Large Files

The Lambda function does not download the entire uploaded file.

It uses the S3 `head_object()` API to retrieve metadata such as file size, content type, ETag, and last modified time.

This makes the solution efficient even when the uploaded file is large.

For applications that require processing the actual contents of very large files, additional services or techniques such as S3 Range Requests, Amazon SQS, or asynchronous processing can be considered.

## 🔐 Security

The Lambda function requires permission to read the uploaded object's metadata and write the generated JSON metadata to S3.

For production environments, IAM permissions should follow the **principle of least privilege** rather than granting unnecessary permissions.

## 💰 Cost Considerations

This project uses serverless AWS services and is suitable for small-scale testing and learning.

Costs can depend on the number of S3 requests, Lambda invocations, storage, and other AWS usage.

## 🎯 Project Objective

The objective of this project is to demonstrate:

* S3 event-driven architecture
* AWS Lambda
* Serverless processing
* Python and Boto3
* S3 object metadata extraction
* JSON metadata storage
* Efficient handling of large files

## 👨‍💻 Author

**Adhithya P S**

B.E. Computer Science and Engineering

Cloud & DevOps | AWS | Docker | Terraform | Kubernetes
