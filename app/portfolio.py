
from flask import ( Blueprint, render_template, request, redirect, url_for, current_app )
import sendgrid
from sendgrid.helpers.mail import *
from .constants import Constants

blue_print = Blueprint('portfolio', __name__, url_prefix='/')

@blue_print.route('/', methods=['GET','POST'])
def index():
    return render_template('portfolio/index.html', constants=Constants)

@blue_print.route('/mail', methods=['GET','POST'])
def mail():

    if request.method == 'POST':
        name = request.form.get('name')    
        email = request.form.get('email')
        message = request.form.get('message')

        send_email(name, email, message)
        return render_template('portfolio/sent_mail.html', constants=Constants)
    else:
        return redirect(url_for('portfolio.index')) 
        
def send_email(name, email, message):
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_API_KEY'])
    from_email = Email(current_app.config['SENDGRID_FROM_EMAIL'])
    to_email = To(current_app.config['SENDGRID_TO_EMAIL'], 
        substitutions={
            "-name-": name,
            "-email-": email,
            "-message-": message
        }
    )

    html_content = """
        <p>Hi Sebastian!, You have a message from your porfolio web contact form</p>
        <p>Nombre: -name-</p>
        <p>Email: -email-</p>
        <p>Message: -message-</p>
    """

    mail = Mail(from_email, to_email, 'New portfolio contact {}'.format(email), html_content=html_content)
    response = sg.client.mail.send.post(request_body=mail.get())

def test():
    print('test')