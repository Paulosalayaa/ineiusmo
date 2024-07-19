import click

@click.command()
@click.option('--output', default='output', help='Output directory')
def my_command(output):
    # Your function logic here
    # You can access the value of the --output option through the 'output' parameter

    # Example usage
    print(f"Output directory: {output}")

if __name__ == '__main__':
    my_command()
