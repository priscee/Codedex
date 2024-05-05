books = ['Zero to One', 'The Lean Startup', 'The Mom Test', 'Make It Stick', 'Life in Code']

#add one more book to list
books.append('Zero to Sold')
#remove index 0
books.remove('Zero to One')
#zero to one removed, lean startup index becomes 0
books.pop(0)

print(books)