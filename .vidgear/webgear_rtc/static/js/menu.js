/* Función para expandir y contraer el dashboard */
$(document).ready(function(){

    const btnToggle = document.querySelector('.toggle-btn');
    let sidebar = document.getElementById('sidebar');

    btnToggle.addEventListener('click', function(){ 
       document.getElementById('sidebar').classList.toggle('active');
       document.getElementById('header_side').classList.toggle('active');
       document.getElementById('pContainer').classList.toggle('active');
       document.getElementById('video-container').classList.toggle('active');
    
    });
       
   window.addEventListener("resize", function(){
        if(screen.width < 991){
            document.getElementById('header_side').classList.remove('active');
            document.getElementById('pContainer').classList.remove('active');
        }
        if(screen.width >= 991 && (sidebar.classList.contains('active')) == true){
            document.getElementById('header_side').classList.add('active');
            document.getElementById('pContainer').classList.add('active');
        }
        if(screen.width < 1000){
            document.getElementById('video-container').classList.remove('active');
        }
   });
});

