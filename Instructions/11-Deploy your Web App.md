# Task 11 - Deploy your Web App

Despite all of the configuration you have done in the previous tasks, your Web App still only shows a plceholder. It's missing the application code, but now it is finally time to change that! You will use the Cloud Shell to deploy the application code to your app.

1. Copy the following command into your Cloud Shell and hit enter.

    `git clone https://github.com/HenriSchulte-MS/AirportSecurityWorkshop.git`

    This command copies the repository containing the code for the Web App (and these instructions) to the Storage Account that's connected to your Cloud Shell.

1. The previous command created a folder called `AirportSecurityWorkshop` and within it a subfolder called `WebApp`. Navigate to the subfolder with the following command.

    `cd AirportSecurityWorkshop/WebApp`

    After executing this command, you will notice that next to your name the CloudShell now displays the current folder.

    > ##### ℹ️
    > If you would like to visually see the contents of the folder, you can use the command `code .` (including the space and dot) to open a VS Code editor in your Cloud Shell. You can also edit the code this way.

1. The next command will deploy the code within the current folder to your Web App. Before executing it, make sure to replace `<your-app-name>` with the actual name of your Web App that you provided in [Task 8](08-Provision%20a%20Web%20App%20resource.md).

    `az webapp up --sku B1 --name <your-app-name>`

    > ##### ℹ️
    > Wondering what `--sku B1` means? This parameter defines which App Service Plan to use (i.e. what compute resources the app can access). B1 is one of the basic options, but it's more than capable to run our little app.

After a short wait, your Cloud Shell should inform you that the deployment has been sucessful and provide you with a url to launch your Web App. If you are seeing a simple **Airport Security Scan** interface, then you're [ready for takeoff](12-Ready%20for%20Takeoff!.md)!

