{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3a84fff0-6a83-4391-bed1-e855c56c95ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===== Car Price Prediction =====\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter vehicle age (in years):  4\n",
      "Enter kilometers driven:  40697\n",
      "Enter mileage (km/l):  13.68\n",
      "Enter engine capacity (cc):  2393\n",
      "Enter max power (bhp):  147.51\n",
      "Enter number of seats:  7\n",
      "\n",
      "Enter brand (e.g., Hyundai, BMW):  Toyota\n",
      "Enter model (e.g., Creta, i20):  crysta gx\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Select seller type:\n",
      "1. Individual\n",
      "2. Dealer\n",
      "3. Trustmark Dealer\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter choice number:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Select fuel type:\n",
      "1. Petrol\n",
      "2. Diesel\n",
      "3. LPG\n",
      "4. Electric\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter choice number:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Select transmission type:\n",
      "1. Manual\n",
      "2. Automatic\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter choice number:  1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "===== Result =====\n",
      "Predicted Selling Price: 1659919.39\n"
     ]
    }
   ],
   "source": [
    "import joblib\n",
    "import pandas as pd\n",
    "\n",
    "# Load model and features\n",
    "model = joblib.load(\"car_price_model.pklt\")\n",
    "feature_columns = joblib.load(\"features.pklt\")\n",
    "\n",
    "print(\"===== Car Price Prediction =====\\n\")\n",
    "\n",
    "# Numeric inputs\n",
    "vehicle_age = int(input(\"Enter vehicle age (in years): \"))\n",
    "km_driven = int(input(\"Enter kilometers driven: \"))\n",
    "mileage = float(input(\"Enter mileage (km/l): \"))\n",
    "engine = int(input(\"Enter engine capacity (cc): \"))\n",
    "max_power = float(input(\"Enter max power (bhp): \"))\n",
    "seats = int(input(\"Enter number of seats: \"))\n",
    "\n",
    "\n",
    "# Helper function for menu selection\n",
    "def choose_option(prompt, options):\n",
    "    print(f\"\\n{prompt}\")\n",
    "    for i, option in enumerate(options, 1):\n",
    "        print(f\"{i}. {option}\")\n",
    "    \n",
    "    choice = int(input(\"Enter choice number: \"))\n",
    "    return options[choice - 1]\n",
    "\n",
    "\n",
    "# Categorical inputs with options\n",
    "\n",
    "brand = input(\"\\nEnter brand (e.g., Hyundai, BMW): \")\n",
    "model_name = input(\"Enter model (e.g., Creta, i20): \")\n",
    "\n",
    "seller_options = [\"Individual\", \"Dealer\", \"Trustmark Dealer\"]\n",
    "seller_type = choose_option(\"Select seller type:\", seller_options)\n",
    "\n",
    "fuel_options = [\"Petrol\", \"Diesel\", \"LPG\", \"Electric\"]\n",
    "fuel_type = choose_option(\"Select fuel type:\", fuel_options)\n",
    "\n",
    "transmission_options = [\"Manual\", \"Automatic\"]\n",
    "transmission = choose_option(\"Select transmission type:\", transmission_options)\n",
    "\n",
    "\n",
    "# Create input dictionary\n",
    "new_car = {\n",
    "    \"vehicle_age\": vehicle_age,\n",
    "    \"km_driven\": km_driven,\n",
    "    \"mileage\": mileage,\n",
    "    \"engine\": engine,\n",
    "    \"max_power\": max_power,\n",
    "    \"seats\": seats,\n",
    "    \"brand\": brand,\n",
    "    \"model\": model_name,\n",
    "    \"seller_type\": seller_type,\n",
    "    \"fuel_type\": fuel_type,\n",
    "    \"transmission_type\": transmission\n",
    "}\n",
    "\n",
    "\n",
    "# Convert to DataFrame\n",
    "input_df = pd.DataFrame([new_car])\n",
    "\n",
    "# One-hot encoding\n",
    "input_encoded = pd.get_dummies(input_df)\n",
    "\n",
    "# Match training columns\n",
    "input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)\n",
    "\n",
    "# Predict\n",
    "predicted_price = model.predict(input_encoded)[0]\n",
    "\n",
    "print(\"\\n===== Result =====\")\n",
    "print(f\"Predicted Selling Price: {round(predicted_price, 2)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ed0f1ee-1dd2-4a7f-a791-2e5443986a53",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:anaconda3]",
   "language": "python",
   "name": "conda-env-anaconda3-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
