# LeapProject

Problem Statement
To create an API Service to fetch the statistics of the contributors of user specified GitHub repositories in the Amazon Web Services Environment.

Working plan
1.Taking the inputs – date range and repository 
2.Getting data from github api calling page wise
3.Storing data into the Pandas dataframe
4.Load and processing the Excel data to display output dictionary
5.Creating data for posting
6.Posting data to database using Api


























Section B) AWS
Services used: AWS Lambda, API Gateway, RDS (Relational Database Service), Cloudwatch, S3 (Simple 
Storage Service)
Steps
• Created AWS RDS instance using MySQL engine. Made the instance ready.
• Uploaded the lambda code in S3.
• Create the lambda function. 
• Connect Mysql Workbench to RDS instance.
• Create/Use database, table.
• Make a REST API in AWS API gateway to trigger the lambda.
• Call the API with query parameters.
NOTE:
The main.py is the code which can be run in the pycharm.
The lambda_function_code.py is the main file for the lambda function without dependencies.
The Package folder is for uploading to lambda, which is to be zipped & compressed and uploaded to S3.
