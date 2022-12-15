/* Función para la ventana modal, zoom y posicionamiento de las cámaras al hacer click sobre ellas */
document.addEventListener('DOMContentLoaded', () => {
    let videoContainer = document.getElementById('video-container');
    let cuadros = videoContainer.querySelectorAll('.cuadro');
    /* let btnCerrar = document.getElementById('cerrar'); */
    let video = document.getElementById('video');
    let modal = document.getElementById('myModal');
    
    cuadros.forEach(cuadro => {
        cuadro.addEventListener('click', (e) => {
            cuadro.classList.add('cuadro-expandir');
            /* btnCerrar.style.display = 'inline-block'; */

            switch (cuadro.id) {
                case 'cuadro0':
                    cuadros[1].style.display = 'none';
                    cuadros[2].style.display = 'none';
                    cuadros[3].style.display = 'none';
                    video.classList.remove('video');
                    video.classList.add('video-expandir');
                    videoContainer.classList.remove('video-container');
                    videoContainer.classList.add('video-container-expand');
                    video.style.top = '0';
                    video.style.left = '0';
                    modal.style.display = "block";
                    cuadros[0].src = this.src;
                    break;

                case 'cuadro1':
                    cuadros[0].style.display = 'none';
                    cuadros[2].style.display = 'none';
                    cuadros[3].style.display = 'none';
                    video.classList.remove('video');
                    video.classList.add('video-expandir');
                    videoContainer.classList.remove('video-container');
                    videoContainer.classList.add('video-container-expand');
                    video.style.top = '0';
                    video.style.right = '0';
                    modal.style.display = "block";
                    cuadros[1].src = this.src;
                    break;

                case 'cuadro2':
                    cuadros[0].style.display = 'none';
                    cuadros[1].style.display = 'none';
                    cuadros[3].style.display = 'none';
                    video.classList.remove('video');
                    video.classList.add('video-expandir');
                    videoContainer.classList.remove('video-container');
                    videoContainer.classList.add('video-container-expand');
                    video.style.bottom = '0';
                    video.style.left = '0';
                    modal.style.display = "block";
                    cuadros[2].src = this.src;
                    break;

                case 'cuadro3':
                    cuadros[0].style.display = 'none';
                    cuadros[1].style.display = 'none';
                    cuadros[2].style.display = 'none';
                    video.classList.remove('video');
                    video.classList.add('video-expandir');
                    videoContainer.classList.remove('video-container');
                    videoContainer.classList.add('video-container-expand');
                    video.style.bottom = '0';
                    video.style.right = '0';
                    modal.style.display = "block";
                    cuadros[3].src = this.src;
                    break;
            
                default:
                    break;
            }
        });
    });

    modal.addEventListener('click', () => {
        cuadros.forEach(cuadro => {
                cuadro.classList.remove('cuadro-expandir');
                cuadro.style.display = 'block';
                /* btnCerrar.style.display = 'none'; */
                modal.style.display = "none";
                videoContainer.classList.remove('video-container-expand');
                videoContainer.classList.add('video-container');
        });

        video.classList.add('video');
        video.classList.remove('video-expandir');
        video.style.top = 'inherit';
        video.style.bottom = 'inherit';
        video.style.left = 'inherit';
        video.style.right = 'inherit';
    });


});