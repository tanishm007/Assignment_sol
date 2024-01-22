Assignment Solution
Part 1 - How to store & retrieve “function” or “formulas”
Here is the solution :
GitHub link - Assignment_sol/backend.py at main · tanishm007/Assignment_sol (github.com)

Explaination of code
The PolynomialFunction class represents a mathematical polynomial function. It is initialized with an expression, a list of variables, and a list of constants. The class provides a method evaluate(variable_values) to calculate the result of the polynomial function by substituting the provided variable values into the expression.

The save_formulas_to_mongodb function connects to a MongoDB database and inserts a dictionary of polynomial function formulas into a specified collection. Each formula in the dictionary is stored as a document in the collection.

The add_formula_to_mongodb function connects to a MongoDB database and adds a new polynomial function formula to a specified collection. It takes the name, expression, variables, and constants of the formula as inputs, creates a PolynomialFunction instance, and inserts the formula data into the MongoDB collection.

The retrieve_formulas_from_mongodb function connects to a MongoDB database, retrieves polynomial function formulas from a specified collection, and returns a dictionary of PolynomialFunction instances. Each formula is stored with a unique name as the key in the dictionary.




Part 2 - How to execute & return end_result
Github Link - Assignment_sol/solPart2.py at main · tanishm007/Assignment_sol (github.com)

Approach :
 
The PolynomialFunction class represents a mathematical polynomial function. It takes an expression, a list of variables, and a list of constants as inputs during initialization. The class provides a method evaluate(variable_values) to calculate the result of the polynomial function by substituting the provided variable values into the expression.

The main_function is the main entry point for evaluating polynomial functions. It takes the name of a polynomial function and a dictionary of variable values as inputs. It retrieves the function from the previously retrieved formulas, checks for missing variables, and computes the function's result. If variables are missing, it recursively resolves them using a Depth-First Search (DFS) approach.

The compute_function function takes a PolynomialFunction instance and a dictionary of variable values as inputs. It checks the provided values for validity and evaluates the polynomial function using the evaluate method of the PolynomialFunction class.

The dfs_for_variable function recursively finds the value of a variable by making DFS calls to resolve its dependencies. It takes the name of the variable, a dictionary of variable values, a dictionary of available formulas, and the original variable to catch missing variable. It returns the computed value of the variable.





