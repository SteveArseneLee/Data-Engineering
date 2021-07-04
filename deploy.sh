rm *.zip
zip lisztfever.zip -r *

aws s3 rm s3://areha/lisztfever/lisztfever.zip
aws s3 cp ./lisztfever.zip s3://areha/lisztfever/lisztfever.zip
aws lambda update-function-code --function-name lisztfever --s3-bucket areha --s3-key lisztfever/lisztfever.zip
