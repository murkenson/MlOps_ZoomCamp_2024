@data_loader
def load_data(*args, **kwargs):
    filenames = [f'filename_{i}' for i in range(10)]
    return [
        filenames,
    ]