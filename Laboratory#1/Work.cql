INSERT INTO CorporateMessenger.Users (Username,Password) VALUES ('Sergey','weaklevelpassword1');
INSERT INTO CorporateMessenger.Users (Username,Password) VALUES ('Evgeniy','hahaclasic0');
INSERT INTO CorporateMessenger.Users (Username,Password) VALUES ('Maria','Sayonara');

SELECT * FROM CorporateMessenger.Users;

INSERT INTO CorporateMessenger.Messages (MessagesData,Username) VALUES ({MessageText:'Some message sent by Sergey', MessageId:1, SentTime:'2019-09-29 00:00:00'}, 'Sergey');
INSERT INTO CorporateMessenger.Messages (MessagesData,Username) VALUES ({MessageText:'Some message sent by Evgeniy', MessageId:2, SentTime:'2019-09-29 00:00:01'}, 'Maria');

INSERT INTO CorporateMessenger.Company (CompanyName,CompanyEmployees) VALUES ('GSC GameWorld',['Sergey', 'Evgeniy', 'Maria']);

INSERT INTO CorporateMessenger.Department (DepartmentName,DepartmentEmployees) VALUES ('Art', ['Nick','Robert']);

UPDATE CorporateMessenger.Users Set Password = 'SayonaraBoy' WHERE Username = 'Sergey';
SELECT * FROM CorporateMessenger.Users;

UPDATE CorporateMessenger.Messages Set Username = 'Sergey' WHERE MessagesData = {MessageText:'Some message sent by Sergey', MessageId:1, SentTime:'2019-09-29 00:00:00'};
SELECT * FROM CorporateMessenger.Messages;

UPDATE CorporateMessenger.Department Set DepartmentEmployees = ['Lex','Dmitriy'] WHERE DepartmentName = 'Art';

SELECT Password FROM CorporateMessenger.Users WHERE Username = 'Maria';
SELECT Username FROM CorporateMessenger.Messages WHERE MessagesData ={MessageText:'Some message sent by Evgeniy', MessageId:2, SentTime:'2019-09-29 00:00:01'};
SELECT CompanyEmployees FROM CorporateMessenger.Company WHERE CompanyName = 'GSC GameWorld';
SELECT DepartmentEmployees FROM CorporateMessenger.Department WHERE DepartmentName = 'Art';


DELETE Password FROM CorporateMessenger.Users WHERE Username = 'Sergey';
DELETE Username FROM CorporateMessenger.Messages WHERE MessagesData = {MessageText:'Some message sent by Evgeniy', MessageId:2, SentTime:'2019-09-29 00:00:01'};
DELETE DepartmentEmployees FROM CorporateMessenger.Department WHERE DepartmentName = 'Art';
