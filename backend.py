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
    
client = pymongo.MongoClient("mongodb+srv://tanishmahajanm:tanish007@cluster0.51epja8.mongodb.net/?retryWrites=true&w=majority")
    
    # Create or use an existing database
database = client["Assignment"]
    
    # Create or use an existing collection
collection = database["polyFun"]
    
def retrieve_formulas_from_mongodb():
    # Connect to MongoDB (Make sure you have MongoDB running locally or provide the connection details)
   

    # Retrieve formulas from the collection
    formulas = {}
    for formula_data in collection.find():
      
        name = formula_data["name"]
        expression = formula_data["expression"]
        variables = formula_data["variables"]
        constants = formula_data["constants"]
        
        formulas[name] = PolynomialFunction(expression, variables, constants)

    return formulas

def add_formula_to_mongodb(name, expression, variables, constants):
    # Connect to MongoDB (Make sure you have MongoDB running locally or provide the connection details)

    # Insert the formula into the collection
    formula = PolynomialFunction(expression, variables, constants)
    formula_data = {
        "name": name,
        "expression": formula.expression,
        "variables": formula.variables,
        "constants": formula.constants
    }
    collection.insert_one(formula_data)
    print(f"Formula '{name}' added to MongoDB")

def save_formulas_to_mongodb(formulas):
    # Connect to MongoDB (Make sure you have MongoDB running locally or provide the connection details)

    
    # Insert formulas into the collection
    for name, formula in formulas.items():
        formula_data = {
            "name": name,
            "expression": formula.expression,
            "variables": formula.variables,
            "constants": formula.constants
        }
        collection.insert_one(formula_data)

def main_function():
    # Store the formulas
    formulas = {
        'f(x, y)': PolynomialFunction('3x + 4y + 2', ['x', 'y'], ['3', '4', '2']),
        'f(x)': PolynomialFunction('3z + 1', ['z'], ['3', '1']),
        'f(z)': PolynomialFunction('4w + 2', ['w'], ['4', '2']),
        'f(w)': PolynomialFunction('5t + 3', ['t'], ['5', '3']),
        'f(t)': PolynomialFunction('6n + 4', ['n'], ['6', '4'])
    }

    retrieve_formulas_from_mongodb()
    
    save_formulas_to_mongodb(formulas)
    # Save formulas to MongoDB
    #save_formulas_to_mongodb(formulas)
    print("formulas saved in mongodb")
    

main_function()
 



