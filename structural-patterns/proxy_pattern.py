from abc import ABC, abstractmethod

class ImagesLoader(ABC):

    @abstractmethod
    def load_images(self, image):
        pass

    @abstractmethod
    def display_images(self):
        pass


class Images(ImagesLoader):

    def __init__(self):
        self.images = []

    def load_images(self, image):
        print('Images have been loaded')
        self.images.append(image)

    def display_images(self):
        for image in self.images:
            print(image)


#our proxy checks things before updating our main 
class ImagesProxy(ImagesLoader):

    def __init__(self, images: Images):
        self.images = images

    def load_images(self, image):
        if len(self.images.images) > 5:
            print('Too many images')
            return
        
        self.images.load_images(image)

    def display_images(self):
        if len(self.images.images) >= 6:
            print('Too many images')
            return
        
        for image in self.images.images:
            print(image)


if __name__ == '__main__':

    realImages = Images()
    imagesProxy = ImagesProxy(realImages)
    
    imagesProxy.load_images('test')
    imagesProxy.display_images()

    imagesProxy.load_images('test')
    imagesProxy.display_images()

    imagesProxy.load_images('test')
    imagesProxy.display_images()

    imagesProxy.load_images('test')
    imagesProxy.display_images()

    imagesProxy.load_images('test')
    imagesProxy.display_images()

    imagesProxy.load_images('test')
    imagesProxy.display_images()

    imagesProxy.load_images('test')
    imagesProxy.display_images()
