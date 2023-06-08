import subprocess


def run_docker_build():
    try:
        subprocess.run(
            ["docker", "build", "-t", "walmart-scrapi", "."], check=True)
        print("Docker build completed successfully.")
    except subprocess.CalledProcessError:
        print("Docker build failed.")


if __name__ == "__main__":
    run_docker_build()
