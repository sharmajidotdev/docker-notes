
### 1. **docker run**
**Explanation**: This command is used to create and start a container from an image.

```bash
docker run -d --name mynginx -p 8080:80 nginx
```
- **Explanation**: 
  - `-d` runs the container in detached mode.
  - `--name` assigns a custom name (`mynginx`).
  - `-p` maps port `8080` on the host to port `80` inside the container.
  - `nginx` is the image from which the container is created.

---

### 2. **docker ps**
**Explanation**: This command shows the list of running containers.

```bash
docker ps
```
- **Explanation**: Displays information about all containers that are currently running, including the container ID, names, and port mappings.

---

### 3. **docker exec**
**Explanation**: This command is used to execute a command inside a running container.

```bash
docker exec -it mynginx bash
```
- **Explanation**: 
  - `-it` allows interactive mode and attaches to the container.
  - `bash` opens a bash shell inside the container (`mynginx`).

---

### 4. **docker stop**
**Explanation**: Stops a running container.

```bash
docker stop mynginx
```
- **Explanation**: Stops the `mynginx` container gracefully.

---

### 5. **docker start**
**Explanation**: Starts a previously stopped container.

```bash
docker start mynginx
```
- **Explanation**: Restarts the stopped container (`mynginx`).

---

### 6. **docker restart**
**Explanation**: This command restarts a running container.

```bash
docker restart mynginx
```
- **Explanation**: The `mynginx` container will be stopped and started again.

---

### 7. **docker logs**
**Explanation**: Fetches logs from a container.

```bash
docker logs mynginx
```
- **Explanation**: Retrieves the logs of the `mynginx` container, useful for debugging or viewing container output.

---

### 8. **docker inspect**
**Explanation**: Provides detailed information about a container or image, such as environment variables, mounts, etc.

```bash
docker inspect mynginx
```
- **Explanation**: Returns a JSON output with detailed information about the `mynginx` container.

---

### 9. **docker attach**
**Explanation**: Attaches to a running container's main process.

```bash
docker attach mynginx
```
- **Explanation**: Attaches to the `mynginx` container’s standard input/output. This will let you interact with the container's main process directly.

---

### 10. **docker cp**
**Explanation**: Copies files between containers and the host.

```bash
docker cp mynginx:/usr/share/nginx/html /tmp/nginx_files
```
- **Explanation**: 
  - This copies the `/usr/share/nginx/html` directory from the `mynginx` container to `/tmp/nginx_files` on the host.

---

### 11. **docker rm**
**Explanation**: Removes a stopped container.

```bash
docker rm mynginx
```
- **Explanation**: Removes the stopped container `mynginx` from the system.

---
