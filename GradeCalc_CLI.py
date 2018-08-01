import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('dark_background')
import click

@click.command()
@click.option('--tests', type=str,
              help='Input exam scores to graph.')

def main(tests):
    """Convert the strings of scores into integers to be graphed.
    """
    tests = [float(grade) for grade in tests.split()]

