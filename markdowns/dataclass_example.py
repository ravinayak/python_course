"""
Comprehensive example showing what @dataclass automatically generates.
"""

from dataclasses import dataclass, field
from typing import List, Dict


# Example 1: Basic dataclass
@dataclass
class BasicPerson:
    name: str
    age: int = 25
    city: str = "Unknown"


# Example 2: Dataclass with custom methods
@dataclass
class AdvancedPerson:
    name: str
    age: int = 25
    city: str = "Unknown"
    hobbies: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """Runs automatically after __init__"""
        if self.age < 0:
            raise ValueError("Age cannot be negative")
    
    def is_adult(self) -> bool:
        """Custom method - not auto-generated"""
        return self.age >= 18


# Example 3: Immutable dataclass
@dataclass(frozen=True)
class ImmutablePerson:
    name: str
    age: int
    city: str = "Unknown"


# Example 4: Dataclass with field customization
@dataclass
class CustomPerson:
    name: str
    age: int = field(default=25, repr=True, compare=True)
    city: str = field(default="Unknown", repr=False, compare=False)
    _secret_id: str = field(default="", repr=False, init=False)
    
    def __post_init__(self):
        import uuid
        self._secret_id = str(uuid.uuid4())


# Example 5: Dataclass with inheritance
@dataclass
class Employee(BasicPerson):
    salary: float = 0.0
    department: str = "Unknown"


# Example 6: Dataclass with complex defaults
@dataclass
class Team:
    name: str
    members: List[str] = field(default_factory=list)
    scores: Dict[str, int] = field(default_factory=dict)
    captain: str = field(default="", init=False)
    
    def __post_init__(self):
        if self.members:
            self.captain = self.members[0]


def demonstrate_auto_generated_methods():
    """Demonstrate all the automatically generated methods."""
    
    print("=== BASIC DATACLASS ===")
    person1 = BasicPerson("Alice", 30, "New York")
    person2 = BasicPerson("Alice", 30, "New York")
    person3 = BasicPerson("Bob", 25)
    
    # __init__ method (auto-generated)
    print(f"person1: {person1}")
    
    # __repr__ method (auto-generated)
    print(f"repr(person1): {repr(person1)}")
    
    # __eq__ method (auto-generated)
    print(f"person1 == person2: {person1 == person2}")
    print(f"person1 == person3: {person1 == person3}")
    
    print("\n=== ADVANCED DATACLASS ===")
    advanced_person = AdvancedPerson("Charlie", 17, "Boston", ["reading", "swimming"])
    
    # __post_init__ validation (auto-called)
    try:
        invalid_person = AdvancedPerson("Invalid", -5)
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # Custom method (not auto-generated)
    print(f"Is adult: {advanced_person.is_adult()}")
    
    print("\n=== IMMUTABLE DATACLASS ===")
    immutable_person = ImmutablePerson("David", 40, "Chicago")
    
    # __hash__ method (auto-generated for frozen=True)
    print(f"Hash: {hash(immutable_person)}")
    
    # Cannot modify (frozen=True)
    try:
        immutable_person.age = 41
    except Exception as e:
        print(f"Cannot modify: {e}")
    
    print("\n=== CUSTOM FIELD DATACLASS ===")
    custom_person = CustomPerson("Eve", 28, "Seattle")
    
    # city is hidden from repr (repr=False)
    print(f"Custom person: {custom_person}")
    
    # _secret_id is hidden from repr and init
    print(f"Secret ID: {custom_person._secret_id}")
    
    print("\n=== INHERITANCE ===")
    employee = Employee("Frank", 35, "LA", 75000.0, "Engineering")
    print(f"Employee: {employee}")
    
    print("\n=== COMPLEX DEFAULTS ===")
    team = Team("Avengers", ["Iron Man", "Captain America", "Thor"])
    print(f"Team: {team}")
    print(f"Captain: {team.captain}")


if __name__ == "__main__":
    demonstrate_auto_generated_methods() 