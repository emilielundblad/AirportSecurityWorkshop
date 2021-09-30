# Task 12 - Ready for takeoff!

Everything is in place. It's time to test your app!

1. Navigate to your Web App's URL. Select **Choose File** and upload an image that you want to test. Make sure that you choose an image that was not included in your model's training data. Then, hit **Submit**. 

    > ##### ℹ️
    > If you see an `internal server error` after submitting your image, check the following:
    > * the image is less than 4MB in size
    > * the image has the .jpg, .png, .bmp, or .gif format
    > * all of the app settings are spelled exactly like shown in [Task 9](09-Configure%20your%20Web%20App.md)

1. In the background, your app sends the picture you uploaded to your AI model, which will return a list of objects it detects. The **Probability** value shows how certain your AI model is about having detected this object in the image. Your web app will only show objects with a certain minimum probability value. You can change this value on the start screen of your app. 

    ![List of detected objects](media/12/dangerous_objects.png)

1. Try a few different images. You can return to the start screen with your browser's **Back** button.

Congratulations! You have made it to the end of the guided workshop. Throughout the past twelve tasks, you have learned to provision Azure resources, trained your own object detection AI, and deployed your own Web App. But the fun doesn't have to end here. If you have time left, consider trying these suggestions before you [clean up](13-Cleanup.md).

### Improve your AI

You might have noticed that your AI model is not detecting everything correctly yet. You can still improve your model! Upload more images to your project at [https://www.customvision.ai/](https://www.customvision.ai/) and tag them. You can now re-train your model on the expanded data set. Don't forget to publish the new iteration and update the prediction URL in the Web App's app settings.

### Challenge other participants

If you have participated in this workshop with others, try to challenge one of their AI models. Ask another participant for the URL to their Web App and what objects they have trained the model on. Then try to "smuggle" a dangerous item past their model with an image of your choice. Your feedback could help them re-train their model to make it more secure!

### Improve your Web App

You might have notices that your Web App is not necessarily the prettiest, or most feature-rich. If you are comfortable editing the code, feel free to improve the design or functionality of the app. You can edit the code in the Cloud Shell and redeploy it with the same command you used in [Task 11](11-Deploy%20your%20Web%20App.md). What additions can you come up with?
