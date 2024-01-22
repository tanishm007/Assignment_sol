import pymongo

class PolynomialFunction:
    def __init__(self, expression, variables, constants):
        self.expression = expression
        self.variables = variables
        self.constants = constants

    def evaluate(self, variable_values):
        # Replace variables with their values in the expression
        expression_with_values = self.expression
        for variable, value in variable_values.items():
            replacement = f"*({value})"  # Wrap the value in parentheses for multiplication
            expression_with_values = expression_with_values.replace(variable, replacement)

        # Evaluate the expression with substituted values
        return eval(expression_with_values)
    
    
def retrieve_formulas_from_mongodb():
    # Connect to MongoDB (Make sure you have MongoDB running locally or provide the connection details)
    client = pymongo.MongoClient("mongodb+srv://tanishmahajanm:tanish007@cluster0.51epja8.mongodb.net/?retryWrites=true&w=majority")
    
    # Create or use an existing database
    database = client["Assignment"]
    
    # Create or use an existing collection
    collection = database["polyFun"]
    
    # Retrieve formulas from the collection
    formulas = {}
    for formula_data in collection.find():
        name = formula_data["name"]
        expression = formula_data["expression"]
        variables = formula_data["variables"]
        constants = formula_data["constants"]
        
        formulas[name] = PolynomialFunction(expression, variables, constants)

    return formulas

newformula = {}
newformula = retrieve_formulas_from_mongodb()


def main_function(function_name, variable_values):
    # Store the formulas
    """
    these formulas are already stored in the mongodb and more can be added accordingly
    formulas = {
        'f(x, y)': PolynomialFunction('3x + 4y + 2', ['x', 'y'], ['3', '4', '2']),
        'f(x)': PolynomialFunction('3z + 1', ['z'], ['3', '1']),
        'f(z)': PolynomialFunction('4w + 2', ['w'], ['4', '2']),
        'f(w)': PolynomialFunction('5t + 3', ['t'], ['5', '3']),
        'f(t)': PolynomialFunction('6n + 4', ['n'], ['6', '4'])
    }
    """

    #retrieving the formula from the database 
 
   
    

    # Check if the provided function exists
    if function_name not in newformula:
        raise ValueError(f"Function '{function_name}' not found")

    function = newformula[function_name]
    required_variables = set(function.variables)
    
 
    # Check if provided variables match the required variables
    if required_variables.issubset(set(variable_values.keys())):
        # If variables match, directly evaluate the function
        return compute_function(function, variable_values)
    else:
        
        # If variables are missing, make DFS calls to compute them
        
        variable_values_dict = variable_values.copy()  # Prevent modifying original dict
        for variable in required_variables - set(variable_values.keys()):
            
            result = dfs_for_variable(variable, variable_values, newformula, variable)
         
            
            if result is None:
                print(f"Missing value for variable '{variable}'")
                return None
            else:
                variable_values_dict[variable] = result
        return compute_function(function, variable_values_dict)



def compute_function(function, variable_values_dict):
    # Check if values are integers before assigning
    for variable, value in variable_values_dict.items():
        if not isinstance(value, (int, float)):
            raise ValueError(f"Invalid value '{value}' for variable '{variable}'. Value must be an integer or float.")

    # Evaluate the function
    return function.evaluate(variable_values_dict)


def dfs_for_variable(variable, variable_values, formulas, originalVar):
    
    """
    Recursively finds the value of a variable by making DFS calls to resolve its dependencies.

    Args:
        variable (str): The name of the variable to find.
        variable_values (dict): A dictionary of currently known variable values.
        formulas (dict): A dictionary of available functions and their definitions.

    Returns:
        int or float: The computed value of the variable.

    Raises:
        ValueError: If the variable is not found or has a circular dependency.
    """

    function = formulas.get(f'f({variable})')

    if function:
     if function.variables:
            current_state = {var: variable_values[var] for var in variable_values}
            for sub_variable in function.variables:
                if variable in variable_values:
                    return variable_values[variable]

                if sub_variable not in variable_values:
                    variable_values[sub_variable] = dfs_for_variable(sub_variable, variable_values, formulas, originalVar)

            result = compute_function(function, variable_values)
            variable_values[variable] = result
         
            return result

    else:   
         raise ValueError(f"Variable '{originalVar}' not found in formulas.")





result = main_function('f(x, y)', {'t': 2, 'y': 6})
print("f(x,y):", result)

#handling variable missing case
#ans = main_function('f(x, y)',{'x':10,'w':5 } )
#print("f(x,y): ", ans)

ans = main_function('f(x, y)',{'y':10,'k':5 } )
print("f(x,y): ", ans)



