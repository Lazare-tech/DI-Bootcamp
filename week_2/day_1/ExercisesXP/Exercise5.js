typeof(15)
// Prediction:number
// Actual:15

typeof(5.5)
// Prediction:decimal
// Actual:5.5
typeof(NaN)
// Prediction:undefined
// Actual:0

typeof("hello")
// Prediction:string
// Actual:hello
typeof(true)
// Prediction:boolean
// Actual:true
typeof(1 != 2)
// Prediction:
// Actual:

"hamburger" + "s"
// Prediction:concatenation
// Actual:hamburgers

"hamburgers" - "s"
// Prediction:we cannot concat with a sign -
// Actual:Nan
"1" + "3"
// Prediction:concatenation,it will output 13
// Actual:13

"1" - "3"
// Prediction:it take 1 and 3 like a number and make the operation
// Actual:-2

"johnny" + 5
// Prediction:concatenation,it will output johnny5
// Actual:johnny5

"johnny" - 5
// Prediction:we cannot concat with the sign -
// Actual:Nan


99 * "hello"
// Prediction:impossible to concat with the multiplication sign
// Actual:nan

1 != 1
// Prediction:comparaison,it is a boolean expression,1 is not different to 1
// Actual:false

1 == "1"
// Prediction:boolean expression,it is compare the equality
// Actual:true
1 === "1"
// Prediction:boolean expression,it compare the type,1 is a number or "1" is strinf
// Actual:false