/* Script para Confirmar las 2 contraseñas */
$(document).ready(function() {
	//Variables
	var pass1 = $('[name=password]');
	var pass2 = $('[name=confirm_password]');
	var confirmacion = "Las Contraseñas Si Coinciden";
	var negacion = "No Coinciden las Contraseñas";
	var enviar = document.getElementById('btnAct')
	
	//Oculto por defecto el elemento span
	var span = $('<span></span>').insertAfter(pass2);
	span.hide();
	//Función que comprueba las dos contraseñas
	function coincidePassword(){
	var valor1 = pass1.val();
	var valor2 = pass2.val();
	//Muestro el span
	span.show().removeClass();
	//Condiciones dentro de la función
	if(valor1 != valor2){
	span.text(negacion).addClass('negacion');
	enviar.disabled = true;	
	}
	if(valor1.length!=0 && valor1==valor2){
	span.text(confirmacion).removeClass("negacion").addClass('confirmacion');
	enviar.disabled = false;
	}
	}
	//Ejecuto la función al soltar la tecla
	pass2.keyup(function(){
	coincidePassword();
	});
});