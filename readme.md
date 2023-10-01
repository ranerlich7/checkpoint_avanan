# Checkpoint Avanan - home assignment . Ran Erlich

# words

This is a dictionary that keeps in memory the words recieved
each word will keep an array of time stamps. for example

curl -X POST 'http://localhost/api/v1/events' -d 'Avanan is a leading Enterprise Solution
for Cloud Email and Collaboration Security'
curl -X POST 'http://localhost/api/v1/events' -d 'CheckPoint Research have been
observing an enormous rise in email attacks since the beginning of 2020'

will create a dictionary of tuples. in each touple we store the timestamp in seconds and the number of times the word was found:
words={
'email' : [(1696164351,1), (1696164358,1)],
'Checkpoint' :[(1696164358,1)],
'Avanan' :[(1696164351,1)],
'security:[(1696164351,1)]

}

/events – which will get a sentence (String) and counts the number of the occurrence
of the following keywords – “checkpoint”, “avanan”, “email” and “security”.

• /stats – which will get a time interval (in seconds) and will return a JSON with the
number of occurrence of the above keywords in the received interval time.

<!-- You could:

Use gunicorn with non-blocking async workers
Containerize the app with Docker
Deploy it in a Kubernetes cluster -->

Add an API Gateway in front of Kube
