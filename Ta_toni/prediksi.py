# step 1 import library
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./../Ta_toni/students.csv")


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

plt.bar(df["Jam"],df["Nilai"])
# plt.figure(figsize=(8, 5))
plt.show()

# # step 2 membuat dataset

# data = {
#     "jam_belajar":[1,2,3,4,5,6,7,8,9,10],
#     "nilai": [50,55,60,65,70,75,80,85,90,95]
    
# }

# df = pd.DataFrame(data)

# print(df)

#step 3 tentukan feature dan label
#df.drop(columns=['jam_Kolom'], axis=1) # atau df.drop('Nama_Kolom', axis=1)

x = df.drop(columns=["Jam"])
y = df["Nilai"]

#step 4 train tes split
x_train, xtest, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,  #test_size 0.2 artinya 20% untuk testing, 80% untuk training
    random_state=42 #digunakan agar pembagian data konsisten ketika di jalankan kembali.
)

# # step 5 Membuat model
# model = LinearRegression()

# # step ke 6 training
# model.fit(x_train, y_train)

# #step 7 melakukan prediksi
# prediksi = model.predict([[11]])

# print(prediksi)

# #evaluasi model Mae
# """
# MAE digunakan untuk Regression.
# misalnya :
# Aktual      Predicted
# 100         90
# 200         220
# 300         280

# Error:
# |100 -90| = 10
# |200 - 220| = 20
# |300 - 280| = 20

# MAE:
# (10 + 20 + 20) / 3
# =16.67

# Semakin kecil MAE:
# Semakin baik model.
# """
# from sklearn.metrics import mean_absolute_error

# y_pred = model.predict(xtest)

# mae = mean_absolute_error(y_test, y_pred)

# print("MAE:", mae)

# #evaluasi model Accuracy
# """
# Accuracy biasanya digunakan untuk clarification
# Misalnya kita mempunyai :

# Actual Prediction
# lulus   lulus
# lulus   lulus
# tidak lulus lulus
# lulus   lulus

# Dari 4 data
# 3 benar 1 salah
# accuracy :
# 3/4 = 75%
# """
# from sklearn.metrics import accuracy_score

# accuracy = accuracy_score (y_test, y_pred)

# print("Accuracy", accuracy)


# # plt.bar(df["jam"],df["nilai"])
# # plt.figure(figsize=(8, 5))

# # # plt.title('Total', fontsize=14)
# # # plt.xlabel('Unit_Price', fontsize=12)
# # # plt.ylabel('Total(Rupiah)', fontsize=12)
# # # plt.xticks(rotation=0)
# # # plt.grid(axis='y', linestyle='--', alpha=0.7)
# # # plt.grid(axis='y', linestyle='--', alpha=0.7)
# # plt.show()
