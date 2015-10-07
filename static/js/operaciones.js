//Sacar costo por ingrediente

function Calcular()
{
	var cantidad = document.getElementById('id_cantidad').value;
	var costo = document.getElementById('costo').value;

	if (isNaN(parseFloat(document.getElementById('id_cantidad').value))){
		alert("Indique un número en cantidad");
        document.getElementById('id_cantidad').innerText = "0";
        document.getElementById('id_cantidad').focus();
        }else{
        	var total = ((costo/1000)*cantidad).toFixed(2);
        	document.getElementById('id_valor').value=total;
        };
	}
//Sacar datos de cotizacion

function Totalizar()
{
	var valor = document.getElementById('suma').value;
	var personas = document.getElementById('id_personas').value;
	var extra = document.getElementById('id_extra').value;
	if (isNaN(parseFloat(document.getElementById('id_personas').value))) {
		alert("Indique un número de personas");
        document.getElementById('id_personas').innerText = "0";
        document.getElementById('id_personas').focus();
        }else if (isNaN(parseFloat(document.getElementById('id_extra').value))) {
        	alert("Indique valor extra o cero");
        	document.getElementById('id_extra').innerText = "0";
        	document.getElementById('id_extra').focus();
        	}else{
        		var vAgregado = (parseFloat(valor) / 0.25).toFixed(2);
				// var va = (((vAgregado/valor)-1)*100).toFixed(2);
				var total = (parseFloat(extra)+(parseInt(personas) * vAgregado)).toFixed(2);
				// document.getElementById('id_valor').value=va;
				document.getElementById('id_venta').value=vAgregado;
				document.getElementById('id_total').value=total;
        	};
}

//Sacar precio venta de la receta

function Venta()
{
	var costo = document.getElementById('id_costo').toFixed(2).value;
	var total = (costo/0.25).toFixed(2);
	document.getElementById('id_venta').value=total;
}

//Manejador de tablas

$(document).ready(function() {
        $('#dataTables-example').DataTable({
                responsive: true
        });
    });

//Sumar costos de los ingredientes de la receta para cotizacion
$(document).ready(function() {
		$("#addAll").click(function() {
			var add = 0;
			$(".costos").each(function() {
				add += Number($(this).val());
			});
			$("#suma").val(add);
		});
	});

//Sumar costos de los ingredientes para la receta

$(document).ready(function() {
		$("#sumar").click(function() {
			var add = 0;
			$(".costos").each(function() {
				add += Number($(this).val());
			});
			$("#id_costo").val(add);
		});
	});


