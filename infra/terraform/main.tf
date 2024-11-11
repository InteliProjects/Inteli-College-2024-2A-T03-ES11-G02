provider "aws" {
  region = "us-east-1"
}

# VPC setup
resource "aws_vpc" "grupox_vpc" {
  cidr_block = "10.0.0.0/16"
}

# Internet Gateway
resource "aws_internet_gateway" "grupox_igw" {
  vpc_id = aws_vpc.grupox_vpc.id
}

# Public Subnet
resource "aws_subnet" "grupox_subnet_public1_us_east_1a" {
  vpc_id     = aws_vpc.grupox_vpc.id
  cidr_block = "10.0.1.0/24"
}

# Route Table for Public Subnet
resource "aws_route_table" "grupox_rtb_public" {
  vpc_id = aws_vpc.grupox_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.grupox_igw.id
  }
}

# Route Table Association for Public Subnet
resource "aws_route_table_association" "public_association" {
  subnet_id      = aws_subnet.grupox_subnet_public1_us_east_1a.id
  route_table_id = aws_route_table.grupox_rtb_public.id
}

# Security Group
resource "aws_security_group" "my_sg" {
  vpc_id = aws_vpc.grupox_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 Instances - Ingestion
resource "aws_instance" "ingestion" {
  ami                         = "ami-0ebfd941bbafe70c6"  # Updated Amazon Linux 2 AMI
  instance_type               = "t3.micro"
  key_name                    = "grupox-key"
  subnet_id                   = aws_subnet.grupox_subnet_public1_us_east_1a.id
  security_groups             = [aws_security_group.my_sg.id]
  associate_public_ip_address = true

  tags = {
    Name = "Ingestion-Instance"
  }

  # File provisioning to copy files directly into the EC2 instance
  provisioner "file" {
    source      = "../../src"
    destination = "/home/ec2-user/src"
    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("grupox-key.pem")
      host        = self.public_ip
    }
  }

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install -y python3 python3-pip", 
      # Ensure Python installation is successful
      "python3 --version", 
      "pip3 --version",
      "pip3 install boto3 kafka-python",
      # Add some logging for troubleshooting
      "echo 'Navigating to src directory'",
      "cd /home/ec2-user/src",
      "echo 'Installing requirements'",
      "pip3 install -r requirements.txt",
      "echo 'Running ingestion script'",
      "python3 backend/ingestion/ingestion.py"
    ]
    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("grupox-key.pem")
      host        = self.public_ip
    }
  }
}


# EC2 Instances - Processing
resource "aws_instance" "processing" {
  ami                         = "ami-0ebfd941bbafe70c6"  # Updated Amazon Linux 2 AMI
  instance_type               = "t3.micro"
  key_name                    = "grupox-key"
  subnet_id                   = aws_subnet.grupox_subnet_public1_us_east_1a.id
  security_groups             = [aws_security_group.my_sg.id]
  associate_public_ip_address = true

  tags = {
    Name = "Processing-Instance"
  }

  # File provisioning to copy files directly into the EC2 instance
  provisioner "file" {
    source      = "../../src"
    destination = "/home/ec2-user/src"
    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("grupox-key.pem")
      host        = self.public_ip
    }
  }

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install -y python3 python3-pip", 
      # Verify that Python and pip were installed correctly
      "python3 --version", 
      "pip3 --version",
      "pip3 install boto3 kafka-python",
      # Add logging for troubleshooting
      "echo 'Navigating to src directory'",
      "cd /home/ec2-user/src",
      "echo 'Installing requirements'",
      "pip3 install -r requirements.txt",
      "echo 'Running processing script'",
      "python3 backend/processing/processing.py"
    ]
    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("grupox-key.pem")
      host        = self.public_ip
    }
  }
}


# EC2 Instances - Presentation
resource "aws_instance" "presentation" {
  ami                         = "ami-0ebfd941bbafe70c6"  # Updated Amazon Linux 2 AMI
  instance_type               = "t3.micro"
  key_name                    = "grupox-key"
  subnet_id                   = aws_subnet.grupox_subnet_public1_us_east_1a.id
  security_groups             = [aws_security_group.my_sg.id]
  associate_public_ip_address = true

  tags = {
    Name = "Presentation-Instance"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install -y python3 python3-pip",
      "pip3 install streamlit boto3"
    ]
    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("grupox-key.pem")
      host        = self.public_ip
    }
  }
}
