import logging
from element import Element


class Whiteboard(object):

    def __init__(self):
        self.elements = []
        self.logger = logging.getLogger(__name__)

    def add_element(self, element):
        element.send_audio_parameters()
        self.elements.append(element)
        self.logger.info('Added %s' % str(element))

    def delete_element(self, element):
        element.stop_audio()
        self.elements.remove(element)
        self.logger.info('Deleted %s' % str(element))

    def update_element(self, element, threshold=0.3, **params):
        element.update_parameters(threshold, **params)
        self.logger.info('Updated %s' % str(element))

    def get_element(self, element_id):
        for element in self.elements:
            if element.id == element_id:
                return element
        return None

    def get_element_ids(self):
        return [element.id for element in self.elements]

    def update(self, new_params):
        self.delete_removed_elements(new_params)
        for params in new_params:
            element = self.get_element(params['id'])
            if element:
                self.update_element(element, **params)
            else:
                element = Element.factory(**params)
                self.add_element(element)

    def get_removed_elements(self, new_params):
        new_element_ids = [params['id'] for params in new_params]
        removed_elements = [element for element in self.elements
                            if element.id not in new_element_ids]
        return removed_elements

    def delete_removed_elements(self, new_params):
        for element in self.get_removed_elements(new_params):
            self.delete_element(element)
