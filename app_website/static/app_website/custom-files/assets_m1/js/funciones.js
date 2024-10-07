// Funcion para validar teclas en inputs solo numeros
function limpiarReportValidity(inputElement) {
    inputElement.setCustomValidity("");
    //inputElement.reportValidity();
    //console.log("LIMPIO")
    return;
}


//Funcion para validar teclas en inputs solo numeros
function soloNumeros(e, inputElement) {
    let ASCIICode = (e.which) ? e.which : e.keyCode;
    if (ASCIICode == 46 || ASCIICode == 44) {
        return true;
     }
     if (ASCIICode > 31 && (ASCIICode < 48 || ASCIICode > 57)) {
         return false;
     } else {
         return true;
     }
 }

// Funcion para dar formato a los numeros en Inputs onblur
function FormatearNumerosInputs(inputElement, evaluarMayorCero) {
     const valor = inputElement.value;
    if (valor.length < 3) {
        nStr_con_punto = valor.replace(/,/g, '.');
        let cifra_2_decimales = Number(nStr_con_punto).toFixed(2);
        let nueva_cifra = cifra_2_decimales * 1;
        const cifra_formateada = nueva_cifra.toLocaleString('es-VE', { minimumFractionDigits: 2 });
        inputElement.value = cifra_formateada;
    };
    // Si es verdadero evalua si es mayor que 0
    if (evaluarMayorCero) { 
        let nStr_sin_punto = inputElement.value.replace(/\./g, '');
        let nStr_con_punto = nStr_sin_punto.replace(/,/g, '.');
        var num = nStr_con_punto * 1;
        if (num > 0) {
            return true;
        } else {
            inputElement.setCustomValidity("Ingrese un monto mayor a 0,00");
            inputElement.reportValidity();
            return false;
        }
    }
    return;
}


//Funcion para dar formato a los numeros en las salidas
function darFormato(cifra) {
    let cifra_2_decimales = Number(cifra).toFixed(2);
    let nueva_cifra = cifra_2_decimales * 1;
    const cifra_formateada = nueva_cifra.toLocaleString('es-VE', { minimumFractionDigits: 2 });
    //const price = 181.5;
    //const formattedPrice = price.toLocaleString('es-VE', { style: 'currency', currency: 'USD' });
    //console.log(formattedPrice)
    return cifra_formateada
}


//Funcion remplazar coma por puntos y poder hacer opereaciones en JS
function quitarFormato(nStr) {
    
    let nStr_sin_punto = nStr.replace(/\./g, ''); // eliminar el punto en el formato
    let nStr_con_punto = nStr_sin_punto.replace(/,/g, '.'); // sustituir la como por el ponto en el formato
    //console.log("quitarFormato a",nStr, "=",nStr_con_punto)
    return nStr_con_punto
}

//Funcion para validar que se mayor de 0
// function Mayor0(e) {
//     if (parseFloat(e.value) > 0) {
//         e.value = parseFloat(e.value).toFixed(2);
//         validation_msg.setAttribute("hidden", false);
//         let nStrTMP = document.getElementById(e.id).value
//         document.getElementById(e.id).value = 0
//         document.getElementById(e.id).value = parseFloat(nStrTMP).toFixed(2)
//         return true;
//     } else {
//         validation_msg.removeAttribute("hidden");
//         e.value = "";
//         e.focus();
//         setTimeout(() => {
//             validation_msg.setAttribute("hidden", false);
//         }, 3000);
//         return false;
//     }
// };


//Funcion para validar al Guardar que se mayor de 0 
function mayorCero(inputElement) {
    let nStr = inputElement.value;
    let nStr_sin_punto = nStr.replace(/\./g, ''); // eliminar el punto en el formato
    let nStr_con_punto = nStr_sin_punto.replace(/,/g, '.'); // sustituir la como por el ponto en el formato
    var num = nStr_con_punto * 1;
    if (num > 0) {
        return true;
    } else {
        inputElement.setCustomValidity("Ingrese un monto mayor a 0,00");
        inputElement.reportValidity();
        return false;
    }
};


//Funcion para mostrar msg de un campo validado
//function Mostra_validation_msg(id_campo, campo_validation_msg) {
//    document.getElementById(campo_validation_msg).removeAttribute("hidden");
//    document.getElementById(id_campo).focus();
//};

//Funcion para ocultar msg de un campo validado
//function Ocultar_validation_msg(campo_validation_msg) {
//    document.getElementById(campo_validation_msg).setAttribute("hidden", false);
//};

// llena la fecha con la fecha de hoy
function get_hoy(elemento) {
    let today = new Date();
    let dd = String(today.getDate()).padStart(2, '0');
    let mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    let yyyy = today.getFullYear();
    elemento.value = yyyy + '-' + mm + '-' + dd;
};

// Funcion para dar formato a los numeros en Inputs al cargar para editar
function FormatearNumerosInputs2(inputElement) {
    const valor = inputElement.value;
    nStr_con_punto = valor.replace(/,/g, '.');
    let cifra_2_decimales = Number(nStr_con_punto).toFixed(2);
    let nueva_cifra = cifra_2_decimales * 1;
    const cifra_formateada = nueva_cifra.toLocaleString('es-VE', { minimumFractionDigits: 2 });
    inputElement.value = cifra_formateada;
    return;
}