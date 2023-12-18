from flask import Flask, render_template,flash,redirect,url_for,abort,request
import uuid
import os
import convertapi








app = Flask (__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config.from_object ('config')

api = convertapi.api_secret = '634340627'

TIPOS_DISPONIVEIS = set (['png', 'jpg', 'jpeg', 'gif', 'pdf', 'xlsx', 'aac', 'mp3','Xlsx'])



def arquivos_permitidos (filename):
    return '.' in filename and filename.rsplit ('.',1)[1].lower () in TIPOS_DISPONIVEIS


@app.route ('/upload')
def home ():
    return render_template('upload.html')

@app.route ('/upload', methods = ["POST"])
def upload_image ():
    file = request.files ["file"]
    if file.filename == '':
        flash("Nenhum arquivo selecionado")
        return redirect(request.url)
    if not arquivos_permitidos(file.filename):
        flash("Utilize os tipos de arquivos permitidos")
        abort (401)
        
    filename = str (uuid.uuid4())
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    flash("Arquivo enviado com sucesso!")
    return render_template('upload.html', filename=filename)

@app.route ('/display/<filename>')
def display_image (filename):
    return redirect(url_for('static', filename = 'uploads/' + filename), code = 301)


# result = convertapi.convert ('pdf', {'File'}: '')
# result.file.save ('')




if __name__ == '__main__':
    app.run(host= '10.3.149.105' , port=443)
