"""
Created on Sun Jun  7 12:48:31 2020
https://towardsdatascience.com/how-to-create-fake-data-with-faker-a835e5b7a9d9
@author: manjg
"""
from faker import Faker
import pandas as pd

def generate_fake_profiles (number_of_records):
    fake = Faker(['en_US'])
    profiles = [fake.profile() for i in range(number_of_records)]
    df_profile = pd.DataFrame(profiles)
    df_profile.to_csv('fake-file.csv')
    print("Operation Complete")

def main():
    generate_fake_profiles(2000)

if __name__ == "__main__":
	main()