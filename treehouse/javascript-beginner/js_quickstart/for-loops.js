const numbers = [1,2,3,4,5,6,7,8,9,10];
let times5 = [];

// times5 should be: [5,10,15,20,25,30,35,40,45,50]
// Write your code below

// times5 = numbers.map(num => num * 5);
// console.log(times5);

numbers.forEach(function(num){
    times5.push(num * 5)
});

console.log(times5)

// for ( let counter = 1; counter < 10; counter++) {
//     console.log( counter );
// } 
// logs 1, 2, 3, 4, 5, 6, 7, 8, 9

const fruits = ['apple', 'pear', 'cherry'];
  
for (i = 0; i < fruits.length; i++) {
    console.log(fruits[i])
}
// logs apple, pear, cherry

const capitalizedFruits = fruits.map( fruit => fruit.toUpperCase() );
console.log(capitalizedFruits) // [ 'APPLE', 'PEAR', 'CHERRY' ]