#!/usr/bin/env python3
import os
from datetime import datetime

# Define the column headers for the table
print('{:<40}{:<30}{:<20}'.format("DEPLOYMENT NAME", "IMAGE", "UPDATED AT"))

# Use kubectl to get a list of deployments and their details
stream = os.popen('kubectl get deployments --all-namespaces -o custom-columns="NAME:.metadata.name,IMAGE:.spec.template.spec.containers[0].image,UPDATED_AT:.metadata.creationTimestamp"')
deployments = stream.read().splitlines()[1:]
for deployment in deployments:
    # Split each line by whitespace and extract the deployment name, image, and timestamp
    deployment = deployment.split()
    name = deployment[0]
    image = deployment[1]
    timestamp = deployment[2]
    
    # Format the timestamp in a more readable format
    updated_at = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')

    # Print the deployment details as a formatted table row
    print('{:<40}{:<30}{:<20}'.format(name, image, updated_at))
