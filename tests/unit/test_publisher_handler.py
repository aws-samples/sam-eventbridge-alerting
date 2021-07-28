import pytest

from eventbridge.eventbridge_publisher import app as publisher_app
from eventbridge.schema.customevent import AWSEvent
from eventbridge.schema.customevent import TheNextEpicEvent_
from eventbridge.schema.customevent import Marshaller

@pytest.fixture()
def eventBridgeEvent():
    """ Generates EventBridge Event"""

    return {
            "id": "7bf73129-1428-4cd3-a780-95db273d1602",
            "detail-type": "The Next Epic Event!!",
            "source": "customevent",
            "account": "123456789012",
            "time": "2015-11-11T21:29:54Z",
            "region": "us-east-1",
            "version": "0",
            "resources": [
            "arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111"
            ],
            "detail": {
            "ADD-YOUR-FIELDS-HERE": ""
            }
    }


def test_lambda_handler(eventBridgeEvent, mocker):

    ret = publisher_app.lambda_handler(eventBridgeEvent, "")

    print(ret)
    awsEventRet:AWSEvent = Marshaller.unmarshall(ret, AWSEvent)
    detailRet:TheNextEpicEvent_ = awsEventRet.detail

    assert awsEventRet.detail_type.startswith("EventBridgePublisherFunction updated event of ")
