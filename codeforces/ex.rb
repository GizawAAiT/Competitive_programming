# Basic Component
class BasicPizza
  def cost
    10
  end

  def ingredients
    "Cheese"
  end
end

# Decorator
class PizzaDecorator
  def initialize(basic_pizza)
    @basic_pizza = basic_pizza
  end

  def cost
    @basic_pizza.cost
  end

  def ingredients
    @basic_pizza.ingredients
  end
end

# Additional Components
class Pepperoni < PizzaDecorator
  def cost
    super + 2
  end

  def ingredients
    super + ", Pepperoni"
  end
end

class Mushrooms < PizzaDecorator
  def cost
    super + 1.5
  end

  def ingredients
    super + ", Mushrooms"
  end
end

class Pineapple < PizzaDecorator
  def cost
    super + 1.5
  end

  def ingredients
    super + ", Pineapple"
  end
end

pizza = BasicPizza.new
pizza = Pepperoni.new(pizza)
pizza = Mushrooms.new(pizza)
pizza = Pineapple.new(pizza)

puts "Cost: #{pizza.cost}"
puts "Ingredients: #{pizza.ingredients}"
