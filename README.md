# GitSwitch
GitSwitch is an application with a graphical user interface (GUI) that allows users to switch between global Git accounts quickly and store the credentials for each account. This tool is especially useful for individuals who have multiple Git accounts, such as work and personal accounts, and occasionally commit code under the wrong account.

# Installation
Download the latest release of GitSwitch from the GitHub repository.

Extract the downloaded ZIP file to a location of your choice.

# Usage
Double-click the Switch.exe executable to launch GitSwitch.

GitSwitch will display a window with the following capabilities:

Switch Account: Clicking the account will update the global Git credentials and set it as the current account. 
Add Account: Store the credentials for a new Git account.
Remove Account: Remove the stored credentials for the Git account selected.
Exit: Quit the GitSwitch application.
Select the appropriate option from the window and follow the on-screen instructions.

Configuration
GitSwitch stores account credentials in a JSON file named `accountsConfig.json`. This file is located in the same directory as the Switch.exe executable. Each account entry in the JSON file includes the following information:

Account: A unique identifier for the Git account.
Username: The username associated with the Git account.
Email: The email address associated with the Git account.
Ensure that the accountsConfig.json file is not deleted on accident.

Contributing
Contributions to GitSwitch are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.

License
MIT License

Disclaimer
GitSwitch is an open-source project and provided "as is" without warranty or guarantee of any kind. The authors and contributors of GitSwitch shall not be liable for any claim, damages, or other liability arising from the use or distribution of this application. Users are responsible for their actions and are advised to exercise caution when using GitSwitch.
