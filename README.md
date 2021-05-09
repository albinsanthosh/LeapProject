
## GitHub Contributor Aggregator
This project uses the commits info data from the github api and process to collect the contributors’ statistics and store in AWS RDS database.  

## Problem Statement
To create an API Service to fetch the statistics of the contributors of user specified GitHub repositories in the Amazon Web Services Environment.
We used Python as programming language in the Pycharm and for Lambda function. 

### Section A) Python
Libraries used: Pandas, Requests, Json, Mysql.connector, datetime 

#### Steps
* Taking the inputs – date range and repository 
* Getting data from github api calling page wise
* Storing data into the Pandas dataframe.
* Process the Pandas dataframe data.
* Create an output dictionary.
* Sending data to RDS database.
* Displaying the output dictionary. 
* Displaying a JSON Response.

### Section B) AWS
Services used: AWS Lambda, API Gateway, RDS (Relational Database Service), Cloudwatch, S3 (Simple Storage Service)

#### Steps
* Created AWS RDS instance using MySQL engine. Made the instance ready.
* Uploaded the lambda code in S3.
* Create the lambda function. 
* Connect Mysql Workbench to RDS instance.
* Create/Use database, table.
* Make a REST API in AWS API gateway to trigger the lambda.
* Call the API with query parameters.

## NOTE:
The main.py is the code which can be run in the pycharm.
The lambda_function_code.py is the main file for the lambda function without dependencies.
The Package folder is for uploading to lambda, which is to be zipped & compressed and uploaded to S3.
