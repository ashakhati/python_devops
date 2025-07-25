import docker

client = docker.from_env()
image_name = input("enter the docker image name")
client.images.pull(image_name)
print ("pulling the image")

container = client.containers.run(image_name,detach=True)
print("container is running")

