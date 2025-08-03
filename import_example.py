# Example demonstrating import behavior and name collisions

# Scenario 1: Module-level import
import my_app.components.utils

# This creates a namespace 'my_app.components.utils'
# To access function 'ab' from utils, you would use:
# my_app.components.utils.ab()

# Scenario 2: From import
from my_app.components import utils

# This creates a namespace 'utils' in current scope
# To access function 'ab' from utils, you would use:
# utils.ab()

# Scenario 3: Direct import of function
from my_app.components.utils import ab

# This brings 'ab' directly into current scope
# You can use it directly as: ab()

# Let's demonstrate with actual code:
def demonstrate_imports():
    print("=== Import Behavior Demonstration ===")
    
    # Scenario 1: Module-level import
    print("1. import my_app.components.utils")
    print("   - Creates namespace: my_app.components.utils")
    print("   - Access with: my_app.components.utils.ab()")
    print("   - No name collision with local 'ab' function")
    print()
    
    # Scenario 2: From import
    print("2. from my_app.components import utils")
    print("   - Creates namespace: utils")
    print("   - Access with: utils.ab()")
    print("   - No name collision with local 'ab' function")
    print()
    
    # Scenario 3: Direct function import
    print("3. from my_app.components.utils import ab")
    print("   - Brings 'ab' directly into current scope")
    print("   - Access with: ab()")
    print("   - POTENTIAL COLLISION if local 'ab' function exists!")
    print()
    
    # Scenario 4: Aliasing to avoid collision
    print("4. from my_app.components.utils import ab as utils_ab")
    print("   - Brings 'ab' as 'utils_ab' into current scope")
    print("   - Access with: utils_ab()")
    print("   - No collision with local 'ab' function")

def local_function_ab():
    """Local function with same name as imported function"""
    return "This is the local function ab"

if __name__ == "__main__":
    demonstrate_imports()
    
    # Example of collision scenario
    print("\n=== Name Collision Example ===")
    
    # This would cause collision:
    # from my_app.components.utils import ab
    # def ab():  # This would override the imported ab
    #     return "local ab"
    
    # Solution: Use aliasing
    # from my_app.components.utils import ab as utils_ab
    # def ab():  # This is now separate from utils_ab
    #     return "local ab" 