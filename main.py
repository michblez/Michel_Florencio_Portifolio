from flask import Flask, render_template, request, flash, redirect
from flask_mail import Mail, Message



app = Flask(__name__)
app.secret_key = 'mike'

mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


class Email:
  def __init__(self, nome, email, assunto, mensagem):
    self.nome = nome
    self.email = email
    self.assunto = assunto
    self.mensagem = mensagem

@app.route('/')
def home():
  return render_template('index.html')

app.route('/enviar', methods=['GET', 'POST'])
def enviar():
   if request.method == 'POST':
        formContato = Email(
            request.form["nome"],
            request.form["email"],
            request.form["assunto"],
            request.form["mensagem"]
        )

        msg = Message(
            subject = f'{formContato.assunto}, foi enviado através do portifolio por {formContato.nome}',
            sender = app.config.get("MAIL_USERNAME"),
            recipients = [app.config.get("MAIL_USERNAME")],
            body = f'''
            
            {formContato.nome} com o e-mail {formContato.email}, te enviou a seguinte 
            mensagem:


            {formContato.mensagem}


            '''
        )

        mail.send(msg)
        flash('Mensagem enviada com sucesso')
        return redirect('/')


if __name__ == '__main__':
  app.run(debug=True)