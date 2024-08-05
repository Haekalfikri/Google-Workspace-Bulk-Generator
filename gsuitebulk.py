#  Gsuite / Google Workspace Bulk Generator by Haekal Fikri (fb.com/haekalfikri.id) Seller Gsuite Sejak 2016

import pandas as pd
from faker import Faker
import hashlib

# Fungsi untuk mengumpulkan input pengguna
def get_user_input():
    file_name = input("Masukkan nama file (tanpa ekstensi): ")
    region = input("Masukkan region (contoh: id_ID untuk Indonesia / en_US untuk Bule): ")
    domain = input("Masukkan domain email (contoh: example.com): ")
    password = input("Masukkan password yang ingin digunakan: ")
    org_unit = input("Masukkan org unit path (contoh: /IT): ")
    change_password = input("Change password at next sign-in? (true/false): ").lower() == 'true'
    num_records = int(input("Masukkan jumlah data yang ingin dihasilkan: "))
    return file_name, region, domain, password, org_unit, change_password, num_records

# Set up the Faker instance berdasarkan region yang dipilih pengguna
def generate_fake_data(region, domain, password, org_unit, change_password, num_records):
    fake = Faker(region)
    data = []
    for _ in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f"{first_name.lower()}{last_name.lower()}@{domain}"
        
        record = [
            first_name,
            last_name,
            email,
            password,
            '',
            org_unit,
            '',
            '',  # Recovery Email
            '',  # Home Secondary Email
            '',  # Work Secondary Email
            '',  # Recovery Phone
            '',  # Work Phone
            '',  # Home Phone
            '',  # Mobile Phone
            '',  # Work Address
            '',  # Home Address
            '',  # Employee ID
            '',  # Employee Type
            '',  # Employee Title
            '',  # Manager Email
            '',  # Department
            '',  # Cost Center
            '',  # Building ID
            '',  # Floor Name
            '',  # Floor Section
            change_password,
            '',  # New Status
            ''   # Advanced Protection Program enrollment
        ]
        data.append(record)
    return data

# Mengumpulkan input pengguna
file_name, region, domain, password, org_unit, change_password, num_records = get_user_input()

# Generate the data
data = generate_fake_data(region, domain, password, org_unit, change_password, num_records)

# Define the column names
columns = [
    "First Name [Required]",
    "Last Name [Required]",
    "Email Address [Required]",
    "Password [Required]",
    "Password Hash Function [UPLOAD ONLY]",
    "Org Unit Path [Required]",
    "New Primary Email [UPLOAD ONLY]",
    "Recovery Email",
    "Home Secondary Email",
    "Work Secondary Email",
    "Recovery Phone [MUST BE IN THE E.164 FORMAT]",
    "Work Phone",
    "Home Phone",
    "Mobile Phone",
    "Work Address",
    "Home Address",
    "Employee ID",
    "Employee Type",
    "Employee Title",
    "Manager Email",
    "Department",
    "Cost Center",
    "Building ID",
    "Floor Name",
    "Floor Section",
    "Change Password at Next Sign-In",
    "New Status [UPLOAD ONLY]",
    "Advanced Protection Program enrollment"
]

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to CSV
csv_file_name = f"{file_name}.csv"
df.to_csv(csv_file_name, index=False)


print(f"Data generated and saved to {csv_file_name}")
