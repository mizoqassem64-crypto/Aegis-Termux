import os, sys, pyAesCrypt

def encrypt_folder(password, folder_path):
    bufferSize = 64 * 1024
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if not file.endswith(".aes"):
                path = os.path.join(root, file)
                pyAesCrypt.encryptFile(path, path + ".aes", password, bufferSize)
                os.remove(path)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        encrypt_folder(sys.argv[1], sys.argv[2])

