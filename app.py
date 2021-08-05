#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify
from flask_cors import CORS
import recommendation

app = Flask(__name__)
CORS(app)



@app.route('/movie', methods=['GET'])
def recommend_movies():
    res = recommendation.results(request.args.get('title'))
    return '''<h1>Your recommended  movies are : {}</h1>'''.format(res)




if __name__ == '__main__':
    app.run(port=5000,debug=True,use_reloader=False)


# In[ ]:




