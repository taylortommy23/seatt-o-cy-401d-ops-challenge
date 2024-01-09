# Script to configure automatic screen lock on Windows 10

# Set the desired screen lock timeout value in seconds (e.g., 300 seconds = 5 minutes)
$screenLockTimeoutSeconds = 300

# Set registry path for screen lock timeout
$registryPath = "HKCU:\Control Panel\Desktop"
$registryName = "ScreenSaveTimeOut"

# Set registry path for screen saver
$screenSaverRegistryPath = "HKCU:\Control Panel\Desktop"
$screenSaverRegistryName = "ScreenSaveActive"

# Set registry path for screen saver executable
$screenSaverExeRegistryPath = "HKCU:\Control Panel\Desktop"
$screenSaverExeRegistryName = "SCRNSAVE.EXE"
$screenSaverExeValue = "scrnsave.scr"

# Set registry path for screen saver executable parameters (blank for default)
$screenSaverExeParamsRegistryPath = "HKCU:\Control Panel\Desktop"
$screenSaverExeParamsRegistryName = "ScreenSaverIsSecure"
$screenSaverExeParamsValue = "1"

# Configure screen lock timeout
Set-ItemProperty -Path $registryPath -Name $registryName -Value $screenLockTimeoutSeconds

# Enable screen saver
Set-ItemProperty -Path $screenSaverRegistryPath -Name $screenSaverRegistryName -Value 1

# Set screen saver executable
Set-ItemProperty -Path $screenSaverExeRegistryPath -Name $screenSaverExeRegistryName -Value $screenSaverExeValue

# Set screen saver executable parameters
Set-ItemProperty -Path $screenSaverExeParamsRegistryPath -Name $screenSaverExeParamsRegistryName -Value $screenSaverExeParamsValue

# Display configured values
Write-Host "Automatic screen lock configured with timeout: $screenLockTimeoutSeconds seconds"
Write-Host "Screen saver enabled with executable: $screenSaverExeValue"

# Force a screen lock to apply the changes immediately
rundll32.exe user32.dll,LockWorkStation
