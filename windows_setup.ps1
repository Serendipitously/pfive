# TODO: self sign this script so Powershell will actually run it
Write-Host: "Installing virtualenv and virtualenvwrapper"
pip install virtualenv
pup install virtualenvwrapper-powershell

Import-Module virtualenvwrapper

Write-Host: "Setting up virtual environment: pfivev"
New-VirtualEnvironment pfivev