5 + "34"
// Prediction:it is a concatenate expression
// Actual:534
5 - "4"
// Prediction:the sign - transform "4" like a number and make operation
// Actual:1
10 % 5
// Prediction:the expression give the remainder of euclidean division
// Actual:0
5 % 10
// Prediction:the expression give the remainder of euclidean division
// Actual:5
"Java" + "Script"
// Prediction:the expression is a concatenation
// Actual:javaScript
" " + " "
// Prediction:it is return nothing
// Actual:empty string

" " + 0
// Prediction:the expression concat an empty string with q number
// Actual:0
true + true
// Prediction:true is considered like 1 and false 0
// Actual:2

true + false
// Prediction:true is considered like 1 and false 0
// Actual:1
false + true
// Prediction:true is considered like 1 and false 0
// Actual:1
false - true
// Prediction::true is considered like 1 and false 0,it return -1
// Actual:-1
!true
// Prediction:the expression is true
// Actual:false

3 - 4
// Prediction:make an operation
// Actual:-1
"Bob" - "bill"
// Prediction:wrong concatenation
// Actual:nan