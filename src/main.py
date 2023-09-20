from Models.Graph import *
from Models.RappiWebScraper import *
from Database.Database import *
import tests

def main():
    
    db = Database()
    db.insert_all_from_file()
    
main()