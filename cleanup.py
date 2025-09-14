# cleanup.py
import os, time, shutil

UPLOAD_FOLDER = '/var/data/uploads'
OUTPUT_FOLDER = '/var/data/output'
EXPIRE_SECONDS = 60  # 1分

def cleanup(folder):
    now = time.time()
    for root, dirs, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            try:
                if os.path.getctime(path) < now - EXPIRE_SECONDS:
                    os.remove(path)
                    print(f"削除: {path}")
            except Exception as e:
                print(f"削除エラー {path}: {e}")
        for name in dirs:
            path = os.path.join(root, name)
            try:
                if os.path.getmtime(path) < now - EXPIRE_SECONDS:
                    shutil.rmtree(path)
                    print(f"削除: {path}")
            except Exception as e:
                print(f"削除エラー {path}: {e}")

if __name__ == "__main__":
    cleanup(UPLOAD_FOLDER)
    cleanup(OUTPUT_FOLDER)