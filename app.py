import os
from flask import Flask, request, jsonify, render_template, send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

from testing import disease
@app.route('/',methods=['GET','POST'])
def hello_world():
	if request.method=='GET':
		return render_template('index.html')
	if request.method=='POST':
		try:
			file=request.files['file']
			filename = file.filename
			filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
			file.save(filepath)
			# image=file.read()
			# print(file.filename)
			# disease_name = "Pneumonia"
			disease_name = disease(file.filename)
			# disease_name=get_disease_name(image_bytes=image)
			return render_template('result.html',dis=disease_name,image_url = filename)	
		except:
			return render_template('index.html')
		
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
	app.run(debug=True,port=os.getenv('PORT',5000))
	