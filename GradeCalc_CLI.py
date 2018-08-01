import matplotlib.pyplot as plt
plt.style.use('dark_background')
import click

@click.command()
@click.option('--tests', type=str,
              help='Input exam scores to graph.')

def main(tests):
    """Convert the strings of scores into integers to be graphed.
    """
    tests = [float(grade) for grade in tests.split()]


    x = range(len(tests))
    y = tests

    plt.scatter(x, y)

    plt.xlabel('Exams')

    plt.ylabel('Grades')

    plt.title('Class Grades')

    plt.show()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
