import plivo, plivoxml

auth_id = "Your AUTH_ID"
auth_token = "Your AUTH_TOKEN"

p = plivo.RestAPI(auth_id, auth_token)

params = {
    'to': '2222222222',    # The phone numer to which the call will be placed
    'from' : '1111111111', # The phone number to be used as the caller id

    # answer_url is the URL invoked by Plivo when the outbound call is answered
    # and contains instructions telling Plivo what to do with the call
    'answer_url' : "https://s3.amazonaws.com/static.plivo.com/answer.xml",
    'answer_method' : "GET", # The method used to call the answer_url