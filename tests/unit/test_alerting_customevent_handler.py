import pytest

from eventbridge.eventbridge_alerting import app as alerting_app
from eventbridge.schema.customevent import AWSEvent
from eventbridge.schema.customevent import TheNextEpicEvent_
from eventbridge.schema.customevent import Marshaller

@pytest.fixture()
def customeventBridgeEvent():
    """ Generates EventBridge Custom Event"""

    return {
            "version":"0",
            "id":"7bf73129-1428-4cd3-a780-95db273d1602",
            "detail-type":"Custom Event Type",
            "source":"customevent",
            "account":"123456789012",
            "time":"2015-11-11T21:29:54Z",
            "region":"us-east-1",
            "detail":{
              "ADD-YOUR-FIELDS-HERE":""
            },
            "comment": "Your custom event here!"
    }

def test_customevent_lambda_handler(customeventBridgeEvent, mocker):
  
    print("Test TheNextEpicEvent_ !")

    ret = alerting_app.lambda_handler(customeventBridgeEvent, "")
    
    awsEventRet:AWSEvent = Marshaller.unmarshall(ret, AWSEvent)
    detailRet:TheNextEpicEvent_ = awsEventRet.detail

    #print(awsEventRet.detail_type)
    assert awsEventRet.detail_type.startswith("Is this the next epic event")