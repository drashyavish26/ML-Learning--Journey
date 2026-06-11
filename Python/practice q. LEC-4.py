#WAP to store folowingg word meaningss in a python dictionary 
dictionary= {
"table": ["a piece of furniture ", " list of facts and figures"],
"cat": " a small animal"  
}
print(dictionary)



#WAP a giiven list of subjects . assume one classroom is required for 1 subject . how many classrooms are needed by all students
classroom= {
     "python", "java","CPP", "python", "javascript", "java","python", "java","CPP","c"
}
print(classroom)
print(len(classroom))




#WAP to enter marks of 3 subjects  from the user and store them in dictionary. start with an empty dictionary and add one by one . use subject name as key and marks as value 
marks= {}
x=int(input("enter phy marks:"))
marks.update({"phy": x})

x=int(input("enter chem:"))
x= marks.update({"chem": x })

x=int(input("enter mat:"))
x= marks.update({"mat": x })
print(marks)

#WAP to figure a way to store 9 & 9.0 as seperate value in the set 
#(take help of built in data types)
values= {9 , 9.0 }
print(values)
values={9, "9.0"}
print(values)




