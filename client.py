import requests
import time

BASE_URL = 'http://localhost:5000/wordcount/api/v1.0'
TASK_URL = BASE_URL + '/count'
STATUS_URL = BASE_URL + '/status/'

def client(words):
    task_response = requests.post(TASK_URL, json={'words': words})
    task_id = task_response.json()['task_id']
    status_response = requests.get(STATUS_URL + task_id)
    status = status_response.json()['status']
    while status == 'PENDING':
        time.sleep(5)
        status_response = requests.get(STATUS_URL + task_id)
        status = status_response.json()['status']
    result = status_response.json()['result']
    print(result)



if __name__ == '__main__':
    words = ['han', 'hon', 'den', 'denna', 'denne', 'hen']    
    client(words)