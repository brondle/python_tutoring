
def converttostr(input_seq, seperator):
   # Join all the strings in list
   final_str = seperator.join(input_seq)
   return final_str

# List of month names
listOfwords = ["Jan" , "Feb", "Mar", "April", "May", "Jun", "Jul"]

# List of words names separated with a space
seperator = ' '
print(converttostr(listOfwords, seperator))


charList = ['p','y','t','h','o','n',' ','p','r','o','g','r','a','m','m','i','n','g']

# Let's convert charList to a string.
finalString = ''.join(charList)

print(charList)
print(finalString)


sourceList = ["I" , "got", 60, "in", "Science", 70, "in", "English",", and", 66, "in", "Maths"]
# Let's convert sourceList to a list of strings and then join its elements.
stringList = ' '.join([str(item) for item in sourceList ])
print(stringList)

#Get a comma-separated string from a list of numbers
numList = [20, 213, 4587, 7869]
print(str(numList).strip('[]'))

#Alternatively, we can use map() function to convert the items in the list to a string.
print ('\n'.join(map(str, numList)))