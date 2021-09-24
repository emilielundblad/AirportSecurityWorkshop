# Task 4 - Get training data for your AI model

Training an object recognition model from scratch would be a lot of work! Luckily, by using Custom Vision, the basics have already been taken care of. All you have to do is to customize the base model for your particular use case.

The technique you are utilizing is called *machine learning*. If you wanted to teach an AI to recognize a fork, for example, you would provide it with a number of reference images of forks, the so-called *training data*. The model then analyzes the common features of those images to understand what forks in general look like. This way, it can even recognize a fork in images it has never seen before (*test data*).

Now, this task is all about getting some training data. Remember what the case was about? You were building an AI model for airport security, specifically, you want to be able to automatically detect what items are in a passenger's luggage. To train your AI to do for you, you need some images of the items that your AI should be able to detect.

1. Choose the items that you would like to train your AI with. Anything that fits into a suitcase goes! Start with five items - you can always expand later.
1. Find these items in your physcial environment and take pictures of them. Aim for at least 20 images per item. In order to train your model effectively, use images with visual variety. Select images that vary by:
    * camera angle
    * lighting
    * background
    * visual style
    * individual/grouped subject(s)
    * size
    * type

    Additionally, make sure all of your training images meet the following criteria:
    * .jpg, .png, .bmp, or .gif format
    * no greater than 6MB in size (4MB for prediction images)
    * no less than 256 pixels on the shortest edge; any images shorter than this will be automatically scaled up by the Custom Vision Service
1. You will use most of the images as your *training data* in the next task. However, in order to properly test your model, take up to five images of each item to the side. These will be your *test data*. Do not upload them in the next task.

Now you have the images but you have not told the AI yet what to look for. That's why, you will [upload and tag the images](05-Upload%20and%20tag%20your%20training%20data.md) next.