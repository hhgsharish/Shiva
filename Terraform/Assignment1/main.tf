#Terraform Code to create an EC2Instance in AWS Cloud
provider "aws" {
  #Access key and secret key are not needed
  #refers from the environment variables
  #Add env variables in powershell like this 
  #$env:AWS_ACCESS_KEY_ID="xxxxxxxx"
  #$env:AWS_SECRET_ACCESS_KEY="xxxxxx"
  region     = "us-east-2"
}

resource "aws_instance" "web" {
  ami           = "ami-0cb91c7de36eed2cb"
  instance_type = "t2.micro"
  tags = {
    Name = "FirstEC2_Instance"
  }
}
