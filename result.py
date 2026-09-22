print("====RESULT SYSTEM====")
name=input("Enter student name: ")
student_id=input("Enter student ID: ")
print("\nStudent Information")
print("-------------------")
print("Student Name: ",name)
print("Student Id: ",student_id)

print("\nEnter marks")

bangla_mark=int(input("Bangla: "))
english_mark=int(input("English: "))
python_mark=int(input("Python: "))

total=bangla_mark+english_mark+python_mark

average=total/3

print("\nRESULT")
print("------------")       
print("Total mark: ",total)
print("Avareage Mark: ",average)

if average >=80:
    print("You got A+")
elif average >=70:
    print("You got A")
elif average >60:
    print("You got A-")
elif average >50:
    print("You got B")
elif average >40:
    print("You got C")
elif average >34:
    print("You got D")
else:
    print("You got F")