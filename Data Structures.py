#Lists
courses = ['Maths', 'Physics', 'English', 'CompScie']
print(courses)

courses = ['Maths', 'Physics', 'English', 'CompScie']
courses.append('art')     #Add a course to the list
print(courses)

courses = ['Maths', 'Physics', 'English', 'CompScie']
courses.insert(1, 'art')    #Add a course to a specific location on the list
print(courses)

courses = ['Maths', 'Physics', 'English', 'CompScie']
courses.remove('Maths')     #Remove a course from the list
print(courses)

courses.sort()      #Sort courses list