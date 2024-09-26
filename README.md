# Simple S3 download/upload script

## Installation

Use the package manager pip3 to install.

```bash
pip3 install -r requirements.txt
```

## Config
First, **you should check config.yaml.**
Region, Bucket, Folder  


## Usage 

For download, run below script 

```
sh down.sh <target_object_name>
```

It will download a file with the same name as the object name in your script execution folder


For upload, run below script

```
sh up.sh <file_path>
```

It will upload a object with the same name as the file name in your script execution folder