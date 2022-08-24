var pizzaList = []

function dojoPizza(name, sauce, cheese, toppings) {
    var pizza = {}
    pizza.name = name
    pizza.sauce = sauce
    pizza.cheese = cheese
    pizza.toppings = toppings
    return pizza
}

pizzaList.push(dojoPizza("bbq chicken pizza", "bbq sauce", "mozzarella", ["chicken", "onions", "cilantro", "jalapenos", "veggies"]))

pizzaList.push(dojoPizza("margarita", "marinara", "mozzarella", ["basil", "tomatoes", "spinach"]))

pizzaList.push(dojoPizza("the purple monster", "sriracha + purple ketchup", "goat cheese + feta cheese", ["marshmallows", "stinky tofu", "gummy worms", "lint"]))

//console.log(pizzaList)

function randomPizza(list){
    return list[Math.floor(Math.random() *list.length)]
}

console.log(randomPizza(pizzaList))