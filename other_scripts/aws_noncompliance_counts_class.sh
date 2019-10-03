# Adding MFA authentication automation
#set -x

echo "Switching to PD-PUB AWS Account"

okta_setup() {
    profile="kermit-devops"
    unset AWS_SESSION_TOKEN
    unset AWS_SECRET_ACCESS_KEY
    unset AWS_ACCESS_KEY_ID
    unset AWS_DEFAULT_REGION
    if [ "$2" != "" ]; then
        export AWS_DEFAULT_REGION=$2
    fi
    shift
    shift
    export AWS_PROFILE=$profile
    bbawscli --profile ${profile} --okta-profile ${profile} "$@"
    rv="$?"
    if [ "$rv" != "0" ]; then
        echo "Error in bbawscli call" >&2
        unset AWS_SESSION_TOKEN
        unset AWS_SECRET_ACCESS_KEY
        unset AWS_ACCESS_KEY_ID
        unset AWS_DEFAULT_REGION
        return $rv
    fi
    echo "Switched to aws profile: $profile" >&2
    return 0
}

okta_setup

echo "Running the CLI Command: describe-compliance-by-config-rule"
# Creating Feed file of AWS SecurityHub Results
temp="$(aws configservice describe-compliance-by-config-rule --compliance-types NON_COMPLIANT --region $1 | jq '.ComplianceByConfigRules[].ConfigRuleName' -r -c)"

for x in $temp; do
	echo $x >> data.txt
	temp2="$(aws configservice get-compliance-details-by-config-rule --compliance-types NON_COMPLIANT --region $1 --config-rule-name $x | jq '.EvaluationResults[]|{ResourceType: .EvaluationResultIdentifier.EvaluationResultQualifier.ResourceType, ResourceId: .EvaluationResultIdentifier.EvaluationResultQualifier.ResourceId, ComplianceType }' -c | wc -l)"
	echo $temp2 >> data.txt
done

echo "Data extracted."
