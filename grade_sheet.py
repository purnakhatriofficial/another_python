subject_marks = int(input("Enter the your Marks :"))

if subject_marks >= 91 and subject_marks < 100:
    print(f"Your Grade is A+ :")

elif subject_marks >= 81  and subject_marks < 91:
    print(f"Your Grade is A :")

elif subject_marks >=71 and subject_marks < 81:
  print(f"Your Grade is B+ :")

elif subject_marks >=61 and subject_marks < 71:
   print(f"Your Grade is B :")

elif subject_marks >=51 and subject_marks < 61:
   print(f"Your Grade is C+ :")

elif subject_marks >=41 and subject_marks <51:
   print(f"Your Grade is C :")

elif subject_marks >= 33 and subject_marks < 41:
   print(f"Your Grade is D :")

elif subject_marks >= 21 and subject_marks < 33:
   print(f"Your Grade is E+ :")

elif subject_marks >=0 and subject_marks < 21:
   print(f"Your Grade is E : ")

else:
   print(f"You Faild")