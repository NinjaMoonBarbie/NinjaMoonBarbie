# Create and print the list of books
list_of_books = ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Moby-Dick", "War and Peace"]
print(list_of_books)
# Access and print the 3rd book in the list
print(list_of_books[2])
# Slice and print the first 3 books
print(list_of_books[0:4])
# Concatenate a new list with existing one and print. New books: "Pride and Prejudice", "The Catcher in the Rye".
new_list = ["Pride and Prejudice", "The Catcher in the Rye"]
print(list_of_books + new_list)
# Repeat the list of books twice and print result
print(list_of_books + new_list * 2)
# Modify the list: Change "1984" to "Brave New World"
list_of_books[2] = "Brave New World"
print(list_of_books)
# Add "The Hobbit" to the end of the list
list_of_books.append("The Hobbit")
print(list_of_books)
# Insert "Harry Potter" at the beginning of the list
list_of_books.insert(0, "Harry Potter")
print(list_of_books)
# Remove "Moby Dick" from list
list_of_books.remove("Moby-Dick")
print(list_of_books)
# Delete the second book in the list
del list_of_books[1]
print(list_of_books)
# Pop the last book from the list and print its title
last_book = list_of_books.pop(-1)
print("Popped book:", last_book)
# Check if "The Great Gatsby" is in the list and print results
if "The Great Gatsby" in list_of_books:
    print("The Great Gatsby is in the list")
else:
    print("The Great Gatsby is NOT in the list")
# Print final list of books
print(list_of_books)
