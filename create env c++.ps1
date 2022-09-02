$BASE_PATH = "C:\_Build\Contests"
$TEMPLATE_FILE_NAME = "template.cpp"
$TEMPLATE_FILE_DIR = "C:\_Build\Contests\Template_files"
$TEMPLATE_FILE_LOCATION = Join-Path -Path $TEMPLATE_FILE_DIR -ChildPath $TEMPLATE_FILE_NAME

$PLATFORM = Read-Host -Prompt """
Select contest platform:
    0. Unknown
    1. Codeforces
    2. Codewars
...
"""

if ($PLATFORM -eq 1) {
    $ROUND = Read-Host -Prompt "Enter current round"

    $PLATFORM = "Codeforces"
    $CODE_DIR = Join-Path -Path $BASE_PATH -ChildPath $PLATFORM
    $CODE_DIR = Join-Path -Path $CODE_DIR -ChildPath "C++"
    $CODE_DIR = Join-Path -Path $CODE_DIR -ChildPath "$ROUND"

    Write-Host "Creating c++ template for $PLATFORM" 
    Write-Host "Path: $CODE_DIR"

    New-Item  -ItemType "directory" -Path $CODE_DIR

    $FILES = "A", "B", "C", "D", "E"
    Foreach ($FILE_NAME in $FILES) {
        Copy-Item $TEMPLATE_FILE_LOCATION -Destination $CODE_DIR
        Rename-Item -Path "$CODE_DIR\$TEMPLATE_FILE_NAME" -NewName "$FILE_NAME.cpp"
    }

}
elseif ($PLATFORM -eq 2) {
    $DIFFICULTY = Read-Host -Prompt "Enter kata difficulty"
    $FILE_NAME = Read-Host -Prompt "Enter file name"

    $PLATFORM = "Codewars"
    $CODE_DIR = Join-Path -Path $BASE_PATH -ChildPath $PLATFORM
    $CODE_DIR = Join-Path -Path $CODE_DIR -ChildPath $DIFFICULTY

    Write-Host "Creating c++ template for $PLATFORM" 
    Write-Host "Path: $CODE_DIR"

    New-Item  -ItemType "directory" -Path $CODE_DIR

    Copy-Item $TEMPLATE_FILE_LOCATION -Destination $CODE_DIR
    Rename-Item -Path "$CODE_DIR\$TEMPLATE_FILE_NAME" -NewName "$FILE_NAME.cpp"

}
else {
    write-host("Cannot create a template")
    exit
}

$PARENT_PATH = (get-item $CODE_DIR ).parent.parent
$PARENT_PATH = Join-Path -Path $PARENT_PATH -ChildPath "C++"

Start-Process -FilePath "code" -WorkingDirectory $PARENT_PATH -ArgumentList .
