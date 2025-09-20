# import pandas as pd
# import io

# # --- DATA: Sample Dataset Banana ---
# # Asli project mein aap 'Bengaluru_House_Data.csv' file se data load karenge.
# # Yahan hum ek sample DataFrame bana rahe hain taaki code chal sake.
# # Is sample mein har tarah ki problem (missing values, range in sqft, etc.) shamil hai.

# # --- Step 1: File ka Path Define Karna ---
# # Agar aapka script 'scripts/' folder mein hai aur data 'data/' folder mein, to path aisa hoga.
# # '..' ka matlab hai ek directory peeche jaana.
# raw_data_path = '../data/Bengaluru_House_Data.csv'
# cleaned_data_path = '../data/cleaned_bengaluru_house_data.csv'

# # --- Step 2: CSV File ko Load Karna ---
# try:
#     # Ab hum dummy data ki jagah asli file se data load kar rahe hain.
#     df = pd.read_csv(raw_data_path)
#     print("File successfully loaded!")
#     print("Dataset ka Shape:", df.shape)
#     print("\nDataset ki shuruaati 5 rows:\n", df.head())
    
#     # --- Yahan par data cleaning ka baaki code aayega ---
#     # Jaise columns drop karna, missing values handle karna, etc.
#     # ...
#     # df_cleaned = ... (saara cleaning logic)
#     # ...
    
#     # print(f"\nCleaned data ko '{cleaned_data_path}' par save kiya ja raha hai...")
#     # df_cleaned.to_csv(cleaned_data_path, index=False)
#     # print("File saved successfully!")

# except FileNotFoundError:
#     print(f"Error: File not found at '{raw_data_path}'")
#     print("Please check karein ki file sahi jagah par hai aur path sahi hai.")


# # 1. Data Load Karna
# # Asli file ke liye aap yeh use karenge: df = pd.read_csv('Bengaluru_House_Data.csv')
# print("--- DATA CLEANING START ---")

# # 2. Faltu Columns Hatana
# # Yeh columns hamare price prediction model ke liye zaroori nahi hain.
# df2 = df.drop(['area_type', 'society', 'balcony', 'availability'], axis='columns')
# print("Faltu columns hatane ke baad Data ki Top 5 Rows:\n", df2.head(), "\n")

# # 3. Missing Values Hatana
# # .isnull().sum() se check karte hain ki kis column mein kitni missing values hain.
# print("Missing values hatane se pehle:\n", df2.isnull().sum(), "\n")
# df3 = df2.dropna() # .dropna() un sabhi rows ko hata deta hai jahan NaN hai.
# print("Missing values hatane ke baad Data ka Shape:", df3.shape)
# print("Missing values hatane ke baad:\n", df3.isnull().sum(), "\n")

# # 4. 'size' Column Saaf Karna
# # '2 BHK', '4 Bedroom' jaise text se sirf number nikalna hai.
# # Hum ek naya column 'bhk' bana rahe hain.
# df3['bhk'] = df3['size'].apply(lambda x: int(x.split(' ')[0]))
# print("'bhk' column banane ke baad Data ki Top 5 Rows:\n", df3.head(), "\n")

# # 5. 'total_sqft' Column Saaf Karna
# # Yeh function check karta hai ki value range mein hai ya single number.
# # Agar range hai (e.g., '1133 - 1384'), to uska average nikalta hai.
# def convert_sqft_to_num(x):
#     try:
#         # Pehle try karo ki kya yeh seedha-seedha number hai
#         return float(x)
#     except:
#         # Agar number nahi hai, to check karo ki kya yeh range hai
#         tokens = x.split('-')
#         if len(tokens) == 2:
#             # Range ke dono parts ko float mein convert karke average return karo
#             return (float(tokens[0]) + float(tokens[1])) / 2
#         # Agar na number hai na range, to isse hum handle nahi kar sakte
#         return None

# df4 = df3.copy()
# df4['total_sqft'] = df4['total_sqft'].apply(convert_sqft_to_num)
# print("'total_sqft' column saaf karne ke baad Data ki Top 5 Rows:\n", df4.head(), "\n")

# # 6. Bachi hui Missing Values Hatana
# # 'total_sqft' ko saaf karne ke baad ho sakta hai kuch values None ban gayi hon.
# # Hum check karke unhe hata denge.
# print("Final cleaning se pehle missing values:\n", df4.isnull().sum(), "\n")
# df5 = df4.dropna()
# print("Final cleaned data ka shape:", df5.shape)

# # 'size' column ko hata dete hain kyunki humne 'bhk' bana liya hai
# df_cleaned = df5.drop('size', axis='columns')

# print("\n--- FINAL CLEANED DATA ---")
# print(df_cleaned.head())

# # 7. Saaf Data Save Karna
# # index=False zaroori hai taaki CSV mein pandas ka index save na ho.
# # df_cleaned.to_csv('cleaned_bengaluru_house_data.csv', index=False)
# print("\nData saaf ho gaya hai aur 'cleaned_bengaluru_house_data.csv' mein save karne ke liye taiyar hai.")
# print("--- DATA CLEANING END ---\n")




import pandas as pd

# --- Step 1: File Paths Define Karna ---
# Yeh relative paths hain jo project structure ke hisaab se hain.
raw_data_path = 'data/Bengaluru_House_Data.csv'
cleaned_data_path = 'data/cleaned_bengaluru_house_data.csv'

print("--- DATA CLEANING SCRIPT START ---")

try:
    # --- Step 2: Asli CSV File ko Load Karna ---
    df = pd.read_csv(raw_data_path)
    print(f"File '{raw_data_path}' successfully loaded!")
    print("Original Data ka Shape:", df.shape)
    
    # --- Step 3: Data Cleaning Logic ---

    # 3a. Faltu Columns Hatana
    df2 = df.drop(['area_type', 'society', 'balcony', 'availability'], axis='columns')
    
    # 3b. Missing Values Hatana
    df3 = df2.dropna()
    
    # 3c. 'size' Column se 'bhk' Column Banana
    # Note: .copy() use karna warnings se bachata hai.
    df4 = df3.copy()
    df4['bhk'] = df4['size'].apply(lambda x: int(x.split(' ')[0]))
    
    # 3d. 'total_sqft' Column ko Saaf Karna
    def convert_sqft_to_num(x):
        try:
            return float(x)
        except:
            tokens = x.split('-')
            if len(tokens) == 2:
                return (float(tokens[0]) + float(tokens[1])) / 2
            return None

    df5 = df4.copy()
    df5['total_sqft'] = df5['total_sqft'].apply(convert_sqft_to_num)
    
    # 3e. Bachi hui Missing Values Hatana
    df6 = df5.dropna()
    
    # 3f. Ab 'size' column ki zaroorat nahi hai.
    df_cleaned = df6.drop('size', axis='columns')
    
    print("\nData cleaning complete!")
    print("Cleaned Data ka Shape:", df_cleaned.shape)

    # --- Step 4: Saaf Data ko nayi CSV file mein Save Karna ---
    df_cleaned.to_csv(cleaned_data_path, index=False)
    print(f"\nCleaned data successfully saved to '{cleaned_data_path}'")

except FileNotFoundError:
    print(f"ERROR: File not found at '{raw_data_path}'")
    print("Please check karein ki file 'data/' folder mein hai aur aap script ko project ke root folder se chala rahe hain.")
except Exception as e:
    print(f"An error occurred: {e}")

print("\n--- DATA CLEANING SCRIPT END ---")

