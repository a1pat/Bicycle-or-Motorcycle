# Bicycle-or-Motorcycle? #
An image-classification project for Udacity's AWS Machine Learning Nanodegree.

## Table of Contents ##
1. [Overview](#overview)
2. [File Descriptions](#file_descriptions)
3. [Instructions](#instructions)
4. [Results](#results)
5. [Dataset](#dataset)
6. [Packages](#packages)
7. [Author](#author)

## Overview<a name="overview"></a> ##
This is a project in Udacity’s AWS Machine Learning Engineer Nanodegree geared towards building an ML workflow.

*Scones Unlimited* is a scone-delivery-focussed company whose delivery drivers use different type of transport. Scones Unlimited optimizes its operations by assigning the appropriate tye of order to a driver/delivery vehicle. For example, bicyclists are assigned short-distance deliveries; motorcyclists are assigned longer-distance deliveries, etc.

The company seeks to automate its process by identifying whether a driver has arrived for order pick-up on bicycle or motorcycle using image classification. Accordingly, the goal of this project is to:
1. Build an image classification model that differentiates between bicycles and motorcycles;
2. Deploy the model for inference using AWS Lambda functions and AWS Step functions.

## File Descriptions<a name="file_descriptions"></a> ##
The following files are in the root folder:
+ **lambda.py**: code for the three AWS Lambda functions
+ **starter.ipynb**: Jupyter notebook
+ **step_function_definition.json**: state machine description
+ **step_function_fail.png**: screen clip of unsuccessful step function execution
+ **step_function_monitor.png**: image file of model inference versus threshold for some test images
+ **step_function_success.png**: screen clip of successful step function execution



## Instructions<a name="instructions"></a> ##
1.	Knowledge of and an account on AWS Sagemaker are prerequisites;
2.	Know how AWS billing works and keep a close eye on your incurred costs. Know your budget. The author is not responsible for costs that you incur;
3.	Upload the `starter.ipynb` file to AWS Sagemaker Studio and follow instructions contained in the file to execute the project;
4.	Delete models, endpoints, endpoint configurations, S3 buckets at the end to avoid continuing costs.



## Results<a name="results"></a> ##

1.	The image classification model had a test accuracy of 0.85.
2.	The Step Function indicates success when the prediction probability meets or exceeds the threshold (set at 0.93) with all three Lambda functions with green status, as shown below:
![success](https://github.com/a1pat/Bicycle-or-Motorcycle/blob/main/step_function_success.png)
3.	The Step Function fails when the prediction probability does not meet the threshold with the third Lambda function having a Red completion status as shown below:
![fail](https://github.com/a1pat/Bicycle-or-Motorcycle/blob/main/step_function_fail.png)





## Dataset<a name="dataset"></a> ##
The [cifar-100 dataset](https://www.cs.toronto.edu/~kriz/cifar.html) contains labeled images of 100 classes of objects. A subset containing images of bicycles and motorcycles was used to train train and test the image-classification model.
  
  
## Packages<a name="packages"></a> ##

1. [base64](https://docs.python.org/3/library/base64.html)
2. [boto3](https://pypi.org/project/boto3/)
3. [json](https://docs.python.org/3/library/json.html)
4. [jsonlines](https://pypi.org/project/jsonlines/)
5. [matplotlib](https://pypi.org/project/matplotlib/)
6. [numpy](https://numpy.org/)
7. [os](https://docs.python.org/3/library/os.html)
8. [pandas](https://pypi.org/project/pandas/)
9. [pickle](https://docs.python.org/3/library/pickle.html)
10. [random](https://docs.python.org/3/library/random.html)
11. [requests](https://pypi.org/project/requests/)
12. [sagemaker](https://pypi.org/project/sagemaker/)
13. [tarfile](https://docs.python.org/3/library/tarfile.html)




## Author<a name="author"></a> ##
Ashutosh A. Patwardhan [GitHub](https://github.com/a1pat), [LinkedIn](https://www.linkedin.com/in/ashutosh-patwardhan/).



