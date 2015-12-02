<head>
...
    <script type="text/javascript"
            src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
    </script>
...
</head>

# Week-Last-Assignment
##The Last Lab!

For our final lab, we are going to explore a couple of very useful Math algorithms and how we can code them in Python.  Also, we will take one of them and explore the performance difference between an imperitive and a recursive version of the algorithms.  

###Euclid's GCD Algorithms

Euclid's algorithm, is an efficient method for computing the greatest common divisor of two numbers, the largest number that divides both of them without leaving a remainder.  The original version of the Euclidean algorithm can take many subtraction steps to find the GCD when one of the given numbers is much bigger than the other. A more efficient version of the algorithm shortcuts these steps, instead replacing the larger of the two numbers by its remainder when divided by the smaller of the two.

As with any recursive algorithm, you need to know 2 things:.  
	1. The base case(es)  
	2. The recursion  

For GCD, the recursion is:  
**GCD(x , y ) = GCD(y, x % y)**

If you walk through an example by hand, you will discover that eventually the base case is when y = 0. At that point, you return x, which should then be the GCD.  

###N of K combinations  

We are going to let our wonderful math education majors explain this, but the crux of the idea represented here is that if you have K total items, how many different ways can you pick N different items out of this.

Lets say that I have three students:  

Alice  
Bob  
Charlie  

And I want to put 2 of them into a group together.  How many different groups can I make?  Well, I can choose:  

Alice & Bob  
Alice & Charlie  
Bob & Charlie  

So with 2 out of 3, we can get 3 choices. Simple enough, but think if I want to pick 5 out of 20?  (n = 20, k = 5) Is there a formula for this?  Yes, 
\\( 1/x^{2} \\), and here is a block rendering: 
\\[ \frac{1}{n^{2}} \\]

<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>C</mi><mi>k</mi><mi>n</mi></msubsup><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mi>k</mi><mo>!</mo><mo>(</mo><mi>n</mi><mo>&#160;</mo><mo>-</mo><mo>&#160;</mo><mi>k</mi><mo>)</mo><mo>!</mo></mrow></mfrac></math>

Interestingly, you can also write this as a recursion:  

<math xmlns="http://www.w3.org/1998/Math/MathML"><msubsup><mi>C</mi><mi>k</mi><mi>n</mi></msubsup><mo>&#160;</mo><mo>=</mo><mo>&#160;</mo><msubsup><mi>C</mi><mrow><mi>k</mi><mo>-</mo><mn>1</mn></mrow><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msubsup><mo>&#160;</mo><mo>+</mo><mo>&#160;</mo><msubsup><mi>C</mi><mi>k</mi><mrow><mi>n</mi><mo>-</mo><mn>1</mn></mrow></msubsup></math>

In this repository is the code for this function written the first way, as an imperative equation using factorials.  For this lab we are going to write a version of this function using a recursion.  Then we are going to run a timed exercise to see if there is any difference in performance.  

For the recursive version, here is what you need to know:  

The base cases:  
	if n == k return 1 (one of one choices left)  
	if k == 0 return 1 (no choices left)

The recursion:  
subset(n,k) = subset(n-1,k-1) + subset(n-1,k)
