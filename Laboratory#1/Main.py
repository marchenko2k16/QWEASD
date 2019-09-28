from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'], port=9042)

if __name__ == "__main__":
    session = cluster.connect('CorporateMessenger')
    session.execute('USE CorporateMessenger')

    session.execute("INSERT INTO CorporateMessenger.Users (Username,Password) VALUES ('Sergey','weaklevelpassword1');")
    session.execute("INSERT INTO CorporateMessenger.Users (Username,Password) VALUES ('Evgeniy','hahaclasic0');")
    session.execute("INSERT INTO CorporateMessenger.Users (Username,Password) VALUES ('Maria','Sayonara');")
    session.execute("SELECT * FROM CorporateMessenger.Users;")
    session.execute("INSERT INTO CorporateMessenger.Messages (MessagesData,Username) VALUES ({MessageText:'Some message sent by Sergey', MessageId:1, SentTime:'2019-09-29 00:00:00'}, 'Sergey');")
    session.execute("INSERT INTO CorporateMessenger.Messages (MessagesData,Username) VALUES ({MessageText:'Some message sent by Evgeniy', MessageId:2, SentTime:'2019-09-29 00:00:01'}, 'Maria');")
    session.execute("INSERT INTO CorporateMessenger.Company (CompanyName,CompanyEmployees) VALUES ('GSC GameWorld',['Sergey', 'Evgeniy', 'Maria']);")
    session.execute("INSERT INTO CorporateMessenger.Department (DepartmentName,DepartmentEmployees) VALUES ('Art', ['Nick','Robert']);")

    session.execute("UPDATE CorporateMessenger.Users Set Password = 'SayonaraBoy' WHERE Username = 'Sergey';")
    session.execute("SELECT * FROM CorporateMessenger.Users;")

    session.execute("UPDATE CorporateMessenger.Messages Set Username = 'Sergey' WHERE MessagesData = {MessageText:'Some message sent by Sergey', MessageId:1, SentTime:'2019-09-29 00:00:00'};")
    session.execute("SELECT * FROM CorporateMessenger.Messages;")

    session.execute("UPDATE CorporateMessenger.Department Set DepartmentEmployees = ['Lex','Dmitriy'] WHERE DepartmentName = 'Art';")
    session.execute("SELECT * FROM CorporateMessenger.Department;")

    session.execute("SELECT Password FROM CorporateMessenger.Users WHERE Username = 'Maria';")
    session.execute("SELECT Username FROM CorporateMessenger.Messages WHERE MessagesData ={MessageText:'Some message sent by Evgeniy', MessageId:2, SentTime:'2019-09-29 00:00:01'};")
    session.execute("SELECT CompanyEmployees FROM CorporateMessenger.Company WHERE CompanyName = 'GSC GameWorld';")
    session.execute("SELECT DepartmentEmployees FROM CorporateMessenger.Department WHERE DepartmentName = 'Art';")

    session.execute("DELETE Password FROM CorporateMessenger.Users WHERE Username = 'Sergey';")
    session.execute("DELETE Username FROM CorporateMessenger.Messages WHERE MessagesData = {MessageText:'Some message sent by Evgeniy', MessageId:2, SentTime:'2019-09-29 00:00:01'};")
    session.execute("DELETE DepartmentEmployees FROM CorporateMessenger.Department WHERE DepartmentName = 'Art';")