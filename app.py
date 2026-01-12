from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
FLAG_FILE = "flag.txt"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def upload():
    html = """
<!DOCTYPE html>
<html>
<head>
<title>CTF File Upload</title>
<style>
body { background:#111; color:#fff; font-family:Arial; text-align:center; padding-top:60px; }
.container { width:400px; margin:auto; background:#1e1e1e; padding:20px; border-radius:8px; }
button { padding:10px 20px; background:#00bcd4; border:none; border-radius:5px; }
</style>
</head>
<body>
<div class="container">
<h2>Upload Profile Picture</h2>
<p>Only JPG/PNG allowed</p>
<form method="POST" enctype="multipart/form-data">
<input type="file" name="file" required><br><br>
<button type="submit">Upload</button>
</form>
</div>
</body>
</html>
"""

    if request.method == "POST":
        file = request.files.get("file")
        if not file:
            return "No file uploaded"

        filename = file.filename
        mimetype = file.mimetype

        save_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(save_path)

        response = f"""
        <h2>Upload Successful</h2>
        <p>Filename: {filename}</p>
        <p>MIME Type: {mimetype}</p>
        """

        if ".py" in filename or ".php" in filename:
            with open(FLAG_FILE) as f:
                flag = f.read()
            response += f"<pre>{flag}</pre>"
        else:
            response += "<p> FILE WAS UPLOADED SUCCESFULLY</p>"

        return response

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
