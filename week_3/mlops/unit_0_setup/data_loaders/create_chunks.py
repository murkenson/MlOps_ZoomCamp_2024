if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):

    chunks = []

    for i in range(2):
        chunks.append(dict(id=i, num=i*11))
        i += 1

    return [
        chunks
    ]
