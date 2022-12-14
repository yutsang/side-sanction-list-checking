# side-sanction-list-checking
Highly automate the workflow of comparing current customers to UN consolidated sanction list in order to fulfil the KYC/AML requirements in Hong Kong

After 2018, Company secretary service providers in Hong Kong are required to keep monitoring on their existing customers if they are being sanctioned or not. For those being sanctioned customers, the company secretaries have to take actions to report to the authorities and do follow-up actions, for example, unregistered the companies that those being sanctioned people set up from the company registry. Seen in this light, the company secretary service providers have to do regular checking their customer names and company names with the [UN Consolidated Sanction List](https://scsanctions.un.org/consolidated/). However, with unknown reasons, the sanction list only provide the daily snapshot and there would be always some human errors, the regular operations may sometimes be forgot and result in fatal consequences. Therefore, this project is to provide as high level as we could to automate the progress in stead of comparing the customer list and sanction list one by one manually. 

The project would be separated into several parts:
* Download the [UN Consolidated Sanction List](https://scsanctions.un.org/consolidated/) from the internet everyday with the help of the Task Scheduler in windows, or any other tools
* Convert the downloaded [UN Consolidated Sanction List](https://scsanctions.un.org/consolidated/) from PDF to python dataframe
* Analyse the dataframe and extract the sanctioned persons and companies from the dataframe into a readable format
* Compare the current client list to the sanctioned list by using the [Fuzzy Lookup](https://www.mrexcel.com/board/threads/fuzzy-matching-new-version-plus-explanation.195635/post-955137) by Excel VBA and create the macro to do the one-click action for officers so as to reduce the training time and probably automate the process in the future

## User Guide:  
E.g. On-going Monitoring, dated 2021 Oct  
* Step 1: Filter the Control Sheet Column B, keep on or before 2021 Oct only(when roll back)  
* Step 2: Copy and paste the template for on-going sanction check template, named “20xxxxxx_On-going Sanction Check.xlsm” and Select “Enable Macros”  
* Step 3: Copy Control List Column A:K  to “Core” Tab in “20xxxxxx_On-going Sanction Check.xlsm”, select “Paste Value”   
* Step 4: from “AML-Sanction check - monitoring (To print)/ Sanction lists (to print)” Folder, Open “HKICPA_UN Consolidated list_20211019.csv”  
* Step 5: Right-click the Tap “HKICPA_UN Consolidated list_202” in the excel file “HKICPA_UN Consolidated list_20211019.csv”, select “Move or Copy…”, select “(move to end)“ and tick “Create a copy”, then confirm the movement by clicking “OK”, now the sanction list is moved to the template  
* Step 6: Open the template again and rename the Tap “HKICPA_UN Consolidated list_202” to “Sanction List”  
* Step 7: Go back to the Control Sheet, Copy “Company Name” (Both Chinese and English) to the Sanction Check template “Company Name” Tap, there is a written formula in cell C2, right under “Merge” tap, Then double-click the  bottom-right of the C2 Cell to apply the formula to all   
* Step 8: Copy the client name from the control sheet,   

References: 
Fuzzy Lookup Algorithm: https://www.mrexcel.com/board/threads/fuzzy-matching-new-version-plus-explanation.195635/post-955137
