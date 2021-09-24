# Task 5 -  Upload and tag your training data

In this section, you will upload and manually tag images to help train the detector. 

1. Return to your Custom Vision project at [customvision.ai](https://customvision.ai), select __Add images__ and then select __Browse local files__. Select __Open__ to upload the images.

    ![The add images control is shown in the upper left, and as a button at bottom center.](./media/05/add-images.png)

    > ##### ℹ️
    > For uploading photos, you can access [customvision.ai](https://customvision.ai) from your phone as well.

1. You'll see your uploaded images in the **Untagged** section of the UI. The next step is to manually tag the objects that you want the detector to learn to recognize. Click the first image to open the tagging dialog window. 

    ![Images uploaded, in Untagged section](./media/05/images-untagged.png)

1. Click and drag a rectangle around the object in your image. Then, enter a new tag name with the **+** button, or select an existing tag from the drop-down list. It's important to tag every instance of the object(s) you want to detect, because the detector uses the untagged background area as a negative example in training. When you're done tagging, click the arrow on the right to save your tags and move on to the next image.

    ![Tagging an object with a rectangular selection](./media/05/image-tagging.png)

Repeat this task until all of your training images have been tagged. Remember to keep a few images for testing later on.
When all of your training images have been added, you can [submit them for training](06-Train%20and%20test%20your%20model.md).