import joblib
import pandas as pd

# Load model and features
model = joblib.load("model_car_pred/car_price_model.pklt")
feature_columns = joblib.load("model_car_pred/features.pklt")

print("===== Car Price Prediction =====\n")

# Numeric inputs
vehicle_age = int(input("Enter vehicle age (in years): "))
km_driven = int(input("Enter kilometers driven: "))
mileage = float(input("Enter mileage (km/l): "))
engine = int(input("Enter engine capacity (cc): "))
max_power = float(input("Enter max power (bhp): "))
seats = int(input("Enter number of seats: "))

# Helper function
def choose_option(prompt, options):
    print(f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = int(input("Enter choice number: "))
    return options[choice - 1]

# Categorical inputs
brand = input("\nEnter brand (e.g., Hyundai, BMW): ")
model_name = input("Enter model (e.g., Creta, i20): ")

seller_options = ["Individual", "Dealer", "Trustmark Dealer"]
seller_type = choose_option("Select seller type:", seller_options)

fuel_options = ["Petrol", "Diesel", "LPG", "Electric"]
fuel_type = choose_option("Select fuel type:", fuel_options)

transmission_options = ["Manual", "Automatic"]
transmission = choose_option("Select transmission type:", transmission_options)

# Create input dictionary
new_car = {
    "vehicle_age": vehicle_age,
    "km_driven": km_driven,
    "mileage": mileage,
    "engine": engine,
    "max_power": max_power,
    "seats": seats,
    "brand": brand,
    "model": model_name,
    "seller_type": seller_type,
    "fuel_type": fuel_type,
    "transmission_type": transmission
}

# Convert to DataFrame
input_df = pd.DataFrame([new_car])

# One-hot encoding
input_encoded = pd.get_dummies(input_df)

# Match training columns
input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)

# Predict
predicted_price = model.predict(input_encoded)[0]

print("\n===== Result =====")
print(f"Predicted Selling Price: {round(predicted_price, 2)}")