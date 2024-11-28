import os
def clear_terminal():
    os.system("cls" if os.name=="nt" else "clear")
class Members:
    members_info={}
    def __init__(self,id):
        self.id=id
        Members.members_info[id]={"first name":self.first_name,
                                  "last name":self.last_name,
                                  "status":self.status,}
    
    def display():
        if Members.members_info:
            for id in Members.members_info:
                print(f"First name:{Members.members_info[id]["first name"]}")
                print(f"Last name:{Members.members_info[id]["last name"]}")
                print(f"Membership ID:{id}")
                print(f"Membership status:{Members.members_info[id]["status"]}")
                print("-"*20)
        else:
            print("No members available")

    def search():
        while True:
            print("Search by:")
            print("1)Membership ID")
            print("2)First name")
            print("3)Membership status")
            search_choice=input("Select a choice 1 or 2 or 3: ")
            if search_choice=="1":
                searched_id=input("Enter membership ID: ")
                if searched_id in Members.members_info:
                    for id in Members.members_info:
                        if searched_id==id:
                            print(f"First name:{Members.members_info[id]["first name"]}")
                            print(f"Last name:{Members.members_info[id]["last name"]}")
                            print(f"Membership ID:{id}")
                            print(f"Membership status:{Members.members_info[id]["status"]}")
                            print("-"*20)
                    break
                else:
                    print("Sorry this ID isn't registered")
            elif search_choice=="2":
                searched_name=input("Enter your first name: ")
                for id in Members.members_info:
                    if searched_name==Members.members_info[id]["first name"]:
                        print(f"First name:{Members.members_info[id]["first name"]}")
                        print(f"Last name:{Members.members_info[id]["last name"]}")
                        print(f"Membership ID:{id}")
                        print(f"Membership status:{Members.members_info[id]["status"]}")
                        print("-"*20)
                break
            elif search_choice=="3":
                searched_status=input("Enter the status: ")
                for id in Members.members_info:
                    if searched_status==Members.members_info[id]["status"]:
                        print(f"First name:{Members.members_info[id]["first name"]}")
                        print(f"Last name:{Members.members_info[id]["last name"]}")
                        print(f"Membership ID:{id}")
                        print(f"Membership status:{Members.members_info[id]["status"]}")
                        print("-"*20)
                break
            else:
                print("Please enter a choice 1 or 2 or 3")


def add_members():
    first_name=input("Enter your first name: ")
    last_name=input("Enter your last name: ")
    while True:
        id=input("Enter your membership ID: ")
        if id not in Members.members_info:
            break
        else:
            print("Please enter valid ID")
    status=input("Enter your membership status or click enter: ").lower()
    if status=="active":
        status="active"
    else:
        status="inactive"
    Members.members_info[id]={"first name":first_name,"last name":last_name,"status":status}
    return Members.members_info

while True:
    print("                                                         Welcome to gym membership management")
    print("Choose an Action:")
    print("1)Add new member")
    print("2)Display all members")
    print("3)search for a member")
    print("4)Exit")
    choice=input("Please enter your choice from 1 to 4: ")
    if choice=="1":
        clear_terminal()
        member1=add_members()
        print("Member added successfully")
    elif choice=="2":
        clear_terminal()
        Members.display()
    elif choice=="3":
        clear_terminal()
        Members.search()
    elif choice=="4":
        print("Exiting.....")
        break
    else:
        print("Please enter a choice from 1 to 4")

        