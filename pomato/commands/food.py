import typer
from typing_extensions import Annotated
from pomato.services.food import FoodService

food_service = FoodService()

app = typer.Typer()

@app.command()
def add(
    name: str = typer.Option(..., prompt=True, help="Enter the food name"),
    restaurant: str = typer.Option(..., prompt=True, help="Enter the restaurant name"),
    price: int = typer.Option(..., prompt=True, help="Enter the price"),
    is_veg: bool = typer.Option(True, prompt=True, help="Specify if the food is vegetarian (True/False)")
):
    food_service.add(name, restaurant, price, is_veg)

@app.command()
def remove(
     name: Annotated[str, typer.Option(prompt=True)]
):
    food_service.remove(name)

@app.command()
def display(
    restaurant: Annotated[str, typer.Option(prompt=True)]
):
    food_service.display(restaurant)

@app.command()
def list():
    food_service.list()

if __name__ == "__main__":
    app()
