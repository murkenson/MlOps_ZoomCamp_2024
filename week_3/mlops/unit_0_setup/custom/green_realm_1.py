if "custom" not in globals():
    from mage_ai.data_preparation.decorators import custom
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):
    """
    args: The output from any upstream parent blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your custom logic here

    download_info = [
        "netflix-shows",
        "amazon-prime-movies-and-tv-shows",
        "hulu-movies-and-tv-shows",
        "disney-movies-and-tv-shows",
    ]

    return [download_info]
