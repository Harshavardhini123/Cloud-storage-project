from flask import Flask, request, render_template_string
import boto3

app = Flask(__name__)

AWS_ACCESS_KEY = "AWSACCESSKEYID"
AWS_SECRET_KEY = "AWSSECRETKEYID"
BUCKET_NAME = "smart-file-storage1-harsha"

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name="ap-south-1"
)

UPLOAD_PAGE = '''
<h2>☁️ Harsha's Smart File Storage</h2>
<form action="/upload" method="post" enctype="multipart/form-data">
  <input type="file" name="file"><br><br>
  <input type="submit" value="Upload">
</form>
'''

@app.route("/")
def home():
    return render_template_string(UPLOAD_PAGE)

@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        file = request.files["file"]
        s3.upload_fileobj(file, BUCKET_NAME, file.filename)
        file_url = f"https://{BUCKET_NAME}.s3.ap-south-1.amazonaws.com/{file.filename}"
        return f"<h3>Uploaded successfully!</h3><a href='{file_url}' target='_blank'>{file_url}</a>"
    except Exception as e:
        return f"<h3 style='color:red;'>
         Error:</h3><pre>{str(e)}</pre>"

if __name__ == "__main__":
    app.run(debug=True)