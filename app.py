import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# 保存フォルダを永続ディスクに
UPLOAD_FOLDER = '/var/data/uploads'
OUTPUT_FOLDER = '/var/data/output'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/api/analyze", methods=["POST"])
def analyze():
    f = request.files.get("video")
    if not f:
        return jsonify({"success": False, "error": "動画ファイルがありません"}), 400
    
    save_path = os.path.join(UPLOAD_FOLDER, f.filename)
    f.save(save_path)

    return jsonify({
        "success": True,
        "message": f"動画 {f.filename} を受け取り、 {save_path} に保存しました（ダミー解析）",
        "result": {"score": 50, "advice": "次は本番の解析を追加しましょう"}
    })advice": "次は本番の解析を追加しましょう"}
    })
    
@app.route("/api/list_output", methods=["GET"])
def list_output():
    files = []
    for root, dirs, filenames in os.walk(OUTPUT_FOLDER):
        for name in filenames:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            files.append({
                "name": name,
                "size": size,
                "path": os.path.relpath(path, OUTPUT_FOLDER)
            })
    return jsonify({"files": files})

@app.route("/api/list_uploads", methods=["GET"])
def list_uploads():
    try:
        files = os.listdir(UPLOAD_FOLDER)
        return jsonify({"files": files})
    except Exception as e:
        return jsonify({"error": str(e)})
