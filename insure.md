# On the Road Car Insurance - Claim Prediction Dataset

## **Overview**
Insurance companies invest significant time and resources into optimizing their pricing and accurately estimating the likelihood of customers making a claim. In many countries, car insurance is a legal requirement for driving on public roads, making the market extensive.

On the Road Car Insurance has requested assistance in building a model to predict whether a customer will file a claim during the policy period. Due to limited expertise and infrastructure for deploying and monitoring machine learning models, they have requested the identification of the single most important feature for an accurate model.

The provided dataset, **`car_insurance.csv`**, contains customer-related attributes that can be used for model training.

## **Dataset Description**
The dataset consists of the following columns:

| Column Name         | Description |
|---------------------|-------------|
| **id** | Unique client identifier |
| **age** | Client's age category: <br> 0: 16-25 <br> 1: 26-39 <br> 2: 40-64 <br> 3: 65+ |
| **gender** | Client's gender: <br> 0: Female <br> 1: Male |
| **driving_experience** | Years the client has been driving: <br> 0: 0-9 <br> 1: 10-19 <br> 2: 20-29 <br> 3: 30+ |
| **education** | Client's education level: <br> 0: No education <br> 1: High school <br> 2: University |
| **income** | Client's income level: <br> 0: Poverty <br> 1: Working class <br> 2: Middle class <br> 3: Upper class |
| **credit_score** | Client's credit score (between 0 and 1) |
| **vehicle_ownership** | Vehicle ownership status: <br> 0: Does not own (paying off finance) <br> 1: Owns vehicle |
| **vehicle_year** | Year of vehicle registration: <br> 0: Before 2015 <br> 1: 2015 or later |
| **married** | Marital status: <br> 0: Not married <br> 1: Married |
| **children** | Number of children the client has |
| **postal_code** | Client's postal code |
| **annual_mileage** | Number of miles driven annually by the client |
| **vehicle_type** | Type of car: <br> 0: Sedan <br> 1: Sports car |
| **speeding_violations** | Total number of speeding violations received |
| **duis** | Number of times caught driving under the influence of alcohol |
| **past_accidents** | Total number of previous accidents the client has been involved in |
| **outcome** | Response variable - Whether the client made a claim: <br> 0: No claim <br> 1: Made a claim |

## **Objective**
The goal is to determine the single feature that results in the best-performing model (measured by accuracy) for predicting whether a customer will make an insurance claim.

## **Usage**
This dataset can be used to:
- Perform exploratory data analysis (EDA) to understand feature distributions.
- Train a classification model to predict `outcome`.
- Identify the most significant feature for claim prediction.

