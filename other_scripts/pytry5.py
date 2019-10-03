# Bookmark references: https://www.tutorialspoint.com/python/dictionary_get.htm
# Bookmark references: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/config.html#ConfigService.Client.describe_compliance_by_config_rule

import boto3
from botocore.exceptions import ClientError

config = boto3.client('config')

list_x = []
try:
    response = config.describe_compliance_by_config_rule(
        ComplianceTypes=[
            'NON_COMPLIANT'
        ]
)
    for rule in response['ComplianceByConfigRules']:
        list_x.append(rule.get('ConfigRuleName'))
except ClientError as e:
    print(e)

print(list_x)

list_y = []
count = 0

try:
    for rname in list_x:
        print(rname)
        response = config.get_compliance_details_by_config_rule(
            ConfigRuleName=rname
)
        for result in response['EvaluationResults']:
            count += 1
            list_y.append(result.get('EvaluationResultIdentifier'))
        print(count)
except ClientError as e:
    print(e)
