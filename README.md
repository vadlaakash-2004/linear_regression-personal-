# Tittle
driveworth: Data-Driven Used Car Price Prediction Using Machine Learning
## Problem Statement

The objective of the project is to design a machine learning system that can effectively predict the selling price of used cars based on different factors such as age of the car, kilometers traveled, type of fuel, type of transmission, capacity of the car’s engine, mileage, brand, and model of the car.

The used car market is highly dynamic, and it is very challenging to estimate the price of the car as there are different factors that affect the price of the car.
## Dataset

The dataset contains information about used cars, including key features such as:

- Vehicle Age  
- Kilometers Driven  
- Mileage  
- Engine Capacity  
- Max Power  
- Number of Seats  
- Brand and Model  
- Fuel Type  
- Seller Type  
- Transmission Type  

The target variable is **selling_price**, which represents the market price of the car in INR.

After preprocessing, categorical variables were converted using one-hot encoding, resulting in multiple derived features.
## Project Workflow

1. Problem statement 
2. Libraries  
3. Load Dataset
4. Data understanding 
5. EDA & Preprocessing
6. Model Training  
7. Model Comparison  
8. Model Evaluation
9. Model saving (joblib) 
10. model script
##  Models Used

- Linear Regression  
- Ridge Regression  
- Lasso Regression  
- Elastic Net  
- Decision Tree Regressor  
- Random Forest Regressor  
- Gradient Boosting Regressor  
- XGBoost  
- LightGBM  
- CatBoost  
##  Best Model

The **CatBoost Regressor** performed the best among all models.

###  Performance Metrics:
- R² Score: 0.958  
- MAE: ~87,000  
- RMSE: ~177,000  

The model showed strong generalization with minimal overfitting.
##  Real-World Testing

The model was tested on real-world car listings.

Example:
- Hyundai Creta (1 year old)
- Real Price: ₹13–16 lakh  
- Predicted Price: ~₹12 lakh
### Insight:
The model tends to underestimate newer cars due to dataset bias and missing features like condition, variant, and market demand.

##  How to Run

1. Clone the repository:
```bash
git clone https://github.com/vadlaakash-2004/driveworth-ml-project.git
cd driveworth-ml-project
```
2. Install the required libraries:
```blash
pip install -r requirements.txt
```
3.Run the prediction script:
```blash
python srcript/predict_price.py
```
##  1️ Project Structure

```markdown
 Project Structure

car-price-prediction/
│
├── data/
├── notebook/
├── model/
├── src/
├── README.md
├── requirements.txt
└── .gitignore
```
## Conclusion

This project demonstrates an end-to-end machine learning pipeline for predicting used car prices. By comparing multiple models and selecting CatBoost as the best performer, the model achieves high accuracy and strong generalization.

The project also highlights real-world challenges such as dataset bias and missing features, which affect prediction accuracy for newer vehicles.
##  Future Improvements

- Deploy as a Streamlit web application  
- Improve feature engineering  
- Use log transformation of target  
- Collect more recent data  
- Handle unseen categories better
## Author

Akash Vadla  
M.Sc Data Science Student  
RWTH Aachen University
