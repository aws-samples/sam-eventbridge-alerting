from schema.aws.cloudwatch.cloudwatchalarmstatechange import Marshaller
from schema.aws.cloudwatch.cloudwatchalarmstatechange import AWSEvent
from schema.aws.cloudwatch.cloudwatchalarmstatechange import CloudWatchAlarmStateChange
from schema.customevent import TheNextEpicEvent_ # Custom Event


def proc_cwevent(awsEvent):
    
    detail:CloudWatchAlarmStateChange = awsEvent.detail

    #Execute business logic

    #Make updates to event payload, if desired
    awsEvent.detail_type = "EventBridgeAlertingFunction updated event of CloudWatch Alarm Alert" + awsEvent.detail_type;

    #Return event for further processing
    return Marshaller.marshall(awsEvent)

def proc_customevent(awsEvent):
    
    detail:TheNextEpicEvent_ = awsEvent.detail

    #Execute business logic

    #Make updates to event payload, if desired
    awsEvent.detail_type = "Is this the next epic event!? " + awsEvent.detail_type;

    #Return event for further processing
    return Marshaller.marshall(awsEvent)

def lambda_handler(event, context):
    
    print("SAM Alerting: %s" % event)
    
    """Sample Lambda function reacting to EventBridge events

    Parameters
    ----------
    event: dict, required
        Event Bridge Events Format

        Event doc: https://docs.aws.amazon.com/eventbridge/latest/userguide/event-types.html

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
        The same input event file
    """
    
    #Deserialize event into strongly typed object
    awsEvent:AWSEvent = Marshaller.unmarshall(event, AWSEvent)

    if awsEvent.detail_type == "CloudWatch Alarm State Change":
        proc_cwevent(awsEvent)
    else:
        proc_customevent(awsEvent)

    #Return event for further processing
    return Marshaller.marshall(awsEvent)

   