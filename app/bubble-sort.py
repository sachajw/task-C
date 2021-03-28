import json

from flask import (Flask, 
                   render_template, 
                   jsonify, 
                   request)
from flask_restful import (Resource,
                          Api,
                          reqparse)

app = Flask(__name__)

def bubbleSort(arr):
    n = len(arr)
   
    # Traverse through all array elements
    for i in range(n):
        swapped = False
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
   
            # traverse the array from 0 to
            # n-i-1. Swap if the element 
            # found is greater than the
            # next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
  
        # IF no two elements were swapped
        # by inner loop, then break
        if swapped == False:
            break
#        return json.dumps(arr)

# number sequence to test above
#arr = [66, 37, 23, 17, 27, 14, 95]

@app.route('/', methods=['GET'])
def bubble():
    arr = [66, 37, 23, 17, 27, 14, 95]
    print (arr)
    for i in range(len(arr)):
#        print ("%d" %arr[i],end=" ")
        return json.dumps(arr)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
