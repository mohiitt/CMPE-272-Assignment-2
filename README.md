## Introduction

This project showcases the development of a serverless web application built with AWS Lambda and Amazon DynamoDB. The application provides a complete set of CRUD (Create, Read, Update, Delete) functionality through API Gateway, where incoming requests trigger Lambda functions that interact with DynamoDB tables.

Through this project, I developed practical expertise in:
1. Designing and deploying AWS Lambda functions
2. Setting up API Gateway with proxy integration patterns
3. Working with DynamoDB for data storage and retrieval operations
4. Implementing proper IAM roles and security permissions

## Screenshots 
### DynamoDB Table
<img width="1683" height="506" alt="Screenshot 2025-09-15 at 1 37 56 AM" src="https://github.com/user-attachments/assets/d4104cc0-10b7-424f-a185-6958f46d23ea" />

<img width="1683" height="692" alt="Screenshot 2025-09-15 at 2 25 31 AM" src="https://github.com/user-attachments/assets/ace5ad0d-802d-4a84-a950-618bdfbed3ce" />

---

### API requests - using Postman API
#### POST - Successfully added a new record to the DynamoDB table.
<img width="1525" height="767" alt="Screenshot 2025-09-15 at 3 02 26 AM" src="https://github.com/user-attachments/assets/1b2e6fb3-97d8-4f5f-bf31-a070d82845cd" />

---

#### GET - Retrieved the newly added record from DynamoDB.
<img width="1525" height="767" alt="Screenshot 2025-09-15 at 3 02 45 AM" src="https://github.com/user-attachments/assets/a678426a-5590-47d8-9f01-2e13210dd033" />

---

#### PUT - Updated an existing record in the DynamoDB table.
<img width="1525" height="767" alt="Screenshot 2025-09-15 at 3 03 41 AM" src="https://github.com/user-attachments/assets/426a8be9-174a-497e-8d28-499728d58420" />

---

#### GET( After 'PUT') - Verified the updated record was stored correctly.
<img width="1525" height="767" alt="Screenshot 2025-09-15 at 3 03 56 AM" src="https://github.com/user-attachments/assets/32063989-320f-4864-9500-16d6d718c3ce" />

---

#### DELETE - Removed the record from the DynamoDB table.
<img width="1525" height="767" alt="Screenshot 2025-09-15 at 3 04 09 AM" src="https://github.com/user-attachments/assets/412c7465-32f0-47ae-8cbc-0bc1bfadc3fb" />

---

#### GET ( After 'DELETE') - Confirmed the record was deleted and no longer exists.
<img width="1525" height="767" alt="Screenshot 2025-09-15 at 3 04 27 AM" src="https://github.com/user-attachments/assets/e9b41136-b344-4a11-be6d-72b8b6e05bc2" />

---

## Reflection

During development, I encountered and resolved several technical challenges that deepened my understanding:

- In API Gateway (proxy integration), I learned that the request body is passed to Lambda as a JSON string inside `event['body']`. If no body is sent in Postman (or if "raw → JSON" is not selected), then `event['body']` becomes `None`, causing `json.loads(None)` errors.  
- I forgot to attach the correct IAM role, which caused authorization errors such as *“StudentRecordHandler is not authorized to perform: dynamodb:PutItem on resource.”*  
- I spent time troubleshooting a "missing" DynamoDB table, only to realize I was viewing resources in the wrong AWS region. Switching to us-east-1 immediately resolved the visibility issue.  
- I had to enable proxy integration specifically for GET methods to ensure requests were processed correctly by the Lambda function.
- The order of key-value pairs in the GET response was inconsistent, so I modified the code to retrieve and return them in a specific order.  

These challenges provided valuable insights into AWS service interactions, the significance of proper configuration and permissions, and effective debugging strategies for serverless applications.
