// function detectar_fecha_actual () {
//     let fechaInicial = document.getElementById('fecha_inicial');
//     let fechaFinal = document.getElementById('fecha_final');
//     let fecha = new Date();
  
//     fecha_actual = fecha.toLocaleDateString().split('/').reverse()
//     fecha_actual[1] = fecha_actual[1] <= 9 ? (0 + fecha_actual[1]) : fecha_actual[1]
//     fecha_actual[2] = fecha_actual[2] <= 9 ? (0 + fecha_actual[2]) : fecha_actual[2]
    
//     fechaInicial.setAttribute('max', fecha_actual.join('-'));
//     fechaFinal.setAttribute('max', fecha_actual.join('-'));

//     fechaInicial.setAttribute('value', fecha_actual.join('-'));
//     fechaFinal.setAttribute('value',  fecha_actual.join('-'));
// }


document.addEventListener('DOMContentLoaded', e => {

    let rangeContainer = document.getElementById('rangeContainer');
    let mesContainer = document.getElementById('mesContainer');
    let checkForm = document.getElementById('flexSwitchCheckChecked');
    mesContainer.style.display = 'none';
    
    checkForm.addEventListener('click', () => {
        if (checkForm.checked) {
            rangeContainer.style.display = 'block';
            mesContainer.style.display = 'none';
            checkForm.title = 'FILTRAR POR AÑO Y MES';
        }
        else{
            rangeContainer.style.display = 'none';
            mesContainer.style.display = 'block';
            checkForm.title = 'FILTRAR POR RANGO DE FECHAS';
        }
    });

    // detectar_fecha_actual();
    // let fechaInicial = document.getElementById('fecha_inicial');
    // let fechaFinal = document.getElementById('fecha_final');
    // fechaFinal.addEventListener('click', e => {
    //     fechaFinal.setAttribute('min', fechaInicial.value);
    //     fechaInicial.setAttribute('max', fechaFinal.value);
    // });
    // fechaInicial.addEventListener('click', e => {
    //     fechaInicial.setAttribute('max', fechaFinal.value);
    //     fechaFinal.setAttribute('min', fechaInicial.value);
    // });

    let player = videojs('video2', {
        autoplay: false,
        controls: true,
        playbackRates: [0.25, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4],
    });

    var tooltipElement = document.getElementById('flexSwitchCheckChecked');
    var tooltip = new bootstrap.Tooltip(tooltipElement);
    
    let container = document.getElementById('container2');
    let videoModal = document.getElementById('videoModal');
    let video = document.getElementById('video2');

    anchor = Array.from(container.querySelectorAll('.btn-video'));
        for (let i = 0; i < anchor.length; i++) {
            anchor[i].addEventListener('click', (e) => {
                e.preventDefault();

                let src = anchor[i].href;
                
                video.src = src;
                video.children[0].src = src;

                console.log(video.src, video.children[0].src);
            });
        }

    videoModal.addEventListener('hidden.bs.modal', () => {
        video.src = '#';
        video.children[0].src = '#';
    })


});