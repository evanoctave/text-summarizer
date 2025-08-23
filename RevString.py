query = str(input("Enter word or phrase: "))


def reverse_string(query):
    if len(query) <= 1:
        return(query)
    else:
        return (query[-1] + reverse_string(query[:-1]))
    
print(reverse_string(query))