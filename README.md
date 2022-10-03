# side-sanction-list-checking
Highly automate the workflow of comparing current customers to UN consolidated sanction list in order to fulfil the KYC/AML requirements in Hong Kong

After 2018, Company secretary service providers in Hong Kong are required to keep monitoring on their existing customers if they are being sanctioned or not. For those being sanctioned customers, the company secretaries have to take actions to report to the authorities and do follow-up actions, for example, unregistered the companies that those being sanctioned people set up from the company registry. Seen in this light, the company secretary service providers have to do regular checking their customer names and company names with the [UN Consolidated Sanction List](https://scsanctions.un.org/consolidated/). However, with unknown reasons, the sanction list only provide the daily snapshot and there would be always some human errors, the regular operations may sometimes be forgot and result in fatal consequences. Therefore, this project is to provide as high level as we could to automate the progress in stead of comparing the customer list and sanction list one by one manually. 

The project would be separated into several parts:
* Download the [UN Consolidated Sanction List](https://scsanctions.un.org/consolidated/) from the internet everyday with the help of the Task Scheduler in windows, or any other tools
* Convert the downloaded [UN Consolidated Sanction List](https://scsanctions.un.org/consolidated/) from PDF to python dataframe
* Analyse the dataframe and extract the sanctioned persons and companies from the dataframe into a readable format
* Compare the current client list to the sanctioned list by using the [Fuzzy Lookup](https://www.mrexcel.com/board/threads/fuzzy-matching-new-version-plus-explanation.195635/post-955137) by Excel VBA and create the macro to do the one-click action for officers so as to reduce the training time and probably automate the process in the future

References: 
Fuzzy Lookup Algorithm: https://www.mrexcel.com/board/threads/fuzzy-matching-new-version-plus-explanation.195635/post-955137
