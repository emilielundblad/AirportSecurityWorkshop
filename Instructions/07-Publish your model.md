# Task 7 - Publish your model

At the moment, you can test your object recognition model from within the Custom Vision project, but you cannot use it from any other application. In order to do so, you have to publish it first.

1. From the [Custom Vision web page](https://customvision.ai), select your project and then select the __Performance__ tab.

1. Publish your model for prediction, which can be done by selecting __Publish__ and specifying a name for the published iteration. This will make your model accessible to the Prediction API of your Custom Vision Azure resource.

    ![The performance tab is shown, with a red rectangle surrounding the Publish button.](./media/07/unpublished-iteration.png)

1. Wait for the publishing to complete. Once your model has been successfully published, you'll see a "Published" label appear next to your iteration in the left-hand sidebar, and its name will appear in the description of the iteration.

    ![The performance tab is shown, with a red rectangle surrounding the Published label and the name of the published iteration.](./media/07/published-iteration.png)

1. In order to connect to the model, you will need its URL and prediction key. Once your model has been published, you can retrieve this information by selecting __Prediction URL__. This will open up a dialog with information for using the Prediction API, including the __Prediction URL__ and __Prediction Key__.

    ![The performance tab is shown with a red rectangle surrounding the Prediction URL button.](./media/07/published-iteration-prediction-url.png)
 
 1. Make a note of the __Prediction URL__ and __Prediction Key__. You will use them in a future task. Ensure that you choose the url underneath **If you have an image file**.
    ![The performance tab is shown with a red rectangle surrounding the Prediction URL value for using an image file and the Prediction-Key value.](./media/07/prediction-api-info.png)

Your model is now published and can be used from anywhere - provided you have the key. But you don't have an application yet that could use the model. [Let's fix that next](08-Provision%20a%20Web%20App%20resource.md).