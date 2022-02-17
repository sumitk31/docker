import docker
client = docker.from_env()
try:
  streamer = client.images.pull("alpine")
  print("Image pulled")
except docker.errors.ImageNotFound:
  print("Image not Found")

container = client.containers.run("alpine",["sh"], detach=True,stdin_open=True,tty=True)
print("Image Running")
container.exec_run("touch myfile.txt",stdout=True,stream=True);
container.commit(repository="myalpine" ,tag="1.0")
client.containers.run("myalpine:1.0",["sh"], detach=True,stdin_open=True,tty=True)

