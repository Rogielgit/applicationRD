import os
from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
   
    a = 5;
    b = 6
   return print a + b
"""

    return "<html><script>function enviaMensagem()\
{\
 \
 var texto = document.getElementById('chat_client').value;\
 document.getElementById('chat_princ').value = texto;}\
</script>\
<body>\
<center>\
    <h1>Chat HelloMyFriends </h1>\
</center>\
<textarea  id ='chat_princ' name = 'chat' rows='20' cols='100'>\
Inicio do Chat .....\
</textarea>\
<textarea id ='chat_client' name = 'text-cliente' rows='10' cols='30'>\
</textarea>\
<input type='button' name='botao-ok' value='send txt' onclick = 'enviaMensagem()'> </input>\
</body>\
</html>\
"
"""
    
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
