@custom
def transform_custom(filename, *args, **kwargs):
    print(f'Fetch data from only 1 file: {filename}')

    return dict(filename=filename, data=f'Some data for file {filename}')