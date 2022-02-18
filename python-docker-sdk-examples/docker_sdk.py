import docker
__all__ = (
        'run',
        'stop',
        'kill',
        'remove_image',
        'load',
        'close',
        )

try:
    import docker

    _client = docker.from_env()
except Exception as e:
        print("Please check if docker sdk installed")
        raise Exception from e



def run(image, run_opts=None):
    """
    Run a docker application.

    :param image:
        Image ID to be passed directly to docker sdk

    :param run_opts:
        Docker run options as a string

    """
    try:
        return _client.containers.run(image,
                                   detach=True,
                                   **kwargs)
    except Exception as e:
        raise Exception from e

def create(image, opts=None):
    """
    Run a docker application.

    :param image:
        Image ID to be passed directly to docker sdk

    :param opts:
        Docker create options as a string

    """
    try:
        return _client.containers.create(image)
    except Exception as e:
        raise Exception from e

def start(container):
    """
    Start a docker container.

    :param container:
        Container ID to be passed directly to docker sdk

    """
    try:
        container = _client.containers.get(container_id)
        container.start(**kwargs)

    except Exception as e:
        raise Exception from e

def update(container, **kwargs):
    """
    Run a docker application.

    :param container_id:
        Container ID or name to be passed directly to docker sdk

    :param **kwargs:
        This arg is TBD

    """

    try:
        container = _client.containers.get(container_id)
        container.update(**kwargs)

    except docker.errors.APIError as e:
        raise Exception from e


def stop(container):
    """
    Lookup a container by id (or name) and stop it.

    The caller can use the underlying stop method if it already
    has a reference to the container object.

    :param container_id:
        Container ID or name to be passed directly to docker sdk

    """
    try:
        container = _client.containers.get(container_id)
        container.stop()

    except docker.errors.APIError as e:
        raise Exception from e

def kill(container_id, **kwargs):
    """
    Lookup a container by id (or name) and kill it.

    The caller can use the underlying kill method if it already
    has a reference to the container object.

    :param container:
        Container ID or name to be passed directly to docker sdk

    :param **kwargs:
        This is meant so the caller than pass kwargs directly to
        docker sdk. Not sure if needed though.

    """


    try:
        container = _client.containers.get(container)
        container.stop()
    except docker.errors.APIError as e:
        raise Exception from e

def download(command, cwd):
    """
    Download a docker .tar file given a curl or wget command string,
    execute the command and make sure the file is valid.

    :param command:
        Container ID or name to be passed directly to docker sdk.

    :param cwd:
        Location to download file to.

    """


    _cmd = shlex.split(cmd)
    proc = subprocess.run(_cmd,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          cwd=cwd)

    print('[{!r} exited with {}]'.format(cmd, proc.returncode))
    if proc.stdout:
        print('[stdout]\n{}'.format(proc.stdout.decode()))
    if proc.stderr:
        print('[stderr]\n{}'.format(proc.stderr.decode()))

    if proc.returncode:
        # TODO add proper cisco exception
        raise Exception('[{!r} exited with {}]'.format(cmd, proc.returncode))


def load(image_file):
    """
    Load a docker image
    """


    with open(image_file, 'rb') as f:
        image_data = f.read()

    try:
        image = _client.images.load(image_data)
    except docker.errors.APIError as e:
        raise Exception from e

    return image

def remove_container(container):
    """
    Remove a container

    The caller can use the underlying remove method if it already
    has a reference to the container object.

    :param container:
        Container ID or name to be passed directly to docker sdk

    :param **kwargs:
        This is meant so the caller than pass kwargs directly to
        docker sdk. Not sure if needed though.

    """


    try:
        container = _client.containers.get(container_id)
        container.remove(v=True, # remove volumes
                         link=False, # remove underlying container
                         force=False)

    except docker.errors.APIError as e:
        raise Exception from e

def remove_image(image_id):
    """
    Remove an image

    :param image_id:
        Image ID to be passed directly to docker sdk
    """


    try:
        _client.images.remove(image_id,
                             force=False,
                             noprune=False)
    except docker.errors.APIError as e:
        raise Exception from e

def get_logs(container):
    """
    Get logs corresponding to a docker container

    :param container:
        Container ID or name to be passed directly to docker sdk

    """


    pass

def get_stats(container):
    """
    Get stats of a container

    :param container:
        Container ID or name to be passed directly to docker sdk

    """


    pass

def close():
    """
    Close docker client session
    """
    _client.close()    

def main():
    try:
       _client.images.pull("ubuntu")
       print("Image pulled")
    except docker.errors.ImageNotFound:
       print("Image not Found")
    container = _client.containers.run("ubuntu",["sh"], detach=True,stdin_open=True,tty=True)
    print("Image Running")
    container.exec_run("touch myfile.txt",stdout=True,stream=True);
    container.commit(repository="myubuntu" ,tag="1.0")
    _client.containers.run("myubuntu:1.0",["sh"], detach=True,stdin_open=True,tty=True)

if __name__ == '__main__':
    main()
    close()
