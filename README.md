## Mid-Term Presentation: Plotly Dash App utilizing AWS SecurityHub Data Points

**APP URL:**
* You can view the finished app on heroku here https://security-hub.herokuapp.com

**COLOR CODES RETRIEVED FROM:**
* HTML Hex Codes are https://htmlcolorcodes.com/

**DATA COLLECTION FOR THE GRAPH AXIS:**
* The other_scripts folder shows two phases of the pre-work to retrieve the data
* other_scripts/aws_noncompliance_counts_class.sh was my initial attempt at pulling this info in Bash for work
* other_scripts/pytry5.app was my 5th attempt and converting the bash script over to pulling it via Python. 

**NOTE FROM STUDENT:**

I wanted to use data points that I would pull in my current job. Unfortunately, this requires AWS access credentials which I cannot pass into Heroku for security concerns. So my approach was to write a separate script to grab the data that I need and dump the output into a feed file that could used by PlotlyDash. 

My initial approach was to write the script in Bash as that is most familiar and then write a Python version. I found that AWS CLI tools are easiest to use in BASH as they are designed for it. To extract AWS data using a Python script is a bit more challenging. It requires the use of the package Boto3, which is like a wrapper for the command line tools. Boto3 extracts the data in a nested dict/list/dict/list manner. From there you have to find the value pair for the key you are searching on. 

**THE BASH VERSION (aws_noncompliance_counts_class.sh):**

The script invokes a MultiFactor Auth used by my company called Okta to connect to an AWS account. It does two loop statements, 1 to pull the ConfigRuleNames into a list, the next loop reads that list and grabs the non-compliance counts. The resulting data is piped to a feed file with the format:

    configrulename
    count
    configrulename
    count

**THE PYTHON VERSION (pytry5.py):**

This version does not utilize the multifactor auth section, requiring you to do that piece separately. It imports the Boto3 package, as this is required by the AWS SDK for Python. 

    Defines the client name
    Sets up an empty list for the x-ais
    Runs the response request to AWS 
    Passes that into a for loop to append the key:value of ConfigRuleName into the empty list for each rule found in non-compliance
    Prints the x-axis list
    Same thing is repeated for the y-axis list with the exception of a counter being added to output an integer for the number of non-compliance findings
    Prints the count for the y-axis
    Running of the app with a pipe to the feed file is needed as last step and results in the same formatted feed file as the bash version

**THE PLOTLY DASH APP (app.py):**

The goal here is to take the feed file generated and break it into two lists that Plotly can use for x and y axis. I was able to do so by the following:

    Use the open command in python to load the feed file
    Specify a new variable 'lines' read each line and using f.read() combined with splitlines(), break the string out when the /n newline character is encountered
    This results in a list containing [str,int,str,int,str,int]
    I now need to use list splicing to break the long list out into two lists: one for strings (label), one for integers (values)
    lines[::2] -- start at position 0 and give me every other value
    lines[1::2] -- start at position 1 and give me every other value
