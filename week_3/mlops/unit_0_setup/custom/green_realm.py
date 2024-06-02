from typing import Dict, List


@custom
def load_data(*args, **kwargs) -> List[List[Dict]]:
    datasets = ['netflix-shows', 'hulu-movies-and-tv-shows']
    metadata = []

    for i, dataset in enumerate(datasets):
        dataset_id = i + 1
        datasets[i] = {'id': dataset_id, 'name': dataset}
        metadata.append(dict(block_uuid=f'for_dataset_{i}'))

    return [
        datasets,
        metadata,
    ]