bash        # switch to Bash
pwsh        # switch back to PowerShell
date   #nash
Get-Date #pwsl

az upgrade          # Update the CLI
az version          # Check version

az interactive

exit

az login --use-device-code
az account list --output table
az account set --subscription "<your-subscription-name>"
az group create --name ritesh-rg --location centralindia
az storage account create --name riteshstorage12345 --resource-group ritesh-rg --location centralindia --sku Standard_LRS
az resource list --resource-group ritesh-rg --output table
az group delete --name ritesh-rg --yes --no-wait

