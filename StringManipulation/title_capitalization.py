# Write a function that takes a string and returns a string with each first letter capitalized.
def title_capitalization(title):
    # Convert the title to lowercase
    title = title.lower()
    # Split the title into a list of words
    title = title.split()
    # Capitalize the first letter of each word
    title = [word[0].upper() + word[1:] for word in title]
    # Join the words back together
    return ' '.join(title)

# Test Cases
print(title_capitalization('the great gatsby')) # The Great Gatsby
print(title_capitalization('the catcher in the rye')) # The Catcher In The Rye
print(title_capitalization('the lord')) # The Lord