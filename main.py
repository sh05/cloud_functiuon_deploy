import os
import functions_framework
from flask import escape
from google.cloud import storage
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

BUCKET_NAME = 'generated_pdf'
KEY_FILEPATH = 'eng-spot-333112-af0008ed541a.json'
PDF_NAME = 'sample'


def upload2cloud(filename=PDF_NAME+'.pdf'):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = KEY_FILEPATH
    client = storage.Client()
    bucket = client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)


def generate_pdf(filename=PDF_NAME):
    pdf_canvas = set_info(filename)
    print_string(pdf_canvas)
    pdf_canvas.save()


def set_info(filename):
    pdf_canvas = canvas.Canvas("./{0}.pdf".format(filename))
    pdf_canvas.setAuthor("")
    pdf_canvas.setTitle("")
    pdf_canvas.setSubject("")
    return pdf_canvas


def print_string(pdf_canvas):
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
    width, height = A4
    font_size = 24
    pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
    pdf_canvas.drawString(60, 770, 'サンプル')


@functions_framework.http
def sample(request):
    generate_pdf()
    upload2cloud()

    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(escape(name))
