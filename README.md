# GENDER-CLASSIFIER
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Gender classifier is a python libary written over a classification model which can classify gender of the human inside the image
  - Classify gender from a image
  - Model train on tensorflow (CNN)


#### Building for source
First install all requirement file:
```sh
>>> pip install gclassifier
```
 

### Run the drawing code:

Step 1 :  Encode a message with shiftencoder
```
>>> from gclassifier import image_classifier
>>> import cv2
```
Step 2 :  Decode the message using shiftencoder
```
>>> img = cv2.imread('7.jpg')
>>> a = image_classifier(frame=img)
['woman']
```

License
----
MIT

PYPI MODULE
----------------
https://pypi.org/project/gclassifier/

CONTRIBUTIONS
----------------
Bug reports and pull requests are always welcome on GitHub at https://github.com/dipghoshraj/Gender-classifer-module. This project is intended to help developers and no restriction to use, welcoming space for collaboration, and contributors are expected to adhere to the Contributor Covenant code of conduct.


### NOTE :
```
This modlue have been inspired from - https://www.youtube.com/watch?v=WOuAI5DhHyU

Author: Dip Ghosh
email: dipghoshraj@gmail.com
IOT and robotics developer with a handson experience in Software development and DevOps.
```


<!-- **Free Software, Yeah it's true!** -->
