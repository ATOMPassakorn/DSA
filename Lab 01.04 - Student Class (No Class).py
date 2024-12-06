"""Lab 01.04 - Student Class (No Class)"""
def student():
    """Lab 01.04 - Student Class (No Class)"""
    stname=[]
    stsex=[]
    stage=[]
    stid=[]
    stgpa=[]
    for i in range(3):
        name=input()
        sex=input()
        stsex.append(sex)
        stname.append(name)
        age=input()
        stage.append(age)
        id=input()
        stid.append(id)
        gpa=float(input())
        stgpa.append(gpa)
    choose=input()
    if choose==stid[0]:
        if stsex[0]=="Male":
            print(f"Mr {stname[0]} ({stage[0]}) ID: {stid[0]} GPA {stgpa[0]:.2f}")
        else:
            print(f"Miss {stname[0]} ({stage[0]}) ID: {stid[0]} GPA {stgpa[0]:.2f}")
    elif choose==stid[1]:
        if stsex[1]=="Male":
            print(f"Mr {stname[1]} ({stage[1]}) ID: {stid[1]} GPA {stgpa[1]:.2f}")
        else:
            print(f"Miss {stname[1]} ({stage[1]}) ID: {stid[1]} GPA {stgpa[1]:.2f}")
    elif choose==stid[2]:
        if stsex[2]=="Male":
            print(f"Mr {stname[2]} ({stage[2]}) ID: {stid[2]} GPA {stgpa[2]:.2f}")
        else:
            print(f"Miss {stname[2]} ({stage[2]}) ID: {stid[2]} GPA {stgpa[2]:.2f}")
    else:
        print("Student not found")
student()
