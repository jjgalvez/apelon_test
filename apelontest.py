from zeep import Client
import datetime

import pretend


client = Client(wsdl='http://localhost:5000/soap/DtsQueryDaoWS?wsdl')

with open('envelope.xml', 'r') as e:
    envelope = e.read()


options = dict(
    snapshotDate=datetime.date(2013,12,1),
    firstResult=0,
    limit=10,
    status="A",
    subsetSearch=0,
    contentId=5102,
    ALL_CONTENT=1,
    DEFAULT_LIMIT=1000
)

response = pretend.stub(
        status_code=200,
        headers = {},
        content=envelope)

operation = client.service._binding._operations['findConceptsWithNameMatching']
result = client.service._binding.process_reply(
    client, operation, response
)

print(result)
