import pytest


def download_images(url, path):
    pass


def extract_images(path):
    pass


@pytest.fixture(scope='session')
def images_dir(tmpdir_factory):
    directory = tmpdir_factory.mktemp('images')
    download_images('https://example.com/samples.zip', directory)
    extract_images(directory / 'samples.zip')


def apply_blur_filter(image):
    pass


def test_blur_filter(images_dir):
    output_image = apply_blur_filter(images_dir / 'rock1.png')
