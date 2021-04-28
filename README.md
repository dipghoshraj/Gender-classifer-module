# GENDER-CLASSIFIER
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Gender classifier is a python libary written over a classification model which can classify gender of the human inside the image
  - Classify gender from a image
  - Model train on tensorflow (CNN)


#### Building for source
First install all requirement file:
```sh
>>> pip install glcassifier
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

### NOTE :
```
This modlue have been inspired from - https://www.youtube.com/watch?v=WOuAI5DhHyU

Author: Dip Ghosh
email: dipghoshraj@gmail.com
IOT and robotics developer with a handson experience in Software development and DevOps.
```


<!-- **Free Software, Yeah it's fucking truth!** -->