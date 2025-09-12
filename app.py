from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/api/analyze", methods=["POST"])
def analyze():
    f = request.files.get("video")
    if not f:
        return jsonify({"success": False, "error": "動画ファイルがありません"}), 400
    return jsonify({
        "success": True,
        "message": f"動画 {f.filename} を受け取りました（ダミー解析）",
        "result": {"score": 50, "advice": "次は本番の解析を追加しましょう"}
    })
