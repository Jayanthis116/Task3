Name="Jayanthi S"
Course="Bsc(ComputerScience)"
College name="Vivekanandha College of Arts and Science For Womens"
sub1_Tamil=int(input("Enter the mark1:"))
sub2_English=int(input("Enter the mark2:"))
sub3_Maths=int(input("Enter the mark3:"))
sub4_physics=int(input("Enter the mark4:"))
sub5_Chemistry=int(input("Enter the mark5:"))
sub6_Computerscience=int(input("Enter the mark6:"))

if(sub1_Tamil > sub2_English and sub2_English > sub3_Maths and sub3_Maths > sub4_physics and sub5_Chemisrty > sub6_ComputerScience):
    max_val=sub5_Chemistry

elif(sub2_English > sub3_Maths and sub2_English > sub4_physics and sub2_English > sub5_Chemistry and sub2_English and sub6_Computerscience):
     Max_val=sub2_English
elif(sub3_Maths >  sub3_Maths and sub4_physics > sub5_Chemistry and sub3_Maths > sub6_Computerscience):
    Max_val=sub3_Maths
elif(sub4_physics > sub5_Chemistry and sub4_physics > sub6_Computerscience):
     Max_val=sub4_physics
elif(sub5_Chemistry > sub6_Computerscience):
     Max_val=sub5_Chemistry
else:
     Max_val=sub6_Computerscience
print("Maximum value=",Max_val)



if(sub1_Tamil < sub2_English and sub1_Tamil < sub3_Maths and sub1_Tamil < sub4_physics and sub1_Tamil < sub5_Chemistry and sub1_Tamil < sub6_Computerscience):
     min_val=sub1_Tamil
elif(sub2_English < sub3_Maths and sub2_English < sub4_physics and sub2_English < sub5_Chemistry and sub2_English and sub6_Computerscience):
     Min_val=sub2_English
elif(sub3_Maths < sub4_physics and sub3_Maths < sub5_Chemistry and sub3_Maths < sub6_Computerscience):
    Min_val=sub3_Maths
elif(sub4_physics < sub5_Chemistry and sub4_physics < sub6_Computerscience):
     Min_val=sub4_physics
elif(sub5_Chemistry < sub6_Computerscience):
     Min_val=sub5_Chemistry
else:
     min_val=sub6_Computerscience
print("Minimum value=",min_val)



   
