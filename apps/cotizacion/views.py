# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from forms import CotizacionForm, AprobacionForm, InformalForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template import RequestContext
from apps.receta.models import Detalle
from apps.receta.models import Receta
from .models import Cotizacion
from wkhtmltopdf.views import PDFTemplateResponse


@login_required
def RegistrarCotizacion(request):

	receta = Detalle.objects.all()
	if request.method == 'POST':
		form = CotizacionForm(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/localidad/confirma/')

	else:
		form = CotizacionForm()

	return render_to_response('negocio/cotizacion.html',{'form':form, 'recetas': receta},
		context_instance=RequestContext(request))

@login_required
def CotizacionInformal(request):
    if request.method == 'POST':
        form = InformalForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/localidad/confirma/')

    else:
        form = InformalForm()

    return render_to_response('negocio/informales.html',{'form':form},
        context_instance=RequestContext(request))

@login_required
def cotizacionesTodas(request):

	cotizaciones = Cotizacion.objects.all()

	ctx = {'cotizaciones': cotizaciones}
	return render_to_response('negocio/cotizaciones.html',ctx,context_instance=RequestContext(request))

@login_required
def aprobar(request,cotizacion_id):

	cotizacion = Cotizacion.objects.get(pk=cotizacion_id)
	if request.method == 'POST':
		form = AprobacionForm(request.POST,instance=cotizacion)
		if form.is_valid():
			edit_cot = form.save(commit=False)
			edit_cot.status = True
			form.save()

			return HttpResponseRedirect('/localidad/confirma/')

	else:
		form = AprobacionForm(instance=cotizacion)
		
	ctx = {'form': form}
	return render_to_response('negocio/aprobaciones.html',ctx,
		context_instance=RequestContext(request))

# Generar pdfs

from io import BytesIO
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table

class PdfView(ListView):
    template_name = 'negocio/pdf.html'
    model = Cotizacion
    context_object_name = 'cot'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
    	return super(PdfView, self).dispatch(*args, **kwargs)



def pendientes(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "cotizacion.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=20,
                            leftMargin=20,
                            topMargin=30,
                            bottomMargin=18,
                            )
    cotizacion = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Cotizaciones", styles['Heading1'])
    cotizacion.append(header)
    headings = ('Fecha de elaboracion','Nombre del cliente','Telefono', 'Total','Fecha de vencimiento','Estado')
    allcotizaciones = [(p.fechaInicial, p.cliente, p.cliente.telefono, p.total, p.fechaFinal, p.estado) for p in Cotizacion.objects.filter(estado='Pendiente')]
    print allcotizaciones

    t = Table([headings] + allcotizaciones)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (5, -1), 1, colors.darkgray),
            ('TEXTCOLOR',(4,1),(-1,-1),colors.green),
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.darkgray),
            ('BOX',(4,1),(-1,-1),2,colors.red),
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkgrey)
        ]
    ))
    cotizacion.append(t)
    doc.build(cotizacion)
    response.write(buff.getvalue())
    buff.close()
    return response

def aprobadas(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "cotizacion.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=20,
                            leftMargin=20,
                            topMargin=30,
                            bottomMargin=18,
                            )
    cotizacion = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Cotizaciones", styles['Heading1'])
    cotizacion.append(header)
    headings = ('Fecha de elaboracion','Nombre del cliente','Telefono', 'Total','Fecha de vencimiento','Estado')
    allcotizaciones = [(p.fechaInicial, p.cliente, p.cliente.telefono, p.total, p.fechaFinal, p.estado) for p in Cotizacion.objects.filter(estado='Aprobado')]
    print allcotizaciones

    t = Table([headings] + allcotizaciones)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (5, -1), 1, colors.darkgray),
            ('TEXTCOLOR',(4,1),(-1,-1),colors.green),
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.darkgray),
            ('BOX',(4,1),(-1,-1),2,colors.red),
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkgrey)
        ]
    ))
    cotizacion.append(t)
    doc.build(cotizacion)
    response.write(buff.getvalue())
    buff.close()
    return response

def vencidas(request):
    print "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "cotizacion.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=20,
                            leftMargin=20,
                            topMargin=30,
                            bottomMargin=18,
                            )
    cotizacion = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Cotizaciones", styles['Heading1'])
    cotizacion.append(header)
    headings = ('Fecha de elaboracion','Nombre del cliente','Telefono', 'Total','Fecha de vencimiento','Estado')
    allcotizaciones = [(p.fechaInicial, p.cliente, p.cliente.telefono, p.total, p.fechaFinal, p.estado) for p in Cotizacion.objects.filter(estado='Vencido')]
    print allcotizaciones

    t = Table([headings] + allcotizaciones)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (5, -1), 1, colors.darkgray),
            ('TEXTCOLOR',(4,1),(-1,-1),colors.green),
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.darkgray),
            ('BOX',(4,1),(-1,-1),2,colors.red),
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkgrey)
        ]
    ))
    cotizacion.append(t)
    doc.build(cotizacion)
    response.write(buff.getvalue())
    buff.close()
    return response

class MyPDFView(DetailView):
    template='negocio/my_template.html'    
    context= {'Saludo': 'Estimad@!'}
    model = Cotizacion

    def get(self, request, *args, **kwargs):    

        self.context['c'] = self.get_object()

        response=PDFTemplateResponse(request=request,
                                     template=self.template,
                                     filename ="cotizacion.pdf",
                                     context=self.context,
                                     show_content_in_browser=True,
                                     cmd_options={'margin-top': 20,}
                                     )
        return response

class Informal(DetailView):
    template='negocio/pdfInformal.html'    
    context= {'Saludo': 'Estimad@!'}
    model = Cotizacion

    def get(self, request, *args, **kwargs):    

        self.context['c'] = self.get_object()

        response=PDFTemplateResponse(request=request,
                                     template=self.template,
                                     filename = "cotizacion.pdf",
                                     context=self.context,
                                     show_content_in_browser=True,
                                     cmd_options={'margin-top': 20,}
                                     )

        return response

# def Informal(request,pk):
#     cotizacion = Cotizacion.objects.get(pk=pk)
#     t = loader.get_template('negocio/pdfInformal.html')
#     c = RequestContext(request, {'Saludo': 'Estimad@!','cotizacion': cotizacion})
#     html = t.render(c)
#     pdf_data = html2pdf(html) # Your favorite html2pdf generator
#     response = HttpResponse(pdf_data, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="cotizacion.pdf"'
#     return response


# 
# import ho.pisa as pisa
# import cStringIO as StringIO
# import cgi
# from django.template.loader import render_to_string
# from django.shortcuts import get_object_or_404

# def generar_pdf(html):
#     # Funcion para generar el archivo PDF y devolverlo mediante HttpResponse
#     result = StringIO.StringIO()
#     pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), mimetype='application/pdf')
#     return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))

# def MyPDFView(request, pk):
#     # vista de ejemplo con un hipotetico modelo Libro
#     cotizacion=get_object_or_404(Cotizacion,pk=pk)
#     html = render_to_string('negocio/my_template.html', {'pagesize':'A4','cotizacion':cotizacion}, context_instance=RequestContext(request))
#     return generar_pdf(html)
