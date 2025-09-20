# # Yeh dictionary hamare "seekhe hue" model ki tarah kaam kar rahi hai.
# # Ismein har location ke liye base price aur per BHK price hai.
# location_data = {
#     'Whitefield': {'base_price': 40, 'price_per_bhk': 15},
#     'Marathahalli': {'base_price': 35, 'price_per_bhk': 12},
#     'Electronic City Phase II': {'base_price': 25, 'price_per_bhk': 8},
#     'Yelahanka': {'base_price': 50, 'price_per_bhk': 20}
# }

# def calculate_price(location, bhk):
#     """
#     Yeh function di gayi location aur bhk ke liye ghar ki keemat calculate karta hai.
#     Formula: Estimated Price = Base Price + (BHK * Price per BHK)
#     """
#     # Sabse pehle check karo ki di gayi location hamare data mein hai ya nahi.
#     if location in location_data:
#         # Agar location hai, to uski details nikalo.
#         base_price = location_data[location]['base_price']
#         price_per_bhk = location_data[location]['price_per_bhk']
        
#         # Formula ka istemal karke keemat calculate karo.
#         estimated_price = base_price + (bhk * price_per_bhk)
        
#         # Ek saaf-suthra message return karo.
#         return f"The calculated price for a {bhk} BHK in {location} is {estimated_price} Lakhs."
#     else:
#         # Agar location hamare data mein nahi hai, to error message return karo.
#         return f"Sorry, we do not have pricing data for the location '{location}'."

# # --- Function ko Test Karna ---
# print("--- MODEL SIMULATION START ---")

# # Test Case 1: Ek location jo data mein hai (Whitefield)
# price1 = calculate_price('Whitefield', 3)
# print("Test Case 1 (Valid Location):")
# print(price1)

# # Test Case 2: Ek aur valid location (Yelahanka)
# price2 = calculate_price('Yelahanka', 2)
# print("\nTest Case 2 (Valid Location):")
# print(price2)

# # Test Case 3: Ek aisi location jo data mein nahi hai (Koramangala)
# price3 = calculate_price('Koramangala', 3)
# print("\nTest Case 3 (Invalid Location):")
# print(price3)

# print("\n--- MODEL SIMULATION END ---")


# Upgrade 2
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# # Saaf kiye hue data ka Path
# cleaned_data_path = 'data/cleaned_bengaluru_house_data.csv'

# print("--- MODEL TRAINING SCRIPT START ---")

# try:
#     # Saaf kiye hue data ko Load Karna
#     df = pd.read_csv(cleaned_data_path)
#     print(f"File '{cleaned_data_path}' successfully loaded!")

#     # Data ko Model ke liye Taiyar Karna (One-Hot Encoding)
#     dummies = pd.get_dummies(df.location)
#     df2 = pd.concat([df, dummies], axis='columns')
#     df3 = df2.drop('location', axis='columns')
    
#     # Features (X) aur Target (y) ko alag karna
#     X = df3.drop('price', axis='columns')
#     y = df3.price

#     # Model Train Karna
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
#     model = LinearRegression()
#     model.fit(X_train, y_train)
    
#     print(f"\nModel successfully trained!")
#     print(f"Model ka testing score (R-squared): {model.score(X_test, y_test) * 100:.2f}%")

#     # Web App ke liye Model ke Parameters Nikalna
#     print("\n--- JavaScript mein use karne ke liye Model Parameters ---")
#     print(f"\nIntercept (Base Price): {model.intercept_}")
    
#     coefficients = pd.DataFrame({'feature': X.columns, 'coefficient': model.coef_})
#     print("\nCoefficients (har feature ke liye weight):")
#     # .to_string() poora output dikhayega
#     print(coefficients.to_string())

# except FileNotFoundError:
#     print(f"ERROR: File not found at '{cleaned_data_path}'")
# except Exception as e:
#     print(f"An error occurred: {e}")

# print("\n--- MODEL TRAINING SCRIPT END ---")



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import json # JSON library ko import karein

# Saaf kiye hue data ka Path
cleaned_data_path = 'data/cleaned_bengaluru_house_data.csv'

print("--- MODEL TRAINING SCRIPT START ---")

try:
    # Saaf kiye hue data ko Load Karna
    df = pd.read_csv(cleaned_data_path)
    print(f"File '{cleaned_data_path}' successfully loaded!")

    # Data ko Model ke liye Taiyar Karna (One-Hot Encoding)
    dummies = pd.get_dummies(df.location)
    df2 = pd.concat([df, dummies], axis='columns')
    df3 = df2.drop('location', axis='columns')
    
    # Features (X) aur Target (y) ko alag karna
    X = df3.drop('price', axis='columns')
    y = df3.price

    # Model Train Karna
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    print(f"\nModel successfully trained!")
    print(f"Model ka testing score (R-squared): {model.score(X_test, y_test) * 100:.2f}%")

    # --- YAHAN NAYA LOGIC HAI ---
    # Web App ke liye Model ke Parameters Nikalna

    print("\n--- JavaScript mein use karne ke liye Model Parameters ---")
    print(f"\nIntercept (Base Price): {model.intercept_}")
    
    # DataFrame banana
    coefficients_df = pd.DataFrame({'feature': X.columns, 'coefficient': model.coef_})
    
    # DataFrame ko Python Dictionary mein badalna
    # 'feature' column key banega aur 'coefficient' column value.
    coeffs_dict = coefficients_df.set_index('feature')['coefficient'].to_dict()

    # Dictionary ko sundar format wale JSON string mein badalna
    coeffs_json_string = json.dumps(coeffs_dict, indent=4)

    print("\n--- Neeche diye gaye poore object ko copy karke 'coefficients' mein paste karein ---")
    # Poora JSON string print karna
    print(coeffs_json_string)


except FileNotFoundError:
    print(f"ERROR: File not found at '{cleaned_data_path}'")
except Exception as e:
    print(f"An error occurred: {e}")

print("\n--- MODEL TRAINING SCRIPT END ---")
