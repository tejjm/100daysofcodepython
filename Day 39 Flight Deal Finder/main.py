# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager
from pprint import pprint
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)
