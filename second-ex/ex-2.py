usersData = []
def main ():
    usersCount = input("please enter user count: ")
    for i in range(int(usersCount)):
        getUsersData()
    searchPersonName(input("please enter user name to search: "))
     
def getUsersData():
        userData = {}
        userData['name'] = input("please enter user name: ")
        userData['age'] = input("please enter user age: ")
        usersData.append(userData)

def searchPersonName(name):
    for user in usersData:
        if user['name'] == name:
            print(user)
            return user
    print("user not found")
main()
