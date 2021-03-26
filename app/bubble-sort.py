import json

from flask import Flask, render_template, jsonify, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

# Python3 Bubble sort
@app.route('/', methods=['GET'])

def bubbleSort():
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
    return json.dumps(arr)
           
# number sequence to test above
arr = [66, 37, 23, 17, 27, 14, 95]
   
bubbleSort()

if __name__ == '__main__':
        app.run(host="0.0.0.0", port=5000)
