from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement


if name == "main":
    cluster = Cluster(['127.0.0.1'], port=9042)
    session = cluster.connect('CorporateMessenger', wait_for_all_pools=True)
    session.execute('USE CorporateMessenger')
    session.execute(
        "BEGIN BATCH "
        "UPDATE CorporateMessenger.Users Set Password = 'SayonaraBoy' WHERE Username = 'Sergey';"
        "INSERT INTO CorporateMessenger.Company (CompanyName,CompanyEmployees) VALUES ('Innovecs',['Masha', 'Sasha', 'Vova']);"
        "APPLY BATCH;")