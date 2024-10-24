// 1. Calcular el área de un rectángulo
let base = prompt("Ingrese la base del rectángulo:");
let altura = prompt("Ingrese la altura del rectángulo:");
let areaRectangulo = base * altura;
console.log("El área del rectángulo es:", areaRectangulo);

// 2. Convertir grados Celsius a Fahrenheit
let celsius = prompt("Ingrese los grados Celsius:");
let fahrenheit = celsius * 9/5 + 32;
console.log(celsius + " grados Celsius equivalen a " + fahrenheit + " grados Fahrenheit.");   


// 3. Calcular promedio de 3 calificaciones
let calificacion1 = prompt("Ingrese la primera calificación:");
let calificacion2 = prompt("Ingrese la segunda calificación:");
let calificacion3 = prompt("Ingrese la tercera calificación:");
let promedio = (parseFloat(calificacion1) + parseFloat(calificacion2) + parseFloat(calificacion3)) / 3;
console.log("El promedio es:", promedio);

// 4. Convertir kilómetros a millas
let kilometros = prompt("Ingrese los kilómetros:");
let millas = kilometros * 0.621371;
console.log(kilometros + " kilómetros equivalen a " + millas + " millas.");

// 5. Calcular interés simple
let capital = prompt("Ingrese el capital:");
let tasaInteres = prompt("Ingrese la tasa de interés (en decimal):");
let tiempo = prompt("Ingrese el tiempo (en años):");
let interes = capital * tasaInteres * tiempo;
console.log("El interés simple es:", interes);

// 6. Clasificar calificaciones
let calificacion = prompt("Ingrese la calificación (de 0 a 100):");
if (calificacion >= 90) {
  console.log("Excelente");
} else if (calificacion >= 70) {
  console.log("Aprobado");
} else if (calificacion >= 50) {
  console.log("Necesita mejorar");
} else {
  console.log("Reprobado");
}

// 7. Clasificar triángulos
let lado1 = prompt("Ingrese el primer lado del triángulo:");
let lado2 = prompt("Ingrese el segundo lado del triángulo:");
let lado3 = prompt("Ingrese el tercer lado del triángulo:");

if (lado1 <= 0 || lado2 <= 0 || lado3 <= 0) {
  console.log("Los lados de un triángulo deben ser positivos.");
} else if (lado1 + lado2 <= lado3 || lado1 + lado3 <= lado2 || lado2 + lado3 <= lado1) {
  console.log("Los lados ingresados no forman un triángulo válido.");
} else if (lado1 === lado2 && lado2 === lado3) {
  console.log("El triángulo es equilátero.");
} else if (lado1 === lado2 || lado1 === lado3 || lado2 === lado3) {
  console.log("El triángulo es isósceles.");
} else {
  console.log("El triángulo es escaleno.");
}