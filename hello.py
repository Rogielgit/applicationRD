import os
from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "<html><head>\
<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />\
<meta http-equiv='Content-Script-Type' content='text/javascript'>\
<title>Endereços randomicos</title>\
<script type='text/javascript'>\
var v = new Array('http://www.uol.com.br','http://www.hardware.com.br/','http://www.google.com');\
function random_element(a)\
{\
 var novo_endereco;\
 var i\
 novo_endereco=a[Math.floor(Math.random() * a.length)];\
// O for abaixo é uma forma padrão de atribuir um endereço a um link nomeado\
// Uma forma mais simples de fazer isso seria\
 for (i=0; i<document.anchors.length; i++)\
{\
  if (document.anchors[i].name=='endereco_variavel')\
  {\
   document.anchors[i].href=novo_endereco;\
  }\
}\
 return novo_endereco\
}\
</script>\
</head>\
 <body>\
        <center>\
        <h1>Tô No Tédio</h1>\
                <center>\
        <div>\
            <input type='button' value='Clique para obter um endereço randômico' onclick='window.open(random_element(v));'\ name='endereco_variavel'>\
        </div>\
</body>\
</html>"

    
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
