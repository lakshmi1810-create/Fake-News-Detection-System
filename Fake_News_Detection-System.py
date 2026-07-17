import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="khushi_db",
    use_pure=True,
)

mycursor = mydb.cursor()

def view_news():
    data = "SELECT * FROM news"
    mycursor.execute(data)
    result = mycursor.fetchall()
    for x in result:
        print(x)

def search_news():
    print("\n=================================================")
    print("                SEARCH NEWS")
    print("=================================================")
    print("Choose the search criteria to find the desired news record.\n")
    print("1. Search by Title")
    print("2. Search by Category")
    try:
        num = int(input("Enter your preferred search choice : "))
        if num == 1:
            num1 = input("Enter Title : ")
            data = "SELECT * FROM news WHERE title LIKE %s"
            values = ("%" + num1 + "%",)
            mycursor.execute(data, values)
            result = mycursor.fetchall()
            if result:
                for x in result:
                    print(x)
            else:
                print("Invalid title. Please enter a valid title.")
    
        elif num == 2:
            num1 = input("Enter Category : ")
            data = "SELECT * FROM news WHERE category LIKE %s"
            values = ("%" + num1 + "%",)
            mycursor.execute(data, values)
            result = mycursor.fetchall()
            if result:
                for x in result:
                    print(x)
            else:
                print("Invalid category. Please enter a valid category.")
        else:
            print("Invalid choice. Please select a valid choice.")
            return
    except ValueError:
        print("Invalid input! Please enter numbers only.")

def detect_news():
    try:
        num1 = int(input("Enter ID : "))
        data = "SELECT title, description FROM news WHERE id = %s"
        values = (num1,)
        mycursor.execute(data, values)
        result = mycursor.fetchone()
        if result:
            title, description = result 
            text = (title + " " + description).lower()
            fake_keywords = ["breaking", "shocking", "click here", "free money", "100% true", "viral"]
            count = 0
            for keyword in fake_keywords:
                if keyword in text:
                    count += 1
            if count >= 3:
                print("Fake news")
                data = "UPDATE news SET status = 'Fake' WHERE id = %s"
                values = (num1,)
                mycursor.execute(data, values)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
            elif count >= 1:
                print("Needs Verification")
            else:
                print("Real")
                data = "UPDATE news SET status = 'Real' WHERE id = %s"
                values = (num1,)
                mycursor.execute(data, values)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
        else:
            print("No ID found")
    except ValueError:
        print("Invalid input! Please enter numbers only.")


def delete_news():
    try:
        num = int(input("Enter ID : "))
        data = "SELECT * FROM news WHERE id = %s"
        values = (num,)
        mycursor.execute(data, values)
        result = mycursor.fetchone()
        if result:
            data = "DELETE FROM news WHERE id = %s"
            values = (num,)
            mycursor.execute(data, values)
            mydb.commit()
            print("News Deleted Successfully!")
        else:
            print("News not found.")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

def view_fake_news():
    data = "SELECT * FROM news WHERE status = 'Fake'"
    mycursor.execute(data)
    result = mycursor.fetchall()
    for x in result:
        print(x)

def view_real_news():
    data = "SELECT * FROM news WHERE status = 'Real'"
    mycursor.execute(data)
    result = mycursor.fetchall()
    for x in result:
        print(x)

def statistics():
    query1 = "SELECT COUNT(*) FROM news"
    mycursor.execute(query1)
    result1 = mycursor.fetchone()
    query2 = "SELECT COUNT(*) FROM news WHERE status = 'Fake'"
    mycursor.execute(query2)
    result2 = mycursor.fetchone()
    query3 = "SELECT COUNT(*) FROM news WHERE status = 'Real'"
    mycursor.execute(query3)
    result3 = mycursor.fetchone()
    print("\n========== FINAL NEWS REPORT ==========")
    print("Total News : ", result1[0])
    print("Fake News  : ", result2[0])
    print("Real News  : ", result3[0])
    print("========================================")

def menu():
    while True:
        print("\n=================================================")
        print("           FAKE NEWS DETECTION SYSTEM")
        print("=================================================")
        print("1. View all news")
        print("2. Search news")
        print("3. Detect news")
        print("4. Delete news")
        print("5. View fake news")
        print("6. View real news")
        print("7. Final news report")
        print("8. Exit")
        print("\n=================================================")
        try:
            choice = int(input("Enter your choice : "))
            if choice == 1:
                view_news()
            elif choice == 2:
                search_news()
            elif choice == 3:
                detect_news()
            elif choice == 4:
                delete_news()
            elif choice == 5:
                view_fake_news()
            elif choice == 6:
                view_real_news()
            elif choice == 7:
                statistics()
            elif choice == 8:
                print("Thanku for visiting.")
                statistics()
                break
            else:
                print("Invalid choice. PLease select a valid choice.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

menu()
    





        

