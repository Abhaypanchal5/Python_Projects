import pyshortener                # pip install pyshortener

def shorten_link(link):           # Function to shorten the URL
    s = pyshortener.shorten(link)
    return s

Long_link = input("Enter the long URL: ")   # Taking input of the long URL from the user
short_link = shorten_link(Long_link)
print("Shortened URL:", short_link)         # Printing the shortened URL


# this code uses the pyshortener library to shorten a given long URL.
# The user is prompted to enter a long URL, which is then passed to the shorten_link function. 
# The function uses the pyshortener library to shorten the URL and returns the shortened version, which is then printed to the user.