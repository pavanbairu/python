
import sys
instance_type = sys.argv[1]

if instance_type == "t2.micro":
    print("instance will be with 1GB of storage")
elif instance_type == "t3.micro":
    print("instance will be created with 1.5GB of storage")
elif instance_type == "t3.small":
    print("instance type will be created with 2 GB of storage")
elif instance_type == "t3.medium":
    print("instance will be created with 2.5GB of storage")
elif instance_type == "t3.large":
    print("instance will be created with 3GB of storage")
else:
    print("Please provide the valid instance type")
