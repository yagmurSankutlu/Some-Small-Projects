#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import warnings
warnings.filterwarnings("ignore")


# In[ ]:


import pandas as pd

data = pd.DataFrame(columns = ["book's name", "book's number", "book's category", "book' placement", "book's author", "book's publishment year"
])
taken_books_data = pd.DataFrame(columns = ["id of the people who take it", "book's name", "book's number", "book's category", "book' placement", "book's author", "book's publishment year"
])


# In[ ]:


def add_book(book_name , book_number,book_category,book_placement,book_author,book_publishment_year):
    
    global data
 
    if not (book_name and book_number and book_category and book_placement and book_author and book_publishment_year):
        print("Can not add book to the system. Missing parameter(s).")
        return data
    
    try:
        book_name = book_name.strip()
        book_number = int(book_number)
        book_publishment_year = int(book_publishment_year)
    except ValueError:
        print("Can not add book to the system. Improper parameter(s).")
        return data
    
    book = {"book's name": book_name, "book's number": book_number, "book's category": book_category, "book' placement": book_placement, "book's author": book_author, "book's publishment year": book_publishment_year}
    data = data.append(book, ignore_index=True)
    print(f"{book_name} has added to the system.")
    
    return data


# In[ ]:


def find_book(book_name_or_number):
    
    global data, taken_books_data
    
    if not (book_name_or_number):
        print("Can not find book. Missing parameter(s).")
        return None
    
    result = None
    
    if type(book_name_or_number==str):
        result = data[data["book's name"] == book_name_or_number]
        
    if type(book_name_or_number)==int and result is None:
        result = data[data["book's number"] == int(book_name_or_number)]
        
    elif type(book_name_or_number)==int and result is not None:
        result = result[data["book's number"] == int(book_name_or_number)]
        
    if result is not None and not result.empty:
        
        book_identities = []
        for index, row in result.iterrows():
            
            book_name = row["book's name"]
            book_number = row["book's number"]
            book_category = row["book's category"]
            book_placement = row["book' placement"]
            book_author = row["book's author"]
            
            book_identities.append(f"{book_name} {book_number} {book_category} {book_placement} {book_author} ")

        output_string = "\n".join(book_identities)
        
        print(f"book has not taken {output_string}")
        return output_string
    
    result_taken = None

    if type(book_name_or_number)==str :
        result_taken = taken_books_data[taken_books_data["book's name"] == book_name_or_number]

    if type(book_name_or_number)==int and result_taken is None:
        result_taken = taken_books_data[taken_books_data["book's number"] == int(book_name_or_number)]

    elif type(book_name_or_number)==int and result_taken is not None:
        result_taken = result_taken[taken_books_data["book's number"] == int(book_name_or_number)]

    if result_taken is not None and not result_taken.empty:
        
        book_identities = []
        for index, row in result_taken.iterrows():
            
            book_name = row["book's name"]
            book_number = row["book's number"]
            book_category = row["book's category"]
            book_placement = row["book' placement"]
            book_author = row["book's author"]
            
            book_identities.append(f"{book_name} {book_number} {book_category} {book_placement} {book_author}")

        output_string = "\n".join(book_identities)
        
        print(f"book has taken {output_string}")
        return output_string
    
    else:
        print("Can not find book. There is no book like this in the system.")


# In[ ]:


def list_an_author_books(book_author):
    
    global data
    
    if not (book_author):
        print("Can not find book in the system. Missing parameter(s).")
        return None
    
    else:
        result = data[(data["book's author"].str.strip() == book_author.strip())]
        
        if result.empty == False:
            
            for index, row in result.iterrows():
                book_name = row["book's name"].strip()
                book_number = row["book's number"]
                print(book_name,book_number)
            
            return result
        
        else:
            print("There are no books by this author in this system.")
            return None


# In[ ]:


def take_book(book_name_or_number, id_of_people_take_it):
    
    global data, taken_books_data
    

    result_data = data[(data["book's name"].str.strip() == book_name_or_number.strip())]
    result_taken_books_data = taken_books_data[(taken_books_data["book's name"].str.strip() == book_name_or_number.strip())] 

    if result_data.empty and result_taken_books_data.empty:
        result_data = data[(data["book's number"] == int(book_name_or_number))]
        result_taken_books_data = taken_books_data[(taken_books_data["book's number"] == int(book_name_or_number))] 


    if not (book_name_or_number and id_of_people_take_it):
        print("Can not take book. Missing parameter(s).")
        return None
        
 
    if  result_data.empty == True and result_taken_books_data.empty == True:
        print("Can not give book. There is no book like this in this system.")
        return None

    if result_taken_books_data.empty == False:
        print("Can not give book. Someone has already taken it")
        return None


    if result_data.empty == False and result_taken_books_data.empty == True:

        book_data = result_data.iloc[0].copy()
        book_data["id of the people who take it"]=id_of_people_take_it
        
        taken_books_data = taken_books_data.append(book_data, ignore_index=True)
        
        data = data.drop(book_data.name)  # remove the book from the original data
   

        print(f"{book_data[0]} has given with no problem")
        return taken_books_data


# In[ ]:


def return_book(book_name_or_number):
    
    global data, taken_books_data 

    result_data = data[(data["book's name"] == book_name_or_number)]
    result_taken_books_data = taken_books_data[(taken_books_data["book's name"] == book_name_or_number)] 

    if result_data.empty and result_taken_books_data.empty:
        result_data = data[(data["book's number"] == int(book_name_or_number))]
        result_taken_books_data = taken_books_data[(taken_books_data["book's number"] == int(book_name_or_number))] 


    if not (book_name_or_number):
        print("Can not give book. Missing parameter(s).")
        return None
    
    if  result_data.empty == True and result_taken_books_data.empty == True:
        print("Can not give book. There is no book like this in this system.")
        return None
    
    if result_data.empty == False and result_taken_books_data.empty == True:
        print("Can not return book. It has not been taken by anyone")
        return None
    
    if result_taken_books_data.empty == False:
        
        book_data = result_taken_books_data.iloc[0].copy()
        
        book_data=book_data[1:]
        
        data = data.append(book_data, ignore_index=True)
        
        taken_books_data = taken_books_data.drop(book_data.name)  # remove the book from the original d
        
    
        print(f"{book_data[0]} has  been returned.")
        return taken_books_data 


# In[ ]:


def list_books():
    
    global data
    
    if data.empty:
        
        print("There are no books in the system.")
        
    else:
        
        book_identities = []
        for index, row in data.iterrows():
            
            book_name = row["book's name"]
            book_number = row["book's number"]

            
            book_identities.append(f"{book_name} {book_number}")

        output_string = "\n".join(book_identities)
        print(output_string)
        return output_string
    
    


# In[ ]:


def list_taken_books():
    
    global taken_books_data
    
    if taken_books_data.empty:
        
        print("No one has taken books :(")
        
    else:
        
        book_identities = []
        for index, row in taken_books_data.iterrows():
            
            book_name = row["book's name"]
            book_number = row["book's number"]
            id_of_people_take_it = row["id of the people who take it"]

            
            book_identities.append(f"{book_name} {book_number} {id_of_people_take_it}")

        output_string = "\n".join(book_identities)
        print(output_string)
        return output_string
    


# In[ ]:


def list_books_before_after_year(year, before_or_after):
    
    global data
    
    if not (year and before_or_after):
        print("Can not list book(s). Missing parameter(s).")
        
    try:
        year = int(year)
    except ValueError:
        print("Can not list book(s). Improper input.")
        return None
    
    if before_or_after == "before":
        
        selected_rows = data[data["book's publishment year"] < year]
        if selected_rows.empty:
            print(f"There are no books that is published before {year} in the system.")
            return None
        
    if before_or_after == "after":
        
        selected_rows = data[data["book's publishment year"] > year]
        if selected_rows.empty:
            print(f"There are no books that is published after {year} in the system.")
            return None
        
    book_names_numbers = []
    for index, row in selected_rows.iterrows():
        book_name = row["book's name"]
        book_number = row["book's number"]
        book_names_numbers.append(f"{book_name} {book_number}")
        
    output_string = "\n".join(book_names_numbers)
    print(output_string)
      


# In[ ]:


def help():

    print("add book", "| -a |", "adds a new book to the system")
    print("find book", "| -f |", "this command finds a book at the system")
    print("list an author's books", "| -la |", "finds the books of an author which are in the system")
    print("take book", "| -t |", "give a book to someone")
    print("return book", "| -r |", "returns a book which have taken by someone")
    print("list books", "| -l |", "lists every book in the system")
    print("list taken books", "| -lt |", "lists every taken book in the system")
    print("list books before/after year", "| -ly |", "lists every book in the system with given dates")
    print("help", "| -h |", "prints all commands and their descriptions")
    print("quit", "| -q |", "quits program")


# In[ ]:


def quit():
    
    print("See you later :)")


# In[ ]:


def main():
    
    command = input("What would you want to do? (Write help for command list)")

    if len(command) == 0:
        return main()

    
    #adds a new book to the system.
    elif command == "add book" or command == "-a":
        try:
            book_name , book_number, book_category, book_placement, book_author, book_publishment_year = input().split(',')
            add_book(book_name , book_number, book_category, book_placement, book_author, book_publishment_year)
        except ValueError:
            print("Can not add book to the system. Missing parameter(s).")
        
        return main()

        
    #finds a book at the system.
    elif command == "find book" or command == "-f":
        
        try:
            book_name_or_number = input()
            find_book(book_name_or_number)
        except ValueError:
            print("Can not find book. Missing parameter(s).")
        
            
        return main()

        
    #finds the books of an author which are in the system.
    elif command == "list an author's books" or command == "-la":
 
        try:
            book_author = input()
            list_an_author_books(book_author)
        except ValueError:
            print("Can not find book in the system. Missing parameter(s).")
       
        return main()

        
    elif command == "take book" or command == "-t":
    
        try:
            book_name_or_number, id_of_people_take_it = input().split(',')
            take_book(book_name_or_number, id_of_people_take_it)
            
        except ValueError:
            print("Can not give book. Missing parameter(s).")
       
        return main()

        
    elif command == "return book" or command == "-r":
        
        book_name_or_number = input()
        return_book(book_name_or_number)
        return main()

        
    elif command == "list books" or command == "-l":

        list_books()
        return main()

    elif command == "list taken books" or command == "-lt":

        list_taken_books()
        return main()

    elif command == "list books before/after year" or command == "-ly":
    
        try:
            year, before_or_after = input().split(',')
            list_books_before_after_year(year, before_or_after)
            
        except ValueError:
            print("Can not list book(s). Missing parameter(s).")
        return main()

    elif command == "help" or command == "-h":

        help()
        return main()

    elif command == "quit" or command == "-q":

        quit()

    else:
        print("You have entered a command that does not exist. Write ‘help’ to get to know commands.")
        return main()
    
main()

