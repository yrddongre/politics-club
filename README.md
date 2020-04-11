# politics-club
Website for Politics Club at Langley


## Azure Installation

1. Create a new Python Web application (see [here](https://portal.azure.com/#create/hub) "Azure Web App Creation Page")
	* Make sure to set the runtime environment as Python 3.7+
2. On the same webpage, open the Azure Cloud Shell terminal
3. Set up storage space to host your website. A pop-up dialog should open to guide you through this set up.
4. Run `git clone <this repo clone URL>`
5. Run `az webapp up -n <webapp name>` Use the name you defined when you created this web application. Use the command any time you pull new changes to the site from Github. 
6. Open a new tab and type in your Azure Site URL.
7. Done!

