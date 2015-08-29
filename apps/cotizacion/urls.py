from django.conf.urls import include, url
from .views import RegistrarCotizacion, cotizacionesTodas, aprobar, pendientes, MyPDFView, PdfView, aprobadas, vencidas, CotizacionInformal, Informal
from apps.estado.views import Confirmacion

urlpatterns = [

	url(r'^cotizacion/$', RegistrarCotizacion, name="cotizacion"),
	url(r'^informal/$', CotizacionInformal, name="informal"),
	url(r'^cotizaciones/$', cotizacionesTodas, name="cotizaciones"),
	url(r'^aprobaciones/(?P<cotizacion_id>.*)/$', aprobar, name="aprobaciones"),
	url(r'^confirma/$', Confirmacion.as_view(), name="confirma"),
	url(r'^pdfView/$', PdfView.as_view(), name="pdfView"),
	url(r'^cotizaciones/pendientes/$', pendientes, name="pdfP"),
	url(r'^cotizaciones/aprobadas/$', aprobadas, name="pdfA"),
	url(r'^cotizaciones/vencidas/$', vencidas, name="pdfV"),
	url(r'^pdfs/(?P<pk>.*)/$', MyPDFView.as_view(), name="pdfs"),
	url(r'^pdfInformal/(?P<pk>.*)/$', Informal.as_view(), name="pdfInformal"),
]