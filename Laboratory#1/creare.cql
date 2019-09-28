CREATE KEYSPACE CorporateMessenger WITH REPLICATION = 
{
	'class' : 'SimpleStrategy', 'replication_factor' : 1
};

USE CorporateMessenger;

CREATE TABLE IF NOT EXISTS CorporateMessenger.Users 
(
	Username TEXT,
	Password TEXT,
	PRIMARY KEY(Username)	
);

CREATE TYPE IF NOT EXISTS CorporateMessenger.UDTMsg
(
	MessageText TEXT,
	MessageId int, // Used as counter of all messages
	SentTime timestamp
);

CREATE TABLE IF NOT EXISTS CorporateMessenger.Messages
(
	MessagesData Frozen<UDTMsg>,
	Username TEXT,
	PRIMARY KEY(MessagesData)
);
 
CREATE TABLE IF NOT EXISTS CorporateMessenger.Company
(
	CompanyName TEXT,//Unique company names, like in Slack
	CompanyEmployees list<TEXT>,
	PRIMARY KEY(CompanyName)
);

CREATE TABLE IF NOT EXISTS CorporateMessenger.Department
(
	DepartmentName TEXT,
	DepartmentEmployees list<TEXT>,
	PRIMARY KEY(DepartmentName)
);
