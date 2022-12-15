$(function() {

  // Fechas de iniciales calculadas con la libreria momentJS
  var start = moment();
  var end = moment();
  let cualitativeTime = 'Hoy';
 
  // Funcion para dar valor a cualitativeTime
  function timeC(diff) {
    switch (diff) {
      case 0:
        return 'Hoy';
        break;
      case 1:
        return 'Ayer';
        break;
      case 6: 
        return 'Hace 7 Días';
        break;
      case 29:
        return 'Hace 30 Días';
        break;
      default:
        return `Hace ${diff} Días`;
        break;
    }
  }

  function cb(start, end) {
    // Lista de rangos (Hoy, Ayer, Hace 7 dias, etc...)
    let ranges = document.querySelector(".ranges ul");

    // Se delega el evento y se asigna el valor de su textContent a cualitativeTime
    ranges.addEventListener('click', (e) => {
      cualitativeTime = e.target.textContent;
    });

    // Se escribe el rango en pantalla para el usuario
    $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY') + ' <b>(' + cualitativeTime + ')</b>');

    // Se guarda el rango (fecha inicial y fecha final) en sus respectivos inputs
    $('#dateStart').attr("value", start.format('YYYY-MM-DD'));
    $('#dateEnd').attr("value", end.format('YYYY-MM-DD'));
  }

  // inicailizacion de la libreria DateRangePicker con las opciones y configuraciones requeridas
  $('#reportrange').daterangepicker({
      startDate: start,
      endDate: end,
      "applyButtonClasses": "btn-success",
      "cancelButtonClasses": "btn-danger",
      locale: {
        cancelLabel: 'Cancelar',
        applyLabel: 'Aplicar',
        customRangeLabel: 'Personalizar Rango'
      },

      ranges: {
         'Hoy': [moment(), moment()],
         'Ayer': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
         'Hace 7 Días': [moment().subtract(6, 'days'), moment()],
         'Hace 30 Días': [moment().subtract(29, 'days'), moment()],
         'Este Mes': [moment().startOf('month'), moment()],
         'Mes Pasado': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
      }
      
  }, cb);

  cb(start, end);

});