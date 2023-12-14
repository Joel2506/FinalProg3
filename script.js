/*alert("cargando");*/







//Generando CV

function generarCV() {
    //console.log("generando cv"); 


    
    
    //validar campos
    const nombre = document.getElementById('nameField').value;
    const correo = document.getElementById('mailField').value;
    const telefono = document.getElementById('contactField').value;
    const idioma = document.getElementById('langField').value;
    const direccion = document.getElementById('addressField').value;
    const edu = document.getElementById('educationField').value;
    const empleo = document.getElementById('workField').value;
    const skills = document.getElementById('skillsField').value;
    const web = document.getElementById('pagField').value;
    const cert = document.getElementById('cerField').value;
    const resumen = document.getElementById('resumeField').value;
    


    if(nombre == "" || correo==""||telefono==""||idioma==""||direccion==""||edu==""||empleo==""||skills==""||web==""||cert==""||resumen==""){
        alert("Asegurese de llenar los campos correctamente");
       
    }else{
        document.getElementById('cv-form').style.display = 'none'
        document.getElementById('cv-template').style.display = 'block';
    }

    //
 

    //Nombre
    let nameField = document.getElementById('nameField').value;

    let nameT1 = document.getElementById('nameT1')

    nameT1.innerHTML = nameField;

    //contacto
    document.getElementById('contactT').innerHTML = document.getElementById('contactField').value;

    //direccion
    document.getElementById('addressT').innerHTML = document.getElementById('addressField').value;

    //correo
    document.getElementById('mailT').innerHTML = document.getElementById('mailField').value;

    //idiomas
    document.getElementById('langT').innerHTML = document.getElementById('langField').value;

    //educacion
    document.getElementById('educacionT').innerHTML = document.getElementById('educationField').value;

    //empleos
    document.getElementById('elT').innerHTML = document.getElementById('workField').value;

    //skills
    document.getElementById('skillsT').innerHTML = document.getElementById('skillsField').value;

    //paginaweb
    document.getElementById('paginaT').innerHTML = document.getElementById('pagField').value;

    //certificacion
    document.getElementById('certificadoT').innerHTML = document.getElementById('cerField').value;

    //resumen
    document.getElementById('resumenT').innerHTML = document.getElementById('resumeField').value;



    //codigo para la configuracion de la imagen
    let file = document.getElementById('imgField').files[0]
    console.log(file);

    let reader = new FileReader()

    reader.readAsDataURL(file);

    console.log(reader.result);

    //Establecer la imagen
    reader.onloadend = function () {
        document.getElementById("imgTemplate").src = reader.result;
    };




}











function imprimirCV() {
    //console.log("Imprimiendo CV");

    window.print();
}