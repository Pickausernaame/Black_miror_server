
# coding: utf-8

# In[5]:


from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2

# Initialize the Flask application
app = Flask(__name__)


# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.line(img,(0,0),(511,511),(255,0,0),5)
    cv2.imshow('img',img)
    cv2.waitKey(30)
    # do some fancy processing here....

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")
#cv2.imshow('img',img)

if __name__ == "__main__":
    # start flask app
    app.run(host="0.0.0.0", port=5000)


# In[ ]:




