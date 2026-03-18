import subprocess

result = subprocess.run("dir", capture_output=True, text=True, shell=True)
print(f"Output:\n{result.stdout}")
print(f"Errors: {result.stderr}")
print(f"Return code: {result.returncode}")