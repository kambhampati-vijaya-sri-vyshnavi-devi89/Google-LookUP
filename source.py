'''
Python Program to Perform Google Search
'''

# Import the necessary module
import pywhatkit as kt

def google_search():
    print("Welcome to the Google Search Tool!")
    print("Enter your search query (or type 'exit' to quit).")

    while True:
        search_query = input("Search: ").strip()
        
        if search_query.lower() == "exit":
            print("Exiting the search tool. Have a great day!")
            break
        
        if search_query:
            try:
                print(f"Searching for '{search_query}' on Google...")
                kt.search(search_query)
            except Exception as e:
                print("An error occurred while searching:", str(e))
        else:
            print("Please enter a valid search query.")

# Run the function
if __name__ == "__main__":
    google_search()
