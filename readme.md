# Checkpoint Avanan - home assignment . Ran Erlich

# words

This is a dictionary that keeps in memory the words recieved
each word will keep an array of time stamps and number of occurences. for example in the input curl requests:

curl -X POST 'http://localhost/api/v1/events' -d 'Avanan is a leading Enterprise Solution
for Cloud Email email and Collaboration Security'
curl -X POST 'http://localhost/api/v1/events' -d 'CheckPoint Research have been
observing an enormous rise in email attacks since the beginning of 2020'

will create a dictionary of tuples. in each touple we store the timestamp in seconds and the number of times the word was found:

words={
'email' : [(1696164351,2), (1696164358,1)],
'Checkpoint' :[(1696164358,1)],
'Avanan' :[(1696164351,1)],
'security:[(1696164351,1)]

}

# todo

Use gunicorn with non-blocking async workers
Containerize the app with Docker
Deploy it in a Kubernetes cluster
Add an API Gateway in front of Kube
