import csv
import os
import numpy as np


FILE_NAME ="students.csv"

#======================
#Fungsi CSV
#=======================


def baca_csv():
    data =[]

    if os.path.exists(FILE_NAME) : 
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                data.append({
                    "nama": row["Nama"],
                    "kelas": row["Kelas"],
                    "jam": int(row["Jam"]},
                    "nilai": int(row["Nilai"])
                    
                })
    
    return data

def simpan_csv(data):
    with open(FILE_NAME,"w", newline="", encoding="utf-8") as file:
        fieldnames = ["Nama", "Kelas", "Jam", "Nilai", ]

        writer = csv.DictWriter(file,fieldnames=fieldnames)

        writer.writeheader()

        for siswa in data:
            writer.writerow ({
                "Nama": siswa["nama"],
                "Kelas": siswa["kelas"],
                "Jam": siswa["jam"],
                "Nilai": siswa["nilai"]
            })

# ==========================
# CRUD
# ============================

def tambah_data(data):
    print("\n=== Tamabah Data ===")

    nama = input("Nama : ")
    kelas = input("Kelas :")
    jam = input("Jam :")

    while True:
        try:
            nilai = int(input("Nilai :"))

            if 0 <= nilai <= 100:
                break
            else:
                print("Nilai harus antara 0-100")

        except ValueError:
                print("Masukan angka!")
        
    data.append({
        "nama": nama,
        "kelas": kelas,
        "jam": jam,
        "nilai": nilai

    })

    simpan_csv(data)

    print("\n data berhasil ditambahkan.")

def tampil_data(data):
    print("\n=================")
    print("   DATA SISWA     ")
    print("===================")

    if len(data)== 0:
        print("Belum ada data")
        return

    print(f"{'No':<5} {'nama':<20}{'kelas':<15}{'jam':<15}{'nilai'}")

    print("-" * 25 + "\n")

    for i, siswa in enumerate(data, start=1):
        print(f"{i:<5} {siswa['nama']:<20}{siswa['kelas']:<15}{siswa['jam']:<15}{siswa['nilai']:}")

def hapus_data(data):

    tampil_data(data)

    if len(data) ==0:
        return
    
    try:
        nomor = int(input("\nNomor yang akan di hapus: "))

        if 1 <= nomor <= len(data):

            data.pop(nomor-1)

            simpan_csv (data)

            print("Data berhasil di hapus")

        else:
            print("Nomor tidak di temukan")

    except ValueError:
        print("Input Harus Angka")


# ====================================
# ANALIS NUMPY
# ======================================

def analisis_nilai(data):

    print("\n========== ANALISIS NILAI ===========")

    if len(data) == 0:
        print("Belum ada data.")
        return

    nilai = np.array([siswa['nilai'] for siswa in data])

    print("Jumlah Siswa   :", len(nilai))
    print("Rata-rata      :", np.mean(nilai))
    print("Nilai Tetinggi :", np.max(nilai))
    print("Niali Terendah :", np.min(nilai))

# ==================================
# MENU
# ====================================

def menu():

    data = baca_csv()

    while True :

        print("\n============================================")
        print("=============== STUDENT DATA MANAGER =========")
        print("1. Tambah Data (Create)")
        print("2. Tampilkan Data (Read)")    
        print("3. Hapus Data (Delete)")
        print("4. Analisis Nilai")
        print("5. Keluar")

        pilih = input ("Pilih menu :")

        if pilih == "1":
            tambah_data(data)

        elif pilih == "2":
            tampil_data(data)

        elif pilih == "3":
            hapus_data(data)

        elif pilih == "4":
            analisis_nilai(data)

        elif pilih == "5":
            print("Keluar dari program.")
            break

        else:
                print("Menu tidak tersedi.\n")

# MAIN PROGRAM
menu()


