# A basic code where letters from the name and surname are cut into 2 and mixed together

print("Let's Mashup some names")
first_name = input("What's the first name (Name Surname):\n")
second_name = input("What's the second name (Name Surname):\n")

space = first_name.find(' ')
first_name1 = first_name[:space]  # first name of the first name
first_name2 = first_name[1+space:len(first_name)]  # surname of the first name

space1 = second_name.find(' ')
second_name1 = second_name[:space1]
second_name2 = second_name[space1+1:len(second_name)]

first_mashup1_first = first_name1[:int(len(first_name1)/2)]  # halfway
second_mashup1_first = first_name1[int(len(first_name1)/2):len(first_name1)]

first_mashup1_second = first_name2[:int(len(first_name2)/2)]
second_mashup1_second = first_name2[int(len(first_name2)/2):len(first_name2)]

first_mashup2_first = second_name1[:int(len(second_name1)/2)]
second_mashup2_first = second_name1[int(len(second_name1)/2):len(second_name1)]

first_mashup2_second = second_name2[:int(len(second_name2)/2)]
second_mashup2_second = second_name2[int(len(second_name2)/2):len(second_name2)]
# splitting all the names into halves for the mashup
new_first_name = first_mashup1_first+second_mashup2_first+' '+first_mashup1_second+second_mashup2_second
new_second_name = first_mashup2_first+second_mashup1_first+" "+first_mashup2_second+second_mashup1_second

print(f'{new_first_name}\n{new_second_name}')
