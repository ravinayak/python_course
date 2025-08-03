#!/usr/bin/env python3
"""
Test file to demonstrate different import scenarios and name collisions
"""

# Scenario 1: Module-level import
print("=== Scenario 1: import my_app.components.utils ===")
import my_app.components.utils

# Local function with same name
def ab():
    return "This is local function ab"

# No collision - different namespaces
print("utils.ab():", my_app.components.utils.ab())
print("local ab():", ab())
print()

# Scenario 2: From import
print("=== Scenario 2: from my_app.components import utils ===")
from my_app.components import utils

# Still no collision - utils is a namespace
print("utils.ab():", utils.ab())
print("local ab():", ab())
print()

# Scenario 3: Direct function import - POTENTIAL COLLISION!
print("=== Scenario 3: from my_app.components.utils import ab ===")
from my_app.components.utils import ab as imported_ab  # Using alias to avoid collision

# Now we have both imported_ab and local ab
print("imported_ab():", imported_ab())
print("local ab():", ab())
print()

# Scenario 4: What happens without alias (collision)
print("=== Scenario 4: Direct import without alias (COLLISION) ===")
# Uncomment the next line to see the collision:
# from my_app.components.utils import ab  # This would override local ab

# If we did the above import, then:
# ab() would call the imported function, not the local one
# The local ab() function would be shadowed

print("Demonstrating what happens with collision:")
print("If we do: from my_app.components.utils import ab")
print("Then: ab() would call the imported function")
print("The local ab() function would be shadowed")
print()

# Scenario 5: Best practices
print("=== Scenario 5: Best Practices ===")
print("1. Use module-level imports for clarity:")
print("   import my_app.components.utils")
print("   my_app.components.utils.ab()")
print()

print("2. Use from import with namespace:")
print("   from my_app.components import utils")
print("   utils.ab()")
print()

print("3. Use aliasing when importing specific functions:")
print("   from my_app.components.utils import ab as utils_ab")
print("   utils_ab()  # imported function")
print("   ab()        # local function")
print()

print("4. Avoid direct imports that might cause collisions:")
print("   # Avoid: from my_app.components.utils import ab")
print("   # Unless you're sure no local function with same name exists") 