# Task 10 - Set up your Cloud Shell

Working with app development often requires you to have a lot of software installed, from code editors to software packages and runtimes. Luckily, you can avoid this by working from the Cloud Shell. Cloud Shell is a [command line interface (CLI)](https://www.w3schools.com/whatis/whatis_cli.asp) that's running in the Cloud. CLIs can look intimidating at first, if you're not used to them - but don't worry - they are just a way to provide commands to a computer, just like clicking buttons on a graphical user interface.

1. Launch Azure Cloud Shell by navigating to [shell.azure.com](https://shell.azure.com) or by clicking the shell icon in the top of the Azure portal.

    ![Launch Cloud Shell](media/10/portal-launch-icon.png)

    > ##### ℹ️
    > If this is your first time using Cloud Shell, you will be asked to create a storage account. 

1. You can use Cloud Shell with Bash or PowerShell commands. When given the choice, select **Bash**. 

    ![Command choices](media/10/overview-choices.png)

1. Wait for Cloud Shell to launch. It is ready when you see this:

    ```
    Requesting a Cloud Shell.Succeeded.
    Connecting terminal...

    <your_name>@Azure:~$
    ```

1. You can now start typing commands. Type `echo Hello World!` and see what happens. 

Now that you have set up your Cloud Shell, you can start using it to [deploy your Web App](11-Deploy%20your%20Web%20App.md).